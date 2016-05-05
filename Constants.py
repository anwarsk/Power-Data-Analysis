'''
Created on Mar 16, 2016

This module all the constants and types required in the program.

@author: anwar
'''

D_FILE_NAME = "d.csv"
E_FILE_NAME = "E.csv"
CF_FILE_NAME = "CF.csv"
VECTORS_FILE_NAME = "Vectors.csv"
SCALARS_FILE_NAME = "Scalars.csv"


technology = [
'oil',
'coal',
'ng',
'coal_ccs',
'ng_ccs',
'nuclear',
'hydro',
'geo',
'ocean',
'biomass',
'wind_off',
'wind_on',
'solar_csp',
'solar_pv'
]

timeVsTechnologyHeader = ['Time'] + technology
summaryHeader = ['PortfolioIndex','PortfolioName','SystemCost(W)']