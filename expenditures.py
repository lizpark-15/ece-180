#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:53:58 2017

@author: elizabethpark
"""

import pandas as pd

data=pd.read_csv('/Users/elizabethpark/Desktop/ECE 180/world-university-rankings/education_expenditure_supplementary_data2.csv')
#had to use data2 because saved excel in MS-DOS csv format to get rid of error messages.
#NaN means blank/no data.
grp = data.groupby('1995')
x = list(data) #contains list of header columns

'''
List of header titles
['country', 'institute_type', 'direct_expenditure_type', '1995', '2000', '2005',
 '2009', '2010', '2011']

'''

#grouping by public expenditures
grp_det = data.groupby('direct_expenditure_type')
public = grp_det.get_group('Public')
#111 rows

#private expenditures
private = grp_det.get_group('Private')
private.country #lists all countries
#111 rows

#total expenditure
total_expenditure = grp_det.get_group('Total')
#111 rows

#group by each country and expenditure type
h = data.groupby('country').country.count() #how many times a country pops up
j = data.groupby('country').count()
len(h) #equals 37

country = data.sort_values(by=['country', 'direct_expenditure_type']) #sort by country and expenditure type
''' 
    Each country appears at least 9 times.
    There are 36 countries represented in this data. OECD is repreented as its
    own 'country'. There are also 9 rows of information about the OECD Average'.
    
    Each country has 3 direct expenditure types: public, private, and total.
    There are 3 institution types: all, elementary & secondary, and higher edu.
    So there are values for each expenditure type and institution type. 3x3 = 9.
    
    Next: need to group separately by public/private/total elementary&secondary 
    expenditure, public/private/total higher education expenditure.. find 
    average/max/min and see if that correlates with university rankings.
    '''

#public_d.columns.str.match('^Higher Education Institutions')
#public_d.columns[public_d.columns.str.match('Higher Education Institutions')]
