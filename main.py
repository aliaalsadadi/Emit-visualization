import netCDF4
import matplotlib.pyplot as plt
import matplotlib.animation as animation
file = 'EMIT_L2A_RFL_001_20231004T065929_2327705_043.nc'
ds = netCDF4.Dataset(file)
reflectance = ds.variables['reflectance']
fig, ax = plt.subplots()
def update(frame):
    ax.clear()
    heatmap = reflectance[:, :, frame]  # Extract the 2D slice for the current frame
    im = ax.imshow(heatmap, cmap='hot')  # Plot the heatmap
    return im,
ani = animation.FuncAnimation(fig, update, frames=285, interval=0.1, blit=True)
plt.show()