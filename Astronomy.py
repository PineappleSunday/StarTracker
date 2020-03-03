import numpy as np 
from datetime import datetime, date
from astropy.time import TimeDelta, Time
import math as m

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

# http://www.stargazing.net/kepler/altaz.html
# https://www.swift.psu.edu/secure/toop/convert.htm
# 
# https://www.instructables.com/id/Two-Axis-Star-Tracker/
# https://www.instructables.com/id/Star-Track-Arduino-Powered-Star-Pointer-and-Tracke/




def main():

    #Input Variables
    OldDate = datetime(1998,8,10,23,10)
    RA = '16-41.7'
    Dec = '36-28'
    Time = '2310'
    LatDMS = '52-30-00-N'
    LongDMS = '01-55-00-W'
    TodayDate = datetime.now()


    LST = LocalSiderealTime(LongDMS, OldDate, Time)
    HA = HourAngle(LST, RA)
    
    Alt, Az = HaDecToAltAz(RA, Dec, HA, LatDMS)
    print(Alt, Az)

def HaDecToAltAz(RA, Declination, HourAngle, Latitude):
    A = float(RA[3]+RA[4]+RA[5]+RA[6])/60
    RA_Format = m.radians((float(RA[0]+RA[1]) + A)*15)
    Lat = m.radians(dms2dd(Latitude))
    Dec = m.radians(float(Declination[0]+Declination[1]) + float(Declination[3]+Declination[4])/60)
    
    Alt1 = m.sin(Dec)*m.sin(Lat)
    Alt2 = m.cos(Lat)*m.cos(m.radians(HourAngle))*m.cos(Dec)
    Alt = m.asin(Alt1+Alt2)

    A1 = m.sin(Dec)-(m.sin(Alt)*m.sin(Lat))
    A2 = m.cos(Alt)*m.cos(Lat)
    A = m.acos(A1/A2)

    if m.sin(m.radians(HourAngle))>0:
        Az = 360-m.degrees(A)
    else:
        Az = m.degrees(A)

    return m.degrees(Alt), Az
def HourAngle(LST, RA):
    A = float(RA[3]+RA[4]+RA[5]+RA[6])/60 
    #Multiply by 15 to get into degrees, 15deg in a minute
    RA_Format = (float(RA[0]+RA[1]) + A)*15
    HA = LST - RA_Format
    while(HA<0):
        HA+=360
    
    return HA

def LocalSiderealTime(Longitude, GivenDate, CurrentTime):   
    DaysBetween = daysBetweenJulianEpoch(GivenDate)
    LongDeg = dms2dd(Longitude)
    Hours = float(CurrentTime[0]+CurrentTime[1])
    Minutes = float((CurrentTime[2]+CurrentTime[3]))/60
    UT_Format =  Hours+Minutes
    LST = 100.46 + (0.985647*DaysBetween) + LongDeg + (15*UT_Format)

    while(LST < 0):
        LST+= 360
    
    return LST
    
def dms2dd(DMS):

    degrees = DMS[0]+DMS[1] 
    minutes = DMS[3]+DMS[4]
    seconds = DMS[6]+DMS[7]
    direction = DMS[9]

    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd

def daysBetweenJulianEpoch(theDate):
    JulianEpoch = datetime(2000,1,1,12)
    Delta = theDate - JulianEpoch 

    DaysBetween = Delta.days + (Delta.seconds/86400)
    #print(DaysBetween)
    return DaysBetween

if __name__ == "__main__":

    main()
