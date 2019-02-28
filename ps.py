import numpy as np
import skimage as skim

def calibrated_gray(images, lights):
    """ Compute calibrated photometric stereo on a stack of grayscale images.
            images: a list of n 2D uint8 images (h x w)
            lights: a 3xn matrix of light vectors, one per image
        Returns:
            normals (h x w x 3)
            albedo (h x w)
    """
    return None, None


def calibrated_color(images, lights):
    """ Compute calibrated photometric stereo on a stack of color images.
            images: a list of n color uint8 images (h x w x 3)
            lights: a 3xn matrix of light vectors, one per image
        Returns:
            normals (h x w x 3)
            albedo (h x w x 3)
    """
    return None, None


def uncalibrated_gray(images):
    """ Compute uncalibrated photometric stereo on a stack of grayscale images.
            images: a list of n 2D uint8 images (h x w)
        Returns:
            normals (h x w x 3)
            albedo (h x w)
    """
    return None, None


def uncalibrated_color(images):
    """ Compute uncalibrated photometric stereo on a stack of color images.
            images: a list of n color uint8 images (h x w x 3)
        Returns:
            normals (h x w x 3)
            albedo (h x w x 3)
    """
    return None, None


if __name__ == '__main__':
    from data import load_dataset

    for ds in ['cat', 'lizard']:
        normals, albedo = calibrated_gray(*load_dataset(ds))

        if normals is not None:
            skim.io.imsave('%s_normals.png' % (ds,), normals)
        if albedo is not None:
            skim.io.imsave('%s_albedo.png' % (ds,), albedo / albedo.max())

    for ds in ['tentacle_rendered']:
        normals, albedo = calibrated_color(*load_dataset('tentacle_rendered'))

        if normals is not None:
            skim.io.imsave('%s_normals.png' % (ds,), normals)
        if albedo is not None:
            skim.io.imsave('%s_albedo.png' % (ds,), np.clip(albedo,0,1))

    images, _ = load_dataset('cat')
    normals, albedo = uncalibrated_gray(images)
    if normals is not None:
        skim.io.imsave('%s_uncalib_normals.png' % (ds,), normals)
    if albedo is not None:
        skim.io.imsave('%s_uncalib_albedo.png' % (ds,), np.clip(albedo,0,1))


    images = load_dataset('tentacle_real')
    normals, albedo = uncalibrated_color(images)

    if normals is not None:
        skim.io.imsave('%s_uncalib_normals.png' % (ds,), normals)
    if albedo is not None:
        skim.io.imsave('%s_uncalib_albedo.png' % (ds,), np.clip(albedo,0,1))


