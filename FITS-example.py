# FITS example:

from numpy.core.fromnumeric import argmax
from numpy.lib.npyio import load
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.utils.data import download_file

def main():
    image_file = download_file('http://www.astropy.org/astropy-data/photometry/M6707HH.fits', cache=True )
    hdu_list = fits.open(image_file)
    hdu_list.info()
    image_data = hdu_list[0].data
    print(type(image_data))
    print(image_data.shape)
    hdu_list.close()
    image_data = fits.getdata(image_file)
    print(type(image_data))
    print(image_data.shape)
    plt.imshow(image_data, cmap='gray')
    plt.colorbar()
    plt.show()

if __name__=="__main__":
    main()