#!/usr/bin/python3
"""========================================================================
Purpose:
    The purpose of this script is to execute and build the fit-up
    calculation for the Lead Use Assembly.
Author:
    Emilio Torres
========================================================================"""
#=========================================================================#
# Preamble                                                                #
#=========================================================================#
#-------------------------------------------------------------------------#
# Python Packages                                                         #
#-------------------------------------------------------------------------#
import sys
import os
from subprocess             import call
#=========================================================================#
# Executing the python calculation                                        #
#=========================================================================#
filename    = "PS1"
call(["clear"])
pwd = os.getcwd()
#=========================================================================#
# Constructing the document                                               #
#=========================================================================#
os.chdir(pwd)
#-------------------------------------------------------------------------#
# 1st build                                                               #
#-------------------------------------------------------------------------#
call(["pdflatex", filename])
#-------------------------------------------------------------------------#
# Create index                                                            #
#-------------------------------------------------------------------------#
call(["makeindex", filename])
#-------------------------------------------------------------------------#
# Create list of abbreviations                                            #
#-------------------------------------------------------------------------#
call(["makeindex","fit-up.nlo","-s","nomencl.ist","-o",filename + ".nls"])
#-------------------------------------------------------------------------#
# Create bibliography                                                     #
#-------------------------------------------------------------------------#
call(["bibtex", filename])
#-------------------------------------------------------------------------#
# 2nd build                                                               #
#-------------------------------------------------------------------------#
call(["pdflatex", filename])
#-------------------------------------------------------------------------#
# 3rd build                                                               #
#-------------------------------------------------------------------------#
call(["pdflatex", filename])
#-------------------------------------------------------------------------#
# Embedding fonts                                                         #
#-------------------------------------------------------------------------#
#embed fonts
call(["gs", "-dNOPAUSE", "-dBATCH", "-sDEVICE=pdfwrite",\
        "-dPDFSETTINGS=/prepress",\
        "-sFONTPATH='/usr/share/fonts/truetype/msttcorefonts'",\
        "-dEmbedAllFonts=true", "-sOutputFile=tmp.pdf", "-f",\
        "TTP-1-3162.pdf"])
call(["clear"])
print("BOOM! Done!")
sys.exit(0)
