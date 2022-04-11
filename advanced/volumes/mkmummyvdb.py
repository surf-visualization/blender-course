#!/usr/bin/env python
# On Arch need to run this as
# LD_PRELOAD=/usr/lib/libjemalloc.so python script.py
# to avoid a segfault related to JEMalloc
import tarfile
import numpy
from PIL import Image
from io import BytesIO
import pyopenvdb as vdb

tar = tarfile.open('../../../../data/basics/importing_data/mummy-slices.tar.gz', 'r:gz')
members = tar.getmembers()
members.sort(key = lambda e: e.name)
images = []
for member in members:
    data = tar.extractfile(member).read()
    b = BytesIO(data)
    img = Image.open(b)
    print(img)
    images.append(img)
    
W, H = images[0].size
S = len(images)

print('%d slice images of %dx%d pixels' % (S, W, H))

voxels = numpy.empty((S, W, H), dtype=numpy.float32)
for idx, slice_image in enumerate(images):
    # Store each slice image in the voxel array
    # Use only R channel of RGB image
    slice_data = numpy.asarray(slice_image)
    assert slice_data.shape == (W, H, 3)
    # Map to unit range
    voxels[idx,:,:] = slice_data[:,:,0] / 255

print(voxels)
print(voxels.shape)
print(numpy.min(voxels), numpy.max(voxels))
print(numpy.histogram(voxels))

# Create a VDB grid
grid = vdb.FloatGrid()
grid.copyFromArray(voxels)
print(grid.activeVoxelCount())
#assert grid.activeVoxelCount() == voxels.size
print(grid.evalActiveVoxelBoundingBox())
grid.name = 'value'

vdb.write('mummy.vdb', grids=[grid])
