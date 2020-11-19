import numpy as nm 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs #used to plot over an Equirectangular projection
from skyfield.api import load, EarthSatellite 
#import all the necessary libraries as well as the SGP4 propogator

ts = load.timescale()

#TLE information for chosen satelite CATSAT-2
TLE="""1 44029U 98067PV  20317.18380552  .00059143  00000+0  44070-3 0  9993
2 44029  51.6377 284.2794 0001336 353.3524   6.7456 15.72187078101707"""

#Separate the TLE data into individual lines
L1, L2 = TLE.splitlines()

#the skyfield EarthSatellite will use the SGP4 model to calculate trajectory of satellite
satellite= EarthSatellite(L1, L2, name='CATSAT-2')
print(satellite)

#define orbit for one day in intervals of 0.01
day = nm.arange(0, 100, 0.01) # one 24 hour orbit
#date as of completing code, ts.now() function can be used as well
time   = ts.utc(2020, 11, 12, 0, day)

#use the skyfield geocentric and subpoint functions to obtain longitude and latitude plotting points
geocentric = satellite.at(time)
subpoint = geocentric.subpoint()

fig = plt.figure(figsize=(30, 40)) #figure size
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree()) #project over a Plate Carree projection
ax.stock_img() #cartopy stock flat earth image, no not that kind
ax.coastlines() #add coastlines
ax.gridlines(color='black') #add gridlines to plot

ax.scatter(subpoint.longitude.degrees, subpoint.latitude.degrees, transform=ccrs.PlateCarree(),
            color='blue')
plt.show()



