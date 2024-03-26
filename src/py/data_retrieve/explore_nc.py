import netCDF4 as nc
#import xarray as xr
import pandas as pd

testfile = "./data/nc_data/13857_Rtraj.nc"

def exploreNC(file: str) -> dict:

    nc_dict = {}
    # Open the NetCDF file
    with nc.Dataset(file, 'r') as file:
        
        print(type(file.variables.values()))
        for i in file.variables.values():
            print("------", i)
            print(type(i))
            for attr_name in i.ncattrs():
                print(f"----- ------- {attr_name}: {getattr(i, attr_name)}")
        # Explore NetCDF file attributes
        try:
            if file.attributes:
                nc_dict['attributes'] = {
                    "number" : len(file.attributes.keys()),
                    "names" : list(file.attributes.keys())
                }
        except:
            pass

        # Explore NetCDF file variables
        try: 
            if file.variables:
                nc_dict['variables'] = {
                    "number" : len(file.variables.keys()),
                    "names" : list(file.variables.keys())
                }
        except:
            pass
        # Explore NetCDF file dimensions
        try:
            if file.dimensions:
                nc_dict['dimensions'] = {
                    "number" : len(file.dimensions.keys()),
                    "names" : list(file.dimensions.keys()),
                    "sizes" : [v.size for v in file.dimensions.values()]
                }
        except:
            pass

        return nc_dict

result = exploreNC(testfile)
