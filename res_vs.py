def triple_res_plot():
        # Average over time and assign data to variables
    ts1_ann = ds1.TS.mean(dim='time')
    ts2_ann = ds2.TS.mean(dim='time')
    ts3_ann = ds3.TS.mean(dim='time')

    # Arrays for loop processing
    ts_arr = [ts1_ann, ts2_ann, ts3_ann]
    reses = ['200', '100', '25']

    # Define the figure and each axis for the 1 rows and 3 columns
    fig, axs = plt.subplots(nrows=1, ncols=3,
                            subplot_kw={'projection': ccrs.PlateCarree()},
                            figsize=(16, 5.5))

    # axs is a 2 dimensional array of `GeoAxes`.
    # We will flatten it into a 1-D array
    # axs = axs.flatten()

    # Loop over all of the datasets and plot
    for i in range(len(ts_arr)):

        # Select the dataset
        data = ts_arr[i]

        # Add the cyclic point
        data, lons = add_cyclic_point(data, coord=data['lon'])

        # Contour plot
        cs = axs[i].contourf(lons, ts_arr[i].lat, data,
                            transform=ccrs.PlateCarree(),
                            cmap='coolwarm', extend='both')

        # Title each subplot with the name of the model
        axs[i].set_title(reses[i] + "km res")

        # Draw the coastines for each subplot
        axs[i].coastlines()

        # Define the xticks for longitude
        axs[i].set_xticks(np.arange(-180, 181, 60), crs=ccrs.PlateCarree())
        lon_formatter = cticker.LongitudeFormatter()
        axs[i].xaxis.set_major_formatter(lon_formatter)

        # Define the yticks for latitude
        axs[i].set_yticks(np.arange(-90, 91, 30), crs=ccrs.PlateCarree())
        lat_formatter = cticker.LatitudeFormatter()
        axs[i].yaxis.set_major_formatter(lat_formatter)
