import numpy as np

# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

import matplotlib.pyplot as plt
import seaborn as sns

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)
sns.set_style('dark')

# Load the images
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')
fl_im = skimage.io.imread('data/HG105_images/noLac_FITC_0004.tif')


plt.imshow(phase_im, cmap=plt.cm.viridis)
plt.close()

# Apply a gaussian blur to the image
im_blur = skimage.filters.gaussian(phase_im, 50.0) # radius = 50

# Show the blurred image
plt.imshow(im_blur, cmap=plt.cm.viridis)
plt.close()

# Convert phase image to a float
phase_float = skimage.img_as_float(phase_im) # rescaling between zero and one
phase_sub = phase_float - im_blur

plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('original')

plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtracted')

plt.close()

# Appy otsu thresholding
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh

plt.imshow(seg, cmap=plt.cm.Greys_r)
plt.close()

# Label each pixel 'island'
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)
plt.close()

# Compute the region properties and extract area of each object
ip_dist = 0.063 # µm per pixel
props = skimage.measure.regionprops(seg_lab)
# props[0].area would give the pixel area of the first object

# Get the areas as an array
areas = np.array([prop.area for prop in props])
cutoff = 300

im_cells = np.copy(seg_lab) > 0
for i, _ in enumerate(areas):
    if areas[i] < cutoff:
        # Erase it from our image by setting all pixels = 0
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)

plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)
#plt.imshow(im_cells)
plt.show()
