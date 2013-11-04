#===============================================================================
# OMDb API Search Script - Module - menus
#-------------------------------------------------------------------------------
# Version: 0.1.3
# Updated: 03-11-2013
# Author: Alex C.
# License: MIT
#-------------------------------------------------------------------------------
# Notes
#===============================================================================

"""
Contains functions for the OMDb API Search Script menus.

"""

#===============================================================================
# IMPORTS
#===============================================================================

from const import *
import dispdat
import getdat
import srchdat

# if OSNAME in ["nt", "dos"]:
#     import msvcrt

#===============================================================================
# MISC. VARIABLES
#===============================================================================

currloc = None
lastloc = None

loaded = None

#===============================================================================
# MAIN MENU
#===============================================================================

def main ():
    """"""

    global currloc
    global lastloc

    lastloc = currloc
    currloc = main

    index = 1

    killscript = False

    dispdat.osclear()

    dispdat.title("Main Menu")

    dispdat.numlist(MAINOPT)

    if loaded is not None:
        print "{0} {1}{2}".format("File:", loaded, NL)

    print HR

    cmd = getdat.getinput()

    if cmd == "1":
        killscript = loadformat()
    elif cmd == "2":
        killscript = filesrch()
    elif cmd == "3":
        killscript = omdbsrch()
    elif cmd == "4":
        killscript = False

    if killscript:
        return True
    elif not killscript:
        return False

#===============================================================================
# FILE MENU
#===============================================================================

def filesrch():
    """"""

    global currloc
    global lastloc

    lastloc = currloc
    currloc = filesrch

    index = 1

    searchagain = False

    dispdat.osclear()

    dispdat.title("Search Cache")

    dispdat.numlist(SRCHOPT)

    print HR

    cmd = getdat.getinput()

    if cmd == "1":
        searchagain = srchdat.fortitle()
    elif cmd == "2":
        searchagain = srchdat.forid()

    if searchagain:
        return True
    elif not searchagain:
        return False


def loadformat():
    """"""

    global currloc
    global lastloc
    global loaded

    loaded = None

    lastloc = currloc
    currloc = loadformat

    format = None

    dispdat.osclear()

    dispdat.title("Format Selection")

    dispdat.numlist(FORMATS, True)

    print HR

    cmd = getdat.getinput()

    if cmd == "1":
        format = FORMATS[0]
    elif cmd == "2":
        format = FORMATS[1]

    dispdat.osclear()

    filelist = getdat.localfiles(format)

    dispdat.title("Local Files")

    dispdat.numlist(filelist)

    loaded = getdat.fromfile(filelist, True)

    return True

#===============================================================================
# OMDB SEARCH MENU
#===============================================================================

def omdbsrch():
    """"""

    global currloc
    global lastloc

    lastloc = currloc
    currloc = omdbsrch

    index = 1

    searchagain = False

    dispdat.osclear()

    dispdat.title("Search OMDb API")

    dispdat.numlist(SRCHOPT)

    print HR

    cmd = getdat.getinput()

    if cmd == "1":
        searchagain = srchdat.fortitle(True)
    elif cmd == "2":
        searchagain = srchdat.forid(True)

    if searchagain:
        return True
    elif not searchagain:
        return False
