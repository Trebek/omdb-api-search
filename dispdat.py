#===============================================================================
# OMDb API Search Script - Module - dispdat
#-------------------------------------------------------------------------------
# Version: 0.1.3
# Updated: 03-11-2013
# Author: Alex C.
# License: MIT
#-------------------------------------------------------------------------------
# Notes
#===============================================================================

"""
Contains functions for displaying movie data, either from a JSON file, 
or from the OMDb API.

"""

#===============================================================================
# IMPORTS
#===============================================================================

import os
import re

from const import *

#===============================================================================
# PADDING VARIABLES
#===============================================================================

infopad = 0
imdbpad = 0
rtpad = 0

#===============================================================================
# DISPLAY MOVIE INFORMATION
#===============================================================================

def movdata(mov):
    """"""
    
    osclear()

    brokenplot = linebreak(mov[MKEY[13]])
    brokenstars = linebreak(mov[MKEY[7]], False)

    title(mov[MKEY[3]], mov[MKEY[4]])

    print brokenplot

    title("Movie Info")

    print INFOLBL[0]
    print mov[MKEY[5]] + NL
    
    print INFOLBL[1]
    print mov[MKEY[6]] + NL

    print INFOLBL[2]
    print brokenstars + NL

    print INFOLBL[3]
    print mov[MKEY[8]] + NL

    print INFOLBL[4]
    print mov[MKEY[9]] + NL

    print INFOLBL[5]
    print mov[MKEY[10]] + NL

    print INFOLBL[6]
    print mov[MKEY[11]] + NL

    print INFOLBL[7]
    print mov[MKEY[12]] + NL
    
    title("IMDb Rating")

    print IMDBLBL[0]
    print mov[MKEY[14]] + "/10" + NL

    print IMDBLBL[1]
    print mov[MKEY[15]] + NL
    
    title("Rotten Tomatoes Rating")

    print RTLBL[0]
    if mov[MKEY[16]] == "certified":
        print "Certified Fresh" + NL
    else:
        print mov[MKEY[16]].capitalize() + NL

    print RTLBL[1]
    print mov[MKEY[17]] + "%" + NL

    print RTLBL[2]
    print mov[MKEY[18]] + "/10" + NL

    print RTLBL[3]
    print mov[MKEY[19]] + NL

    print RTLBL[4]
    print mov[MKEY[20]] + "%" + NL

    print RTLBL[2]
    print mov[MKEY[21]] + "/5" + NL

    print RTLBL[5]
    print mov[MKEY[22]] + NL

    print HR + NL

#===============================================================================
# GENERAL FORMATTING FUNCTIONS
#===============================================================================

#-------------------------------------------------------------------------------
# OS Depndant Clear Screen
#-------------------------------------------------------------------------------

def osclear ():
    """"""

    if OSNAME in ["nt", "dos"]:
        os.system('cls')
    elif OSNAME is "posix":
        os.system('clear')

#-------------------------------------------------------------------------------
# Title Printer
#-------------------------------------------------------------------------------

def title (*args):
    """"""
    
    argl = len(args)

    print HR
    if argl == 1:
        print args[0]
    elif argl == 2:
        print args[0] + " (" + args[1] + ")"
    else:
        pass
    print HR + NL

#-------------------------------------------------------------------------------
# Section Title Printer
#-------------------------------------------------------------------------------

def sect (title):
    """"""
    
    print HR3 + " " + title + " " + HR3 + NL

#-------------------------------------------------------------------------------
# Numbered List Printer
#-------------------------------------------------------------------------------

def numlist (thelist, upper=False):
    """"""

    index = 1

    if not upper:
      for item in thelist:
          print "[{0}] {1}".format(index, item)
          index += 1
    elif upper:
      for item in thelist:
          print "[{0}] {1}".format(index, item.upper())
          index += 1
    print

#-------------------------------------------------------------------------------
# Runtime Converter
#-------------------------------------------------------------------------------

def convtime (time):
    """"""
            
    spltime = time.split(" ")
    
    mintime = None
    
    if len(spltime) == 4:
        spltime[0] = int(spltime[0])
        spltime[2] = int(spltime[2])
        mintime = str((60 * spltime[0]) + spltime[2]) + " min"
    
    return mintime

#-------------------------------------------------------------------------------
# Padding Setter
#-------------------------------------------------------------------------------

def padset (INFOLBL, IMDBLBL, RTLBL):
    """"""

    global infopad, imdbpad, rtpad

    temppad = 0

    for x in INFOLBL:
        if len(x) > infopad:
            infopad = len(x) + 1
    
    for x in IMDBLBL:
        if len(x) > imdbpad:
            imdbpad = len(x) + 1
    
    for x in RTLBL:
        if len(x) > rtpad:
            rtpad = len(x) + 1

#-------------------------------------------------------------------------------
# Line Breaker
#-------------------------------------------------------------------------------

def linebreak (plot, nl=True):
    """"""

    if nl:
      compiled = re.compile("(.{,79})($|\s)")
      subbed = compiled.sub("\\1\n", plot)
    elif not nl:
      compiled = re.compile("(.{,79})($|\s)")
      subbed = compiled.sub("\\1", plot)

    return subbed

#===============================================================================
# PADDING SETUP CALL
#===============================================================================

padset(INFOLBL, IMDBLBL, RTLBL)
