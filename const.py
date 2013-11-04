#===============================================================================
# OMDb API Search Script - Module - const
#-------------------------------------------------------------------------------
# Version: 0.1.3
# Updated: 03-11-2013
# Author: Alex C.
# License: MIT
#-------------------------------------------------------------------------------
# Notes
#===============================================================================

"""
Contains the various constants used by the OMDb API Search Script.

"""

#===============================================================================
# LIST LEGEND
#===============================================================================

"""

#=== Query options ===#

Q[0] = "?s="
Q[1] = "?i="
Q[2] = "?t="

QOP[0] = "&y="
QOP[1] = "&plot="
QOP[2] = "&r="
QOP[3] = "&tomatoes=true"

PLOT[0] = "short"
PLOT[1] = "full"

#=== Display Info Labels ===#

INFOLBL[0] = "Directed by:"
INFOLBL[1] = "Written by:"
INFOLBL[2] = "Starring:"
INFOLBL[3] = "Genre:"
INFOLBL[4] = "Released:"
INFOLBL[5] = "Rated:"
INFOLBL[6] = "Runtime:"
INFOLBL[7] = "Produced by:"

IMDBLBL[0] = "Rating:"
IMDBLBL[1] = "Votes:"

RTLBL[0] = "Overall:"
RTLBL[1] = "Tomatometer:"
RTLBL[2] = "Rating:"
RTLBL[3] = "Reviews:"
RTLBL[4] = "Audience:"
RTLBL[5] = "Ratings:"

#=== OMDb JSON Keys ===#

MKEY[0] = "Search"
MKEY[1] = "imdbID"
MKEY[2] = "Type"
MKEY[3] = "Title"
MKEY[4] = "Year"
MKEY[5] = "Director"
MKEY[6] = "Writer"
MKEY[7] = "Actors"
MKEY[8] = "Genre"
MKEY[9] = "Released"
MKEY[10] = "Rated"
MKEY[11] = "Runtime"
MKEY[12] = "Production"
MKEY[13] = "Plot"
MKEY[14] = "imdbRating"
MKEY[15] = "imdbVotes"
MKEY[16] = "tomatoImage"
MKEY[17] = "tomatoMeter"
MKEY[18] = "tomatoRating"
MKEY[19] = "tomatoReviews"
MKEY[20] = "tomatoUserMeter"
MKEY[21] = "tomatoUserRating"
MKEY[22] = "tomatoUserReviews"

"""

import os

#===============================================================================
# MISC. FORMATTING
#===============================================================================

NL = ("\n")
HR = ("*" * 79)
HR2 = ("-" * 40)
HR3 = ("-" * 8)

#===============================================================================
# URLS AND QUERY OPTIONS
#===============================================================================

OMDBURL = ("http://www.omdbapi.com/")
IMDBURL = ("http://www.imdb.com/title/")

Q = ("?s=", "?i=", "?t=")
QOP = ("&y=", "&plot=", "&r=", "&tomatoes=true")
PLOT = ("&plot=short", "&plot=full")

#===============================================================================
# MENU OPTIONS
#===============================================================================

MAINOPT = ("Load file into cache", "Search cache", "Search OMDb API", "Exit")

SRCHOPT = ("Search by title", "Search by IMDb ID", )

FORMATS = ("json", "xml")

#===============================================================================
# TITLES
#===============================================================================

MENUTITLES = ("Main Menu", "Search Cache", "Format Selection", 
			  "Search OMDb API", )

INFOTITLES = ("Info", "IMDb Data", "Rotten Tomatoes Data")

#===============================================================================
# MOVIE INFO LABELS
#===============================================================================

INFOLBL = ("Directed by:", "Written by:", "Starring:", "Genre:", 
           "Released:", "Rated:", "Runtime:", "Produced by:")
        
IMDBLBL = ("Rating:", "Votes:")

RTLBL = ("Overall:", "Tomatometer:", "Rating:", 
          "Reviews:", "Audience:", "Ratings:")

#===============================================================================
# OMDB JSON KEYS
#===============================================================================

MKEY = ("Search", "imdbID", "Type", "Title", "Year", "Director", "Writer",
        "Actors", "Genre", "Released", "Rated", "Runtime", "Production",
        "Plot", "imdbRating", "imdbVotes", "tomatoImage", "tomatoMeter",
        "tomatoRating", "tomatoReviews", "tomatoUserMeter", 
        "tomatoUserRating", "tomatoUserReviews")

#===============================================================================
# USER INPUT QUERIES
#===============================================================================

UIQUERY = (">> ", "Would you like search again? ")

#===============================================================================
# ERROR MESSAGES
#===============================================================================

FILEERR = ("Can't find that file.")

LOADERR = ("Oops! Couldn't find that title.", "Oops! Couldn't find that ID.")

#===============================================================================
# MISC.
#===============================================================================

OSNAME = (os.name)

TESTID = ("tt0083658", "tt0076929", "tt0088247", "tt0066769", "tt0103064")
