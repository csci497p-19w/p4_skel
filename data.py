import numpy as np
import skimage as skim

from numpy import pi, sin, cos

cat = {
    'img_fn':'data/cat/Image_%02d.png',
    'lights_fn': 'data/cat/lights.txt',
    'img_range': (1, 21)
}

lizard = {
    'img_fn': 'data/lizard/Image_%02d.png',
    'lights_fn': 'data/lizard/lights.txt',
    'img_range': (1, 21)
}

tentacle_rendered = {
    'img_fn': 'data/tentacle_rendered/%04d.png',
    'img_range': (1, 10)
}

tentacle_real = {
    'img_fn': 'data/tentacle_real/meas-%05d-00000.png',
    'img_range': (1, 10)
}

datasets = {
    'cat': cat,
    'lizard': lizard,
    'tentacle_rendered': tentacle_rendered,
    'tentacle_real': tentacle_real
}


def tentacle_lights():
    rotations = (
        (0, 0),
        (0, 15),
        (0, -15),
        (-15, 15),
        (-15, 15),
        (15, 15),
        (15, -15),
        (15, 0),
        (-15, 0),
    )

    lights = []
    for rotx, roty in rotations:
        direction = np.array(((0.0, ), (0.0, ), (1.0, )))

        radians_x = rotx / 180.0 * pi
        new_x = direction[1] * cos(radians_x) - \
            direction[2] * sin(radians_x)
        new_y = direction[1] * sin(radians_x) + \
            direction[2] * cos(radians_x)
        direction[1] = new_x
        direction[2] = new_y

        radians_y = roty / 180.0 * pi
        new_z = direction[2] * cos(radians_y) - \
            direction[0] * sin(radians_y)
        new_x = direction[2] * sin(radians_y) + \
            direction[0] * cos(radians_y)
        direction[2] = new_z
        direction[0] = new_x

        lights.append(direction)

    return np.hstack(lights)

def load_dataset(ds_name):
    try:
        ds = datasets[ds_name]
    except KeyError:
        print "Dataset not found."
        return

    images = [skim.io.imread(ds['img_fn'] % i) for i in range(*ds['img_range'])]

    if ds_name == 'tentacle_real':
        return images

    if ds_name == 'tentacle_rendered':
        lights = tentacle_lights()
    else:
        lights = np.loadtxt(ds['lights_fn'], delimiter=',')

    return images, lights
