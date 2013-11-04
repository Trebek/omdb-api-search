#===============================================================================
# OMDb API Search Script - Module - srchdat
#-------------------------------------------------------------------------------
# Version: 0.1.3
# Updated: 03-11-2013
# Author: Alex C.
# License: MIT
#-------------------------------------------------------------------------------
# Notes
#===============================================================================

"""
Contains functions for searching movie data, either from a JSON file, 
or from the OMDb API.

"""

#===============================================================================
# IMPORTS
#===============================================================================

import msvcrt

from const import *
import dispdat
import getdat

#===============================================================================
# SEARCH FOR TITLE
#===============================================================================

def fortitle (omdb=False):
    """"""
    
    def titlesearch ():
        """"""

        for mov in getdat.cache:
            
            movtitle = mov[MKEY[3]].lower()
            movtitlespl = mov[MKEY[3]].lower().split()
            
            if search == movtitle or search == movtitle[4:]:
                if year == "":
                    dispdat.movdata(mov)
                    return True
                else:
                    if year == mov[MKEY[4]]:
                        dispdat.movdata(mov)
                        return True
            # elif any(word in searchspl for word in movtitlespl):
            #     for word in search.split():
            #          if word in movtitlespl:
            #                 matches.append("{0} ({1})").format(mov[MKEY[3]], 
            #                                                    mov[MKEY[4]])

        else:
            return False

    # matches = []

    dispdat.osclear()

    dispdat.title("Search by Title")

    title = getdat.getinput("Title: ")
    year = getdat.getinput("Year (optional): ")
    
    search = title.lower()
    searchspl = search.split()
    searchl = len(searchspl)

    found = titlesearch()

    if not found and omdb:

        getdat.withtitle(search, year)
        # elif searchl == 2:
        #     getdat.withtitle(searchpl[0], searchpl[1])
        found = titlesearch()
        
    # if len(matches) > 0 < 10: 
    #     index = 1   
    #     print("Which one?" + NL) 
    #     for title in matches:
    #         print("[{0}] {1}").format(str(index), title)
    #         index += 1
    #     print
    #     newchoice = raw_input("Enter 1 - " + str(len(matches)) + ": ")

    if not found:
        print
        print LOADERR[0] + NL
        getdat.getinput()
        return True
    else:
        cmd = getdat.getinput(UIQUERY[1])
        if cmd in ["y", "Y"]:
            return True
        elif cmd in ["n", "N"]:
            return False

#===============================================================================
# SEARCH FOR IMDB ID
#===============================================================================

def forid (omdb=False):
    """"""

    def idsearch ():
        """"""

        for mov in getdat.cache:
            if mov[MKEY[1]] == ID:
                dispdat.movdata(mov)
                return True
        else:
            return False

    # matches = []

    dispdat.osclear()

    ID = getdat.getinput("IMDb ID: ")

    if ID[0:2] != "tt":
        ID = "tt" + ID

    found = idsearch()

    if not found and omdb:

        getdat.withid(ID)
        found = idsearch()

    if not found:
        print
        print LOADERR[1] + NL
        getdat.getinput()
        return True
    else:
        cmd = getdat.getinput(UIQUERY[1])
        if cmd in ["y", "Y"]:
            return True
        elif cmd in ["n", "N"]:
            return False
            