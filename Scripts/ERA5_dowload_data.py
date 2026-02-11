import cdsapi
import xarray as xr
import os.path

dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "2m_temperature",
        "sea_surface_temperature",
        "surface_pressure",
        "boundary_layer_height",
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "100m_u_component_of_wind",
        "100m_v_component_of_wind"
    ],
    "year": ["1996"],
    "month": ["04"],
    "day": ["07"],
    "time": [
        "00:00", "01:00", "02:00",
        "03:00", "04:00", "05:00",
        "06:00", "07:00", "08:00",
        "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00",
        "21:00", "22:00", "23:00"
    ],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [20, -100, 15, -95]
}

client = cdsapi.Client()

test_file = 'test_ERA5.nc'

if not os.path.isfile(test_file):
    client.retrieve(dataset, request, test_file).download()
else:
    print(f"{test_file} already exists, skipping download.")
    netcdf_ds = xr.open_dataset(test_file)


#%% Running a quick xarray check.
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr

airtemps = xr.tutorial.open_dataset("air_temperature")
airtemps

# Convert to celsius
air = airtemps.air - 273.15

# copy attributes to get nice figure labels and change Kelvin to Celsius
air.attrs = airtemps.air.attrs
air.attrs["units"] = "deg C"

air1d = air.isel(lat=10, lon=10)
air1d.plot();
