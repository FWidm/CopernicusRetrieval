# Copernicus Data "Crawler"

Retrieves data from the copernicus servers

## Acknowledgements
- Receives and returns data by using and modifying Copernicus Atmosphere Monitoring Service Information 2017 -  ongoing

## Requirements
- Python 2.7
- Installed ECWMFAPI and ECCodes
    - can be done by using conda with the following packages: 
        - eccodes: https://anaconda.org/conda-forge/python-eccodes
        - ecmwf-api: `source activate <env name>` 
        followed by `pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz`
   
   - calling the api from another scripting language can be done
        - refer to [Info.md](/doc/info.md)
        
## Tasks
- Customizable retrieval
- Optimize for less strain on the ECWMF Servers
- Retrieve has to be in a separate thread - retrieval can take a long time
- add all the non grib ".128" parameters
- Add option to retrieve values for all the indexes in the grib file?
- When finishing ERA5 receive - credit the data source
    - Receives and returns data by using and modifying Copernicus Climate Change Service Information 2017 -  ongoing

## Finished
- Get data nearest to a specific point
- Retrieve should always retrieve all vals, it doesn't help if you want to optimize if you need to wait 1h+ for data
