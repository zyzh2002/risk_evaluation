import numpy as np
import scipy as sp
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import xarray as xr
import shapely
import rioxarray as rxr
import rasterio as rio
from affine import Affine
import multiprocessing
import os


def generate_filename_map(year:str)->dict:

    def generate_filename(year:str,date:str)->str:
        preifx = 'MOD16A2GF.006_PET_500m_doy'
        suffix = '_aid0001.tif'
        return preifx+year+date+suffix

    def calc_days(start:int,end:int)->list:
        length = end-start
        counts = length//8
        days = []
        for i in range(counts):
            days.append(start+i*8)
        days.append(end)
        return days

    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    months_start_date_lst = [1,33,57,89,121,153,185,209,241,273,305,337]
    months_end_date_lst = [25,49,81,113,145,177,209,233,265,297,329,361]

    filename_map = {}

    for i in range(len(months)):
        start = months_start_date_lst[i]
        end = months_end_date_lst[i]
        days = calc_days(start,end)
        filename_map[months[i]] = []
        for day in days:
            filename_map[months[i]].append(generate_filename(year,str(day).zfill(3)))

    return filename_map

def resample_pet_and_save(year:str)->None:

    filename_map = generate_filename_map(year)

    for month in filename_map.keys():
        print("Processing month: ",month)
        month_frames = []
        for filename in filename_map[month]:
            print("Processing file: ",filename)
            frame = xr.open_dataset(os.path.join(base_path,filename))
            frame = frame.squeeze("band",drop=True)
            month_frames.append(frame)
        month_frames = xr.concat(month_frames,dim="time",data_vars=["band_data"])
        month_frames_max_prod=month_frames.max(dim="time")*len(filename_map[month])
        # resampling
        month_frames_max_resampled = month_frames_max_prod.rio.reproject(month_frames_max_prod.rio.crs,shape=(1800,1560),resampling=rio.enums.Resampling.bilinear)
        month_frames_max_resampled.rio.write_crs("EPSG:4326",inplace=True)
        month_frames_max_resampled.rio.write_coordinate_system(inplace=True)
        month_frames_max_resampled.to_netcdf(os.path.join(output_path,year+"_"+str(month).zfill(2)+".nc"))
        print("Month: ",month," done!")

base_path = os.path.join("scripts/datas/MODIS/MODIS16A2GF/PET")
output_path = os.path.join("scripts/outputs/PET")

if __name__ == "__main__":
    pool = multiprocessing.Pool(os.cpu_count())
    pool.map(resample_pet_and_save,[str(i) for i in range(2000,2016)])