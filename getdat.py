#===============================================================================
# OMDb API Search Script - Module - getdat
#-------------------------------------------------------------------------------
# Version: 0.1.3
# Updated: 03-11-2013
# Author: Alex C.
# License: MIT
#-------------------------------------------------------------------------------
# Notes
#===============================================================================

"""
Contains functions for retrieving movie data, either from a JSON file, 
or from the OMDb API.

"""

#===============================================================================
# IMPORTS
#===============================================================================

import glob
import json
import msvcrt
import urllib2

from const import *
import dispdat

#===============================================================================
# LOCAL CACHE FOR STORING PAST SEARCHES
#===============================================================================

cache = []

#===============================================================================
# GET USER INPUT
#===============================================================================

def getinput (msg=""):
    """"""

    # if OSNAME in ["nt", "dos"]:
    #     if msg is not "":
    #         print msg
    #     cmd = msvcrt.getch()
    # elif OSNAME is "posix":
    #     cmd = raw_input(msg)

    cmd = raw_input(msg)

    return cmd

#===============================================================================
# GET DATA FROM JSON FILE
#===============================================================================

def fromfile (filelist, ret=False):
    """"""

    global cache
    
    dupe = False
    thefile = None
    choice = None

    loaded = None

    print HR

    userinput = getinput("File: ")

    try:
        choice = (int(userinput) - 1)
    except:
        choice = userinput

    try:
        if choice is not "":
            if type(choice) is int:
                thefile = open(filelist[choice], 'r')
                loaded = filelist[choice]
            elif type(choice) is str:
                thefile = open(choice, 'r')
                loaded = choice
    except (IOError, IndexError):
        print "Can't find that file." + NL
        return fromfile()
    
    if thefile is not None:
        movdata = json.load(thefile)
    
        for mov in movdata:
            for mov2 in cache:
                if mov[MKEY[1]] == mov2[MKEY[1]]:
                    dupe = True
            if not dupe:
                cache.append(mov)

        print "File loaded."

    if thefile is not None:
        thefile.close()

    if ret:
        return loaded


def localfiles (format="json"):
    """"""

    filelist = glob.glob("*." + format)

    return filelist

#===============================================================================
# GET DATA FROM OMDB API - IMDB ID
#===============================================================================

def withid (theid):
    """"""
    
    global cache

    dupe = False
    
    theurl = "{0}{1}{2}{3}{4}".format(OMDBURL, Q[1], theid, PLOT[1], QOP[3])
    
    response = urllib2.urlopen(theurl)
    
    movdata = json.load(response)
    
    for mov in cache:
        if movdata[MKEY[1]] == mov[MKEY[1]]:
            dupe = True
    if not dupe:
        cache.append(movdata)

#===============================================================================
# GET DATA FROM OMDB API - TITLE
#===============================================================================

def withtitle (thetitle, year=None):
    """"""
    
    dupe = False

    response = None
    
    newtitle = enctitle(thetitle)
   
    theurl = "{0}{1}{2}{3}{4}".format(OMDBURL, Q[2], newtitle, PLOT[1], QOP[3])
    theurl2 = "{0}{1}{2}{3}{4}{5}{6}".format(OMDBURL, Q[2], newtitle, QOP[0], 
                                             year, PLOT[1], QOP[3])
    
    if year == None:
        theurl = "{0}{1}{2}{3}{4}".format(OMDBURL, Q[2], newtitle, PLOT[1], 
                                          QOP[3])
        response = urllib2.urlopen(theurl) 
    elif year != None:
        theurl2 = "{0}{1}{2}{3}{4}{5}{6}".format(OMDBURL, Q[2], newtitle, QOP[0], 
                                                 year, PLOT[1], QOP[3])
        response = urllib2.urlopen(theurl2)
    
    movdata = json.load(response)
    
    
    for mov in cache:
        if movdata[MKEY[1]] == mov[MKEY[1]]:
            dupe = True
    if not dupe:
        cache.append(movdata)

#===============================================================================
# GET DATA FROM OMDB API - GENERAL SEARCH
#===============================================================================

def gensearch (thetitle):
    """"""
    
    matches = []
    
    newtitle = enctitle(thetitle)
    
    theurl = "{0}{1}{2}".format(OMDBURL, Q[0], newtitle)
    
    response = urllib2.urlopen(theurl)
    
    movdata = json.load(response)
    
    for mov in movdata[MKEY[1]]:
        if mov[MKEY[2]] == "movie":
            matches.append(mov)
        
    if len(matches) > 0 < 10:
        index = 1
        print "Which one?" + NL
        for mov in matches:
            print "[{0}] {1} ({2})".format(str(index), mov[MKEY[3]], 
                                           mov[MKEY[4]])
            index += 1
    print
    newchoice = raw_input("Enter 1 - " + str(len(matches)) + ": ")
    
    newchoice = int(newchoice) - 1
    
    withid(matches[newchoice][MKEY[1]])

#===============================================================================
# MISC. FUNCTIONS
#===============================================================================

def enctitle (title):
    """Encodes a string for a URL"""
    
    return urllib2.quote(title)
