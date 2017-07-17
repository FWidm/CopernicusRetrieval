# Copernicus Data "Crawler"

Retrieves data from the copernicus servers

## Requirements
- Installed ECWMFAPI and ECCodes
    - can be done by using conda with the following packages: 
        - eccodes: https://anaconda.org/conda-forge/python-eccodes
        - ecmwf-api: `source activate <env name>` 
        followed by `pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz`
   
   - calling the api from another scripting language can be done by executing (and adapting!)the pywrapper shell script.
        
## Tasks
- Customizable retrieval
- Get data nearest to a specific point
- Check if the file for the specific day with specified vars exist
- Optimize for less strain on the ECWMF Servers
- Retrieve has to be in a separate thread - retrieval can take a long time

## Finished
