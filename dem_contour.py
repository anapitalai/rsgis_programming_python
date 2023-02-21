import gdal
import numpy as np

# Load contour lines
contour_file = "path/to/contour.shp"
contour_ds = gdal.OpenEx(contour_file, gdal.OF_VECTOR)
contour_layer = contour_ds.GetLayer()

# Create output raster
raster_file = "path/to/output.tif"
raster_ds = gdal.GetDriverByName("GTiff").Create(raster_file, 1000, 1000, 1, gdal.GDT_Float32)
raster_ds.SetGeoTransform((xmin, cellsize, 0, ymin, 0, cellsize))
raster_ds.SetProjection(projection)

# Interpolate elevations at grid cells
gdal.FillNodata(targetBand=raster_ds.GetRasterBand(1), maskBand=None, maxSearchDist=None, smoothingIterations=None)
gdal.Grid(destName=raster_file, srcDSLayer=contour_layer, zfield='elevation', algorithm='invdist:power=2:smoothing=0.0')

# Read DEM as numpy array
dem_array = raster_ds.GetRasterBand(1).ReadAsArray()

# Optional: plot DEM using matplotlib
import matplotlib.pyplot as plt
plt.imshow(dem_array, cmap='terrain', interpolation='none')
plt.colorbar()
plt.show()
