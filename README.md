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
        
## Docker Image setup
- `docker pull continuumio/anaconda` - pull the newest image into cwd (for me its `/Docker`)
- `docker run -i -t continuumio/anaconda /bin/bash`- run the container, call bin bsh
- `conda install -c conda-forge python-eccodes` - setup eccodes
- `conda install -c conda-forge ecmwf-api-client` - setup the api client
    - Set your ecwmf credentials in `root/.ecmwfapirc`
        - e.g. `<editor> /root/.ecmwfapirc` - you might have to install any editor first by using apt-get, then copy paste your credentials in the form of:
        ```
        {
            "url"   : "https://api.ecmwf.int/v1",
            "key"   : "supersecretkey",
            "email" : "your-email@email.com"
        }
        ```

## Usage
1. Retrieve a file for the latest possible date from the CAMS data set. Per default this lib is setup that the retrieved data is only for europe. You can disable this by passing the named parameter `filterEurope=False`
    ```python
    r = retrieve.Retrieve()
    latestRetrievalDate = datetime.today() - timedelta(days=copernicus_enums.DataSets.CAMS.value['delayDays'])
    dateString = latestRetrievalDate.strftime(retrieve.Retrieve.DATEFORMAT)
    fileName=r.retrieve_file("data/ecmwf/an-" + dateString, date=latestRetrievalDate, dataType=copernicus_enums.DataType.ANALYSIS)
    print fileName # prints the filename - e.g. "data/ecmwf/an-2017-09-13.grib"
    ```
2. Parse the file and find data for a specific date, latitude and longitude. If you do not want to specify the `Time` enum manually you can use the `Time.convertTimeStampToTimes(ISOTimeString)`
    ```python
    point = [48.4391, 9.9823]  
    times=copernicus_enums.Time.all()
    
    parser = parser.Parser()
    # specify your params in an array as named parameter as well as the times
    result = parser.get_nearest_values(fileName, point, times=times, parameters=copernicus_enums.ParameterCAMS.all()) 
    # Output the data as json.
    print(json.dumps(result, default=copernicus_data.CopernicusData.json_serial, indent=2)) 
    ```

## Tasks
- Optimize for less strain on the ECWMF Servers
- Retrieve has to be in a separate thread - retrieval can take a long time
- add all the non grib ".128" parameters
- Add option to retrieve values for all the indexes in the grib file?
- When finishing ERA5 receive - credit the data source
    - Receives and returns data by using and modifying Copernicus Climate Change Service Information 2017 -  ongoing

## Finished
- Get data nearest to a specific point
- Retrieve should always retrieve all vals, it doesn't help if you want to optimize if you need to wait 1h+ for data
- Customizable retrieval
- Implemented classification - see the `copernicus_enums.py` file for more informations
