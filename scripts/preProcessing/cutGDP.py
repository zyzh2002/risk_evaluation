import numpy as np
import scipy as sp
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import xarray as xr
import rioxarray as rxr
import rasterio as rio
from affine import Affine
import multiprocessing as mp
import os
from rasterio.enums import Resampling

file_paths = [os.path.join(r"E:\risk_evaluation\scripts\datas\GDP\extracted\\"+str(i)+"GDP.tif") for i in range(2000, 2016)]

border_frame = gpd.read_file(r"E:\risk_evaluation\scripts\preProcessing\border.json")

def process_file(file):
    print("Processing: "+os.path.basename(file)[:-4])

    frame = xr.open_dataset(file).squeeze("band",drop=True)

    frame = frame.rio.reproject("EPSG:4326")

    frame = frame.rio.clip(border_frame.geometry, frame.rio.crs)

    frame_resampled = frame.rio.reproject(
        frame.rio.crs, shape=(1800, 1560), resampling=Resampling.bilinear)

    frame_resampled.to_netcdf(os.path.join(r"E:\risk_evaluation\scripts\outputs\GDP\\"+os.path.basename(file)[:-4]+"_resampled.nc"))

if __name__ == "__main__":
    with mp.Pool(4) as pool:
        pool.map(process_file,file_paths)