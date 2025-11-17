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

vdb.write('cube.vdb', grids=[grid])
