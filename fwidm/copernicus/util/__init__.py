# -*- coding: UTF-8 -*-
from pprint import pprint
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json


# Code from: http://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/
class HTMLTableParser:
    def parse_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return self.parse_html_table(soup.find('table'))

    def parse_html_table(self, table):
        n_columns = 0
        n_rows = 0
        column_names = []

        # Find number of rows and columns
        # we also find the column titles if we can
        for row in table.find_all('tr'):

            # Determine the number of rows in the table
            td_tags = row.find_all('td')
            # print "td_tags={}, len={}".format(td_tags,len(td_tags))
            if len(td_tags) > 0:
                n_rows += 1
                if n_columns == 0:
                    # Set the number of columns for our table
                    n_columns = len(td_tags)
                    # print "n_columns={}, len={}".format(n_columns, len(td_tags))

            # Handle column names if we find them
            th_tags = row.find_all('th')
            if len(th_tags) > 0 and len(column_names) == 0:
                for th in th_tags:
                    column_names.append(th.get_text())

        # Safeguard on Column Titles
        if len(column_names) > 0 and len(column_names) != n_columns:
            raise Exception("Column titles do not match the number of columns")

        columns = column_names if len(column_names) > 0 else range(0, n_columns)
        df = pd.DataFrame(columns=['code figure', 'abbrev.', 'field param.', 'unit'],
                          index=range(0, n_rows))
        row_marker = 0
        for row in table.find_all('tr'):
            # row_content=[]
            # print ">> row={}".format(row)
            column_marker = 0
            columns = row.find_all('td')
            for column in columns:
                # print ">>>> col={}".format(column.get_text())
                df.iat[row_marker, column_marker] = column.get_text()
                # row_content.append(column.get_text())
                column_marker += 1
            if len(columns) > 0:
                row_marker += 1
                # print(row_content)

        new_header = df.iloc[0]  # grab the first row for the header
        df = df[1:]  # take the data less the header row
        df.rename(columns=new_header)  # set the header row as the df header

        return df


def retrieve_parameters():
    hp = HTMLTableParser()
    table = hp.parse_url(
        'https://rda.ucar.edu/cgi-bin/transform?xml=/metadata/ParameterTables/WMO_GRIB1.98-0.128.xml&view=gribdoc')

    params = []
    for index, row in table.iterrows():
        if ('Reserved' not in row[2]):
            param = {
                'eraId': str(int(row[0])) + ".128",  # change this to the correct grib version!!
                'id': int(row[0]),
                'shortName': row[1].encode('utf8'),
                'description': row[2].encode('utf8'),
                'unit': row[3].replace('-', '^-').encode('utf8')
            }
            sname = row[2].encode('utf8')

            # replace all kind of unwanted chars in a python library.
            for ch in ['/', ' + ', ' ', '#', '&', '-', ',', '+', ]:
                if ch in sname:
                    sname = sname.replace(ch, "_")

            # replace brackets
            for ch in ['(', ')']:
                if ch in sname:
                    sname = sname.replace(ch, "")

            # replace the numbers 2 and 10 with the text representation
            if '10' in sname:
                sname = sname.replace('10', 'TEN')

            if '2' in sname:
                sname = sname.replace('2', 'TWO')

            # stringify the paramters to python's default dict representation "x = {'key':<val>}"
            if int(row[0]) in [34, 129, 137, 151, 164, 165, 166, 167, 168, 172, 174, 186, 187, 188]:
                params.append(sname.upper() + '=' + str(param))

        # >> > for val in valid_params.split("/"): --> see Parameters.Parameter comment for more info
        #     ... split = val.split(".")
        #     ... if "128" in split[1]:
        #     ...   x.append(int(split[0]))
        # [34, 129, 137, 151, 164, 165, 166, 167, 168, 172, 174, 186, 187, 188]

    # Save parsed parameters to the temp text file - copy contents to /fwidm/copernicus/data/Parameters.py
    with open('../../../parameters.txt', 'wb') as f:
        for entry in params:
            f.write(str(entry) + os.linesep)


retrieve_parameters()
# parse_parameters("../../../parameters.json")
