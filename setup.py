from distutils.core import setup

setup(
    name='Copernicus Retrieval',
    version='0.0.3',
    packages=['copernicus_retrieval', 'copernicus_retrieval.data', 'copernicus_retrieval.util'],
    # packages=find_packages(),
    description='Wrapper for retrieving data from copernicus services for a specific location',
    author='Fabian Widmann',
    author_email='fabian.widmann@gmail.com',
    url='https://github.com/FWidm/CopernicusRetrieval',
    keywords=['weather', 'weather-data', 'ecmwf', 'copernicus', 'retrieval', 'wrapper'],
    classifiers=['Operating System :: MacOS',
                 'Operating System :: Unix',
                 'Programming Language :: Python :: 2.7',
                 ],
    dependency_links=[
        "https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz"
    ],
)
