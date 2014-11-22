#Code that generates URL for Factfinder census data and pastes it to clipboard

#This code pastes a string to your clipboard, regardless of OS.
#Codes straight outta StackOverflow:

#Windows way:
output = 'TEST AAAHHH'
from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(output)
r.destroy()

import subprocess
process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
process.communicate(output.encode('utf-8'))
