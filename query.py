from astropy.io import fits              
from astropy.wcs import WCS              
from scipy.ndimage import map_coordinates
import numpy as np 

exthdu = fits.open('/yourdirectory/MC_RC_Distance_Map_Oden25.fits')
extim = exthdu[0].data
exthead = exthdu[0].header

wcs = WCS(exthead)             # In Magellanic Stream Coordinates (Nidever+2008)

x, y = wcs.world_to_pixel_values(np.asarray(data['mlon'], float), np.asarray(data['mlat'], float))

vals = map_coordinates(extim, [y, x], order=1, mode="constant", cval=np.nan)
distance_map = vals

