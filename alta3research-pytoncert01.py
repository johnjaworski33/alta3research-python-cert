#!/usr/bin/env python3

#"""This is just a basic Python script to show i was listening and learned a few thing.  Dont expect miricles with this script. I used to write complext bahs scripts so concepts like reg exptressions or wrting in funcitons is not new to me but that was over a decade ago and  im a newbie at python"


# Usage:  Just answer the questions but the idea behind the script in my head was to test
#         a few things we did in class but i could imagine intead of hand input i would gather a few
#         stats from our switches in real life like port and port utilzation or ISL utilization and then
#         that could be graphed
#
#         Here , in the first part, just answer the questions with anything you want but something
#        like:
#        Switch1  90
#        switch2  60
#        switch3  40
#
#        when that created the Excel, i thought "great..now lets make a plot or graph". Thats when
#        Things went horribly wrong.  I worked for hours making changes and now im stuck with what 
#        looks like basic syntax but im also wondering if im causing confusion with python (or just me)
#        my importing and using excel calls from both pandas and pyexcel
#
#        so can you help me with how i would take and input filename and graph something as simple as
#        a list of text switches and each of thier numbers?
#


# After the intro, always list your global variables and imports
import pyexcel
import time		#can we really import time?..wouldnt that be nice
#			We weill use these imports for the second part of this script
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import xlrd
import pylab


#                    ***  This is the funtion sectiion. ***
# Conjuction functions ..whats your function..dated reference you might have to look up
#
#    Just like with my bash scripts you should always put your work in
#    separate functions for bot readablity and to make it eaiser to add other
#    code  w/o disturbing the peace


# Request data from user
def get_switchdata():
    read_swname = input("\nWhat is the switch name? ")
    read_percent_util = input("Enter numerical  Percent utilized of the switch:")
    d = {"Switch": read_swname, "%Util": read_percent_util}
    return d


# start our main script
def main():

   mylistdict = []  # this will be our list we turn into a *.xls file

   while(True):
      mylistdict.append(get_switchdata())
      keep_going = input("\nWould you like to enter anouther switch? Hit Enter to continue, or 'q' to quit: ")
 
      if (keep_going.lower() == 'q'):
           break

   filename = input("\nWhat is the name of the *.xls file? ")
   pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')
   print("Ok..Now i will  make you and Excel workbook. Please be  patiant. This will take a while..")
   time.sleep(4)	#sleep for 6 seconds
   print("Just kidding..come on..im a computer. Im done...")
   print("\nThe file " + filename + ".xls should be in your local directory")
   print("\nYou can look at that Excel file now ..but we will move onto the second Student test..")
   print("\n\nLets take that Excel sheet of switch percent busy and make a pretty graph for managgement")

#
#   If the below was working , it should be functionalized above and called from here
#
   #   makeitpretty():
   #   workbook = xlrd.open_workbook(filename)
   records = pyexcel.iget_records(file_name=f'{filename}.xls')
   for record in records:
      #print("%s switch is at %d" % (record['Switch' ], record['Util' ]))
      print(record)

   readfile = pd.read_excel('file2.xls' , 'pyexcel_sheet1' )
   # create plot
   plt.plot(readfile['Switch'], readfile['Util'])
   plt.xlabel('Switches')
   plt.ylabel('Util percentage')
   plt.title('Hooky JJ graph')
   plt.legend()
   plt.show()

if __name__ == "__main__":
   main()
