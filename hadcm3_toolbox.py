import numpy as np
import numpy.ma as ma


def running_mean(data, n):
    """
    Running mean on n years for a 1D array. Only use the past values.

    Parameters
    ----------
    data : list of numpy 1D array
        data to process the running mean
    n : int
        number of years to perform the running mean
    Returns
    -------
    list of numpy 1D array
        new averaged data
    """
    mean = np.convolve(data, np.ones((n)), mode="full")
    out_mean = np.zeros((len(data)))
    for i in range(len(data)):
        if i + 1 < n:
            out_mean[i] = mean[i] / (i + 1)
        else:
            out_mean[i] = mean[i] / n
    return out_mean


def coordinate_to_index(longitude, latitude, target_lon, target_lat):
    """
        Find the closet -or at least pretty clos- indexes from a coordiantes grid to a point.
        inc should have the magnitude of the grd size

        Parameters
        ----------
        lon : numpy 2D array
            grid longitudes coordinates
        lat : numpy 2D array
            grid latitudes coordinates
        lon_p : float?
            point longitude
        lat_p : float?
            point latitude
        inc :  float, optional
            step for the research (default is 0,5)
        Returns
        -------
        int, int
            indexes that match the longitudes and the latitudes.
        """
    i_out = (np.abs(latitude - target_lat)).argmin()
    j_out = (np.abs(longitude - target_lon)).argmin()

    return j_out, i_out


def lon_to_index(longitude, target_lon):
    return (np.abs(longitude - target_lon)).argmin()


def lat_to_index(latitude, target_lat):
    return (np.abs(latitude - target_lat)).argmin()
