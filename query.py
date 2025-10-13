from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u
from scipy.ndimage import map_coordinates

# --- load the distance map ---
exthdu = fits.open('/yourdirectory/MC_RC_Distance_Map_Oden25_galactic.fits')
extim = exthdu[0].data
exthead = exthdu[0].header

wcs    = WCS(exthead)  # in galactic coordinates
Ny, Nx = extim.shape

# --- your data (ICRS) ---
coo_icrs = SkyCoord(data['ra']*u.deg, data['dec']*u.deg, frame='icrs')

# Convert to Galactic Coords
coo_gal = coo_icrs.galactic
x, y = wcs.world_to_pixel(SkyCoord(l=coo_gal.l, b=coo_gal.b, frame='galactic'))

dist = np.full(x.shape, np.nan, float)
dist = map_coordinates(extim, [y,x], order=0, mode='nearest')

# store back to your table (same length as data rows)
data['dist'] = dist
