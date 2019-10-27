from scipy.io import netcdf
#import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt
import geopandas

import matplotlib.animation as manimation

def plot_temperature_map_at_year(RCP_model=8.5, year=2006):
    filenames = {
        2.6: "tas_Amon_IPSL-CM5A-MR_rcp26_r1i1p1_200601-210012.nc",
        4.5: "tas_Amon_IPSL-CM5A-MR_rcp45_r1i1p1_200601-210012.nc",
        8.5: "tas_Amon_IPSL-CM5A-MR_rcp85_r1i1p1_200601-210012.nc",
        6.0: "d401c16d-f083-415d-8f53-d6a017cc9cd2-tas_Amon_IPSL-CM5A-MR_rcp60_r1i1p1_200601-210012.nc"
    }

    import os
    f1 = netcdf.netcdf_file(os.path.join("data/CMIP5_monthtly_temp", filenames[RCP_model]))

    lon = np.array(f1.variables['lon'][:])
    lat = np.array(f1.variables['lat'][:])
    tas = np.array(f1.variables['tas'][:])
    time = np.array(f1.variables['time'][:])

    # print(time.shape,tas.shape,lon.shape,lat.shape)
    weights = np.cos(np.deg2rad(lat))
    weights = weights/weights.sum()
    weights = weights[np.newaxis, :, np.newaxis]

    FFMpegWriter = manimation.writers['ffmpeg']
    metadata = dict(title='Movie temperature',
                    comment='Movie support!')
    writer = FFMpegWriter(fps=15, metadata=metadata)


    f, ax = plt.subplots(ncols=1, nrows=1,
                             figsize=(24, 24))
    for a in f.get_axes():
        a.axis('off')

    # ax = fig.add_subplot(1,1,1, projection=ccrs.Robinson())
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

    #ax.set_global()
    year_index = (year-2006)*12
    # Take average over one year:
    tas_at_year = np.concatenate((tas[year_index:year_index+12],tas[year_index:year_index+12,:,0,None]),axis=-1).mean(axis=0)

    lon = np.concatenate((lon,np.array([360.])))
    ax.set_aspect('equal')
    #ax.set_title(f"{title}")
    world.plot(ax=ax, color='lightblue', edgecolor='black')
    mask = lon > 180
    lon[mask] -= 360

    lo, la = np.meshgrid(lon, lat)
    # print(lo, la, tas[0])
    # print(lo.shape, la.shape, tas_at_year.shape)
    layer = ax.pcolormesh(lo, la, tas_at_year-273.15, cmap="jet",alpha = 0.5, edgecolor=(1.0, 1.0, 1.0, 0.3), linewidth=1e-10,
                          vmin=-10, vmax=35)


    # cbar = f.colorbar(layer, orientation="horizontal")
    # cbar.set_label("Temperature (K)")
    #ax.set_title(time[timeindex])
    # ax.gridlines()
    #ax.coastlines()
    # plt.show()

    # def init():
    #     layer.set_array([])
    #     return layer
    #
    # def animate(ktime):
    #     year = 2006+ktime
    #     year_index = (year - 2006) * 12
    #     # Take average over one year:
    #     tas_at_year = np.concatenate((tas[year_index:year_index + 12], tas[year_index:year_index + 12, :, 0, None]),
    #                                  axis=-1).mean(axis=0)
    #     layer.set_array(tas_at_year - 273.15)
    #     return layer

    NB_FRAMES = 94
    MONTH_AVERAGING = 24
    # anim = manimation.FuncAnimation(f, animate, init_func=init, frames=NB_FRAMES, interval=20, blit=True)


    with writer.saving(f, os.path.join(os.getcwd(), "plots", "video_RCP{}.mov".format(RCP_model)), 200):
        for i in range(NB_FRAMES):
            year += 1
            year_index = (year - 2006) * 12
            # Take average over one year:
            tas_at_year = np.concatenate((tas[year_index:year_index + MONTH_AVERAGING], tas[year_index:year_index + MONTH_AVERAGING, :, 0, None]),
                                         axis=-1).mean(axis=0)
            layer.set_array((tas_at_year-273.15).ravel())
            writer.grab_frame()
            ax.set_title("Year {}".format(year), fontsize=50)


    # f.savefig(os.path.join(os.getcwd(), "plots", "RCP{}_year_{}.png".format(RCP_model, year)), format='png')

plot_temperature_map_at_year(8.5, 2006)
plot_temperature_map_at_year(2.6, 2006)
plot_temperature_map_at_year(6.0, 2006)
