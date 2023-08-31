import xarray as xr
import rasterio as rio
import os

dem_frame = xr.open_dataset(os.path.join("scripts/datas/DEM-90/extracted/DEM_SRTM.tif")).squeeze("band",drop=True)

dem_frame_resampled = dem_frame.rio.reproject(dem_frame.rio.crs,shape=(1800,1560),resampling=rio.enums.Resampling.bilinear)

dem_frame_resampled.to_netcdf(os.path.join("scripts/outputs/DEM-90/DEM_SRTM.nc"))