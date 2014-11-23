# -*- coding: utf-8 -*-
#Code that generates URL for Factfinder census data and pastes it to clipboard

#Get modules
from Tkinter import Tk
from sys import exit

print 'Welcome to the One and Only Veen Census Zipcode Data Finder! \n'
#Get the topic
topic = raw_input('\n Do you want data about population totals or a breakdown of\
 age and sex? \nType 1 for population totals or 2 for sex & age,\
 and press Enter. \n')

#URL-BUILDER PART ONE COMMENCE:
standardURL = 'http://factfinder2.census.gov/bkmk/table/1.0/en/DEC/10_SF1/'

if topic == '1':
    topic = 'P1'
    standardURL = standardURL + topic +  '/'
    
elif topic == '2':
    topic = 'P12'
    
    #Get race
    race = raw_input('\n Do you want to limit the data to a specific race? \n \
    Press the corresponding letter, or nothing, and then press Enter. \n \
    A: White alone \n \
    B: Black or African American alone   \n \
    C: American Indian and Alaska Native alone \n \
    D: Asian alone  \n \
    E: Native Hawaiian and Other Pacific Islander alone  \n \
    F: Some Other Race alone \n \
    G: Two or More Races \n \
    H: Hispanic or Latino \n \
    I: White alone, not Hispanic or Latino  \n')

    standardURL = standardURL + topic + race.upper() + '/'

else:
    exit('Error: invalid input')



decision = raw_input('\n What area do you want the zip codes from? \n \
For a state, press 1 and Enter. For a county, press 2 and Enter. \n ')

statecode = raw_input('Please type in the state code: \n \
01 Alabama  17 Illinois     30 Montana      44 Rhode Island \n \
02 Alaska   18 Indiana      31 Nebraska     45 South Carolina \n \
04 Arizona  19 Iowa         32 Nevada       46 South Dakota \n \
05 Arkansas 20 Kansas       33 New Hampsh.  47 Tennessee \n \
06 Califor. 21 Kentucky     34 New Jersey   48 Texas \n \
08 Colorado 22 Louisiana    35 New Mexico   49 Utah \n \
09 Connet.  23 Maine        36 New York     50 Vermont \n \
10 Delaware 24 Maryland     37 North Carol. 51 Virginia \n \
11 DiColumb 25 Massachus.   38 North Dakota 53 Washington \n \
12 Florida  26 Michigan     39 Ohio         54 West Virginia \n \
13 Georgia  27 Minnesota    40 Oklahoma     55 Wisconsin \n \
15 Hawaii   28 Mississippi  41 Oregon       56 Wyoming \n \
16 Idaho    29 Missouri     42 Pennsylvania 72 Puerto Rico \n ')

#Check if input is long enough, otherwise add a zero
statecode = str(statecode)
if len(statecode) == 1:
    statecode = '0' + statecode

if decision =='1':
    standardURL = standardURL + '0400000US' + str(statecode) + '.86000P'
    
elif decision == '2':
    fips = raw_input('\n Type in the 3-digit county FIPS code. Examples: \n \
    ISLAND  = 029 \n \
    KING    = 033\n \
    KITSAP  = 035\n \
    SKAGIT  = 051\n \
    PIERCE  = 053\n \
    SNOHO   = 061\n \
    WHATCOM = 073\n \
    L.A     = 037\n \
    RIVERS  = 065\n \
    SANBER  = 071\n \
    VENTURA = 111\n')

    fips = str(fips)
    #Adding zeroes to fips for if people enter it without it
    if len(fips) == 1:
        fips = '00' + str(fips)
    elif len(fips) == 2:
        fips = '0' + str(fips)
    
    standardURL = standardURL + '0400000US06.86000P|0500000US' \
                  + statecode + fips

print '\n The URL \n', standardURL, '\n has been pasted to your clipboard.'
print '\n PLEASE NOTE: If you want to join this data with something like ArcGIS,'
print 'it is advised to flip the table on the Factfinder site so that the zip'
print 'codes are the rows and not the columns.'
print '\n veen out'

#This code pastes a string to your clipboard, regardless of OS.
#Code straight outta StackOverflow.

#Example census data from all zipcodes (860) in state (040) California (06)
'http://factfinder2.census.gov/bkmk/table/1.0/en/DEC/10_SF1/P12A/0400000US06.86000P'

#Example of the same, clipped to LA:
'http://factfinder2.census.gov/bkmk/table/1.0/en/DEC/10_SF1/P12A/0400000US06.86000P|0500000US06037'

#Windows way:
output = standardURL
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(output)
r.destroy()

#Mac way
import subprocess
process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
process.communicate(output.encode('utf-8'))
