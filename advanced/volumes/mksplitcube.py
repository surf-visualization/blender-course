import numpy as np
import openvdb as vdb

dimension = 400

array = np.zeros((dimension, dimension, dimension))
for i in range(dimension):
   for j in range(dimension):
      for k in range(dimension):
         if i < 200 and i >=100 and \
          j < 200 and j >=100 and \
          k < 200 and k >=100:

            array[i,j,k] = 1.0

grid = vdb.FloatGrid()
grid.copyFromArray(array)
grid.name = "cube"

array2 = np.zeros((dimension, dimension, dimension))
for i in range(dimension):
   for j in range(dimension):
      for k in range(dimension):
         if i < 200 and i >=100 and \
          j < 200 and j >=100 and \
          k < 200 and k >=100:

            array2[i,j,k] = 0.0 if i < 150 else 1.0

grid2 = vdb.FloatGrid()
grid2.copyFromArray(array2)
grid2.name = "cube2"

vdb.write('split-cube.vdb', grids=[grid, grid2])
