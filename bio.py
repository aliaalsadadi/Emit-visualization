import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import geopandas as gpd
# Open the L1R file
l1r_file = 'hyperion.L1R'  # Replace with the path to your L1R file
src = rasterio.open(l1r_file)

print(src.read())
print(src.meta)

# Plot the L1R data using matplotlib
# plt.figure(figsize=(10, 10))
# show(l1r_data, cmap='gray')
# plt.axis('off')
# plt.show()
#
#
# bioscape_domain = gpd.read_file('bioscape_domain.geojson')
# bioscape_domain.plot()
# plt.show()
# src.close()








