#!/usr/bin/env python
# https://www.openvdb.org/documentation/doxygen/python.html
# section Working with NumPy arrays
#
# On Arch need to run this as
# LD_PRELOAD=/usr/lib/libjemalloc.so python script.py
# to avoid a segfault related to JEMalloc
import pyopenvdb as vdb
import numpy

array = numpy.random.rand(200, 200, 200)
print(array.dtype)

# Copy values from a three-dimensional array of doubles
# into a grid of floats.
grid = vdb.FloatGrid()
print('Copying')
grid.copyFromArray(array)
assert grid.activeVoxelCount() == array.size
print(grid.evalActiveVoxelBoundingBox())
grid.name = 'float'

# Metadata doesn't appear in Blender?
grid['myattrib'] = 1.0
grid['myattrib2'] = 'doh!'
grid['myattrib3'] = False
grid['myattrib4'] = (1,2,3)

vdb.write('floats.vdb', grids=[grid])

# Copy values from a four-dimensional array of ints
# into a grid of float vectors.
vecarray = numpy.ndarray((60, 70, 80, 3), int)
vecarray.fill(42)
vecgrid = vdb.Vec3SGrid()
vecgrid.copyFromArray(vecarray)
print('Copying')
assert vecgrid.activeVoxelCount() == 60 * 70 * 80
print(vecgrid.evalActiveVoxelBoundingBox())
vecgrid.name = 'float3'

vdb.write('float3s.vdb', grids=[vecgrid])

# Both grids written to the same file
vdb.write('floats-and-float3s.vdb', grids=[grid,vecgrid])