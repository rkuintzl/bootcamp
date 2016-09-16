"""Contains functions useful for processing phase images"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters

# Set matplotlib rc params.
rc = {'lines.linewidth' : 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)
sns.set_style('dark')


def load_image(image_file):
    """Converts image to matrix using skimage"""
    image = skimage.io.imread(image_file)
    return image


def correct_uneven_illumination(image, radius):
    """Convert image to float. Apply gaussian blur to image
       and then subtract this from the image."""

    # Convert phase image to a float (rescale between zero and one)
    im_float = skimage.img_as_float(image)
    im_blur = skimage.filters.gaussian(image, radius)

    # Substract image blur
    im_sub = im_float - im_blur

    return im_sub


def correct_for_hot_pixels(image, width=3):
    """Generate a structural element; apply median filter to get rid of 'hot' pixel"""

    selem = skimage.morphology.square(width) # can take in this param
    im_filt = skimage.filters.median(image, selem)

    return im_filt


def apply_threshold(image):
    """Compute Otsu threshold value to impose pixel value cutoff"""

    thresh_otsu = skimage.filters.threshold_otsu(image)
    image_seg = image < thresh_otsu

    return image_seg


def apply_size_filter(seg_labs, cutoff_lower=300, cutoff_upper=10000):
    """Removes objects too large or small"""

    areas, props = measure_object_areas(seg_labs)
    im_objects = np.copy(seg_labs) > 0  # what?
    for i, _ in enumerate(areas):
        if areas[i] < cutoff_lower or areas[i] > cutoff_upper:
            # Erase it from our image by setting all pixels = 0
            im_objects[seg_labs==props[i].label] = 0

    size_filt_labs = skimage.measure.label(im_objects)

    return size_filt_labs


def clear_borders(seg_labs):
    """Remove objects touching the image border"""

    image_trimmed = skimage.segmentation.clear_border(seg_labs)
    return image_trimmed


def label_objects(image):
    """ Label each pixel 'island' """

    seg_labels, num_objects = skimage.measure.label(image, return_num=True, background=0)
    return seg_labels, num_objects


def measure_object_areas(seg_labs):
    """Compute the region properties and extract area of each object"""

    props = skimage.measure.regionprops(seg_labs)
    areas = np.array([prop.area for prop in props])

    return areas, props

def process_image(image, radius, width, cutoff_lower, cutoff_upper):
    """Call all image-processing functions in proper order.
       Image will be evened, filtered, segmented, labeled,
       and otherwise cleaned up."""

    image_cooled = correct_for_hot_pixels(image, width)
    image_even = correct_uneven_illumination(image_cooled, radius)
    image_seg = apply_threshold(image_even)
    seg_labs, num_objects = label_objects(image_seg)
    seg_labs = clear_borders(seg_labs)
    size_filt_labs = apply_size_filter(seg_labs, cutoff_lower, cutoff_upper)

    return size_filt_labs

#############################################
## Begin "executable" portion of code here ##
#############################################

image_file_1 = 'data/HG105_images/noLac_phase_0004.tif'
image_file_2 = 'data/bsub_100x_phase.tif'

image_1 = load_image(image_file_1)
image_2 = load_image(image_file_2)

# Specify parameters
radius = 50.0
width = 3
size_cutoff_lower = 200
size_cutoff_upper = 10000

im_filt_labs_1 = process_image(image_1, radius, width, size_cutoff_lower, size_cutoff_upper)
size_cutoff_lower = 450
im_filt_labs_2 = process_image(image_2, radius, width, size_cutoff_lower, size_cutoff_upper)

plt.figure()
plt.imshow(image_1, cmap=plt.cm.Greys_r)

plt.figure()
plt.imshow(im_filt_labs_1, cmap=plt.cm.Spectral_r)

plt.figure()
plt.imshow(image_2, cmap=plt.cm.Greys_r)

plt.figure()
plt.imshow(im_filt_labs_2, cmap=plt.cm.Spectral_r)

plt.show()
