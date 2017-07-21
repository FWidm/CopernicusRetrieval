# Copernicus Library notes
## Functionality
1. `copernicus.Retrieve` contains the Retrieve class that allows you to retrieve data from the ECMWF Data set by specifying times and parameters - currently only for the analysis part. The method `retrieve_file` 
2. `copernicus.Parser` in turn can get you the nearest data for a Location (lat,lng), specific times and parameters.
    - It also offers methods to retrieve all parameter's meta data in a specific format so that you can extend the `copernicus.data.Parameters`.
    
## Using Python from PHP when following the setup with conda
Call [`exec($cmd,$out)`](http://php.net/manual/de/function.exec.php) to run the script, `$cmd`should contain the command to activate the correct conda environment and in turn call the script
```php
<?php
php > exec("source activate copernicus && python copernicuslib.py ".escapeshellarg($a)." ".escapeshellarg($b),$output);
php > var_dump($output);
array(4) {
  [0]=>
  string(40) "{"a": [1, 2, 3], "b": {"a": ["b", "c"]}}"
  [1]=>
  string(33) "Number of arguments: 3 arguments."
  [2]=>
  string(65) "Argument List: ['copernicuslib.py', '[1,2,3]', '{"a":["b","c"]}']"
  [3]=>
  string(40) "{"a": [1, 2, 3], "b": {"a": ["b", "c"]}}"
}
```

Testing script: accepts two or more params, lists them in the console and then prints a dict containing the value.
```python
import sys
import json

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

def parseJson(json_data):
    data = json.loads(json_data)
    return data

if __name__ == '__main__':
    a = parseJson(sys.argv[1])
    b = parseJson(sys.argv[2])
    ret= {'a':a, 'b':b}
    print(json.dumps(ret))

```

To test the testing script call:
```bash
$ source activate copernicus && python copernicuslib.py "2017-07-08.grib" "[48.4391, 9.9823]"
```

Output can in turn be parsed with PHP:
```php
<?php
exec("source activate copernicus && python copernicuslib.py ".escapeshellarg("2017-07-08.grib")." ".escapeshellarg("[48.4391, 9.9823]"),$output);"
$out=json_decode($output[count($output)-1]) // parse the last value that was printed
print_r($out->TEN_METRE_V_WIND_COMPONENT); // or all other keys as seen in Parameters.Parameter
```

