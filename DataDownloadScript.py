#Code that generates URL for Factfinder census data and pastes it to clipboard

#Get modules
from Tkinter import Tk
from sys import exit

#Get the topic
topic = input('Do you want data about population totals or a breakdown of\
 age and sex? Type P for population or S for sex & age, and press Enter.')
if topic == 'P':
    topic = 'P1'
if topic == 'S':
    topic = 'P12'
if topic == '':
    exit('Error: invalid input')
#Get race
race = input('Do you want to limit the data to a specific race? \
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

#URL-BUILDER COMMENCE:
standardURL = 'http://factfinder2.census.gov/bkmk/table/1.0/en/DEC/10_SF1/'
standardURL = standardURL + topic + race

print race
exit('done')

#Get the data level
nation = '010'
state = '040'
county = '050'
censustr = '140'
zipcode = '860'

level = state

statecode = input('Please type in the state code: \n \
01 Alabama  17 Illinois     30 Montana      44 Rhode Island \n \
02 Alaska   18 Indiana      31 Nebraska     45 South Carolina \n \
04 Arizona  19 Iowa         32 Nevada       46 South Dakota \n \
05 Arkansas 20 Kansas       33 New Hampsh.  47 Tennessee \n \
06 Califor. 21 Kentucky     34 New Jersey   48 Texas \n \
08 Colorado 22 Louisiana    35 New Mexico   49 Utah \n \
09 Conne.   23 Maine        36 New York     50 Vermont \n \
10 Delaware 24 Maryland     37 North Carol. 51 Virginia \n \
11 DiColumb 25 Massachus.   38 North Dakota 53 Washington \n \
12 Florida  26 Michigan     39 Ohio         54 West Virginia \n \
13 Georgia  27 Minnesota    40 Oklahoma     55 Wisconsin \n \
15 Hawaii   28 Mississippi  41 Oregon       56 Wyoming \n \
16 Idaho    29 Missouri     42 Pennsylvania 72 Puerto Rico \n ')

exit('Your code is' + str(statecode))
#Get the state code
fips = '06'

geoid = level + '0000US' + fips

#Get the FIPS of the county to clip to.
#Codes from http://www.epa.gov/enviro/html/codes/
ISLAND = '53029'
KING = '53033'
KITSAP = '53035'
SKAGIT = '53051'
PIERCE = '53053'
SNOHO = '53061'
WHATCOM = '53073'

LA = '06037'
RIVERS = '060065'
SANBER = '06071'
VENTURA = '060111'

clipCounty = '0500000US' + countylevel

#This code pastes a string to your clipboard, regardless of OS.
#Code straight outta StackOverflow.

#Example census data from all zipcodes (860) in state (040) California (06)
'http://factfinder2.census.gov/bkmk/table/1.0/en/DEC/10_SF1/P12A/0400000US06.86000P'

#Example of the same, clipped to LA:
'http://factfinder2.census.gov/bkmk/table/1.0/en/DEC/10_SF1/P12A/0400000US06.86000P|0500000US06037'

#Windows way:
output = 'TEST AAAHHH'
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
