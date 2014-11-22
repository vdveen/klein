#Code that generates URL for Factfinder census data and pastes it to clipboard

#URL-BUILDER COMMENCE:
standardURL = 'http://factfinder2.census.gov/bkmk/table/1.0/en/DEC/10_SF1/'

#Get the data level
state = '040'
county = '050'
censustr = '140'
zipcode = '860'

level = state

geoid = level + '0000US' + fips

#This code pastes a string to your clipboard, regardless of OS.
#Code straight outta StackOverflow.

#Windows way:
output = 'TEST AAAHHH'
from Tkinter import Tk
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
