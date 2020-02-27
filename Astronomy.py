import numpy as np 
from datetime import datetime, date
from astropy.time import TimeDelta, Time
# Astronomy.py
# Purpose: The purpose of this function is to convert
# Date, Time, Location of observer, with RA and Dec of
# orbital object, outputting the Azimuth and Altitude (deg)
# of said object. 
# Input:
#   Date (yyyy-mon-dd), ex, Jan, Feb, Mar, Apr...etc
#   Right Acension (hh-mmm), 16-41.7 (16h 41.7min)
#   Declination (aaa-mm), 360-28 (360deg 28min)
#   Time (hhmm), UT 
#   Latitude (deg-mm-NS), 052-30-N, (52deg 30min North)
#   Longitude (deg-mm-EW), 01-55-W, (01deg 55min West)
# Output:
#   Azimuth (deg), 269.1deg
#   Altitude (deg), 49.2deg



def main():

    #Input Variables
    Date = datetime(1998,8,10,23,10)
    RA = '16-41.7'
    Dec = '36-28'
    Time = '2310'
    Latitude = '52-30-N'
    Longitude = '01-55-W'
    Today = datetime.now()

    DaysBetween = daysBetweenJulianEpoch(Today)
    print(DaysBetween)

    
def LocalSiderealTime(DaysBetween, Longitude, UT):

    LST = 100.46 + 0.985647*DaysBetween + Longitude + 15*UT


def daysBetweenJulianEpoch(theDate):
    JulianEpoch = datetime(2000,1,1,12)
    Delta = theDate - JulianEpoch 

    DaysBetween = Delta.days + (Delta.seconds/86400)
    print(DaysBetween)
    return DaysBetween

if __name__ == "__main__":

    main()