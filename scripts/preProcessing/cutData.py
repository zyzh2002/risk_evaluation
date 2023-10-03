import geopandas as gpd
import xarray as xr
import os
import multiprocessing as mp
import rioxarray as rxr
import shapely

def cut_precip_and_save(file_path):
    print(file_path)
    border = border_frame # Here
    frame = xr.open_dataset(file_path,decode_coords=True)
    frame.rio.write_crs("epsg:4326", inplace=True)
    frame.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
    frame.rio.write_coordinate_system(inplace=True)
    frame = cut_data(frame,border)
    frame.to_netcdf(os.path.join(output_path,"PRECIP",os.path.basename(file_path)))

def cut_popular_and_save(file_path):
    print(file_path)
    border = border_frame
    frame = xr.open_dataset(file_path).squeeze("band",drop=True)
    frame = cut_data(frame,border)
    frame.to_netcdf(os.path.join(output_path,"POPULAR",os.path.basename(file_path)[:-4]+".nc"))

def cut_gdp_and_save(file_path):
    print(file_path)
    border = border_frame
    frame = xr.open_dataset(file_path).squeeze("band",drop=True)
    frame = frame.rio.reproject("epsg:4326")
    frame = cut_data(frame,border)
    frame.to_netcdf(os.path.join(output_path,"GDP",os.path.basename(file_path)[:-4]+".nc"))

def cut_clcd_and_save(file_path):
    print(file_path)
    border = border_frame
    frame = rxr.open_rasterio(file_path,masked=True)
    frame = frame.rio.clip(border.geometry, frame.rio.crs,from_disk=True).squeeze("band",drop=True)
    frame.to_netcdf(os.path.join(output_path,"CLCD",os.path.basename(file_path)[:-4]+".nc"))

def cut_data(frame:xr.Dataset, border: gpd.GeoDataFrame):
    return frame.rio.clip(border.geometry, frame.rio.crs)

border_frame = gpd.read_file('scripts/preProcessing/border.json')
path_prefix = os.path.join("scripts","datas")
path_postfix = os.path.join("extracted")
data_types = ["PRECIP","POPULAR","GDP","CLCD"]

output_path = os.path.join("scripts","outputs")

file_names = dict([])
for data_type in data_types:
    file_namepath = []
    file_path =os.path.join(path_prefix,data_type,path_postfix)
    for filename in os.listdir(file_path):
        file_namepath.append(os.path.join(file_path,filename))
    file_names[data_type] = file_namepath


gdp_path = [os.path.join("scripts/datas/GDP/extracted/GDPGrid_China2005/cngdp2005.tif"),os.path.join("scripts/datas/GDP/extracted/GDPGrid_China2010/cngdp2010.tif")]

if __name__ == "__main__":
    pool = mp.Pool(2)
    #pool.map(cut_precip_and_save,file_names["PRECIP"])
    #pool.map(cut_popular_and_save,file_names["POPULAR"])
    #pool.map(cut_gdp_and_save,gdp_path)
    pool.map(cut_clcd_and_save,file_names["CLCD"])

    pool.close()
    pool.join()