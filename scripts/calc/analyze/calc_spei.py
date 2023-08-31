from typing import Any
import numpy as np
import scipy as sp
import torch
import xarray as xr
import os
from numba_stats import norm
import numpy.typing as npt

def read_precip() -> np.ndarray:
    data_frame_list = []
    for i in os.listdir(os.path.join("scripts/outputs/PRECIP")):
        filename  = os.path.join("scripts/outputs/PRECIP",i)
        data_frame = xr.open_dataset(filename,decode_coords="all").to_array()[0,:,:,:]
        data_frame_list.append(data_frame)
    return np.concatenate(data_frame_list,axis=0)

def read_pet() -> np.ndarray:
    data_frame_list = []
    for i in os.listdir(os.path.join("scripts","outputs","PET")):
        data_frame_list.append(xr.open_dataset(os.path.join("scripts","outputs","PET",i),decode_coords="all").to_array())
    return np.concatenate(data_frame_list,axis=0)

def get_lmoments(x, nmom=5) -> np.ndarray:
    try:
        x = np.asarray(x, dtype=np.float64)
        n = x.shape[0]
        x.sort(axis=0)
    except ValueError:
        raise ValueError("Input data to estimate L-moments must be numeric.")

    if nmom <= 0 or nmom > 5:
        raise ValueError("Invalid number of sample L-moments")

    if n < nmom:
        raise ValueError("Insufficient length of data for specified nmoments")

    # First L-moment

    l1 = np.sum(x,axis=0) / sp.special.comb(n, 1, exact=True)

    if nmom == 1:
        return l1

    # Second L-moment

    comb1 = range(n)
    coefl2 = 0.5 / sp.special.comb(n, 2, exact=True)
    sum_xtrans = sum([(comb1[i] - comb1[n - i - 1]) * x[i] for i in range(n)])
    l2 = coefl2 * sum_xtrans

    if nmom == 2:
        return np.array([l1, l2])

    # Third L-moment

    comb3 = [sp.special.comb(i, 2, exact=True) for i in range(n)]
    coefl3 = 1.0 / 3.0 / sp.special.comb(n, 3, exact=True)
    sum_xtrans = sum(
        [
            (comb3[i] - 2 * comb1[i] * comb1[n - i - 1] + comb3[n - i - 1]) * x[i]
            for i in range(n)
        ]
    )
    l3 = coefl3 * sum_xtrans / l2

    if nmom == 3:
        return np.array([l1, l2, l3])

    # Fourth L-moment

    comb5 = [sp.special.comb(i, 3, exact=True) for i in range(n)]
    coefl4 = 0.25 / sp.special.comb(n, 4, exact=True)
    sum_xtrans = sum(
        [
            (
                comb5[i]
                - 3 * comb3[i] * comb1[n - i - 1]
                + 3 * comb1[i] * comb3[n - i - 1]
                - comb5[n - i - 1]
            )
            * x[i]
            for i in range(n)
        ]
    )
    l4 = coefl4 * sum_xtrans / l2

    if nmom == 4:
        return np.array([l1, l2, l3, l4])

    # Fifth L-moment

    comb7 = [sp.special.comb(i, 4, exact=True) for i in range(n)]
    coefl5 = 0.2 / sp.special.comb(n, 5, exact=True)
    sum_xtrans = sum(
        [
            (
                comb7[i]
                - 4 * comb5[i] * comb1[n - i - 1]
                + 6 * comb3[i] * comb3[n - i - 1]
                - 4 * comb1[i] * comb5[n - i - 1]
                + comb7[n - i - 1]
            )
            * x[i]
            for i in range(n)
        ]
    )
    l5 = coefl5 * sum_xtrans / l2

    return np.array([l1, l2, l3, l4, l5])

def get_gev_lm_paras(lm_est:np.ndarray) -> np.ndarray:
    kappa = (0.488138*lm_est[2]**1.70839)-(1.7631*lm_est[2]**0.981824)+0.285706
    alpha = (1.023602813*lm_est[2]**1.8850974-2.95087636*lm_est[2]**1.195591244+1.759614982)*lm_est[1]
    zeta = (-0.0937*lm_est[2]**4-0.2198*lm_est[2]**3+1.407*lm_est[2]**2-1.4825*lm_est[2]-0.6205)*lm_est[1]+lm_est[0]
    return np.array([kappa,zeta,alpha])


def gev_cdf(x:npt.ArrayLike, c:npt.ArrayLike, loc:npt.ArrayLike, scale:npt.ArrayLike)-> np.ndarray:
    if torch.cuda.is_available():
        torch.set_default_device('cuda')
    else:
        torch.set_default_device('cpu')
    # This function is designed for GPU
    x = torch.tensor(x)
    c = torch.tensor(c)
    loc = torch.tensor(loc)
    scale = torch.tensor(scale)
    # Use the general formula
    z = 1 - c * (x - loc) / scale
    return torch.exp(-z ** (1 / c)).cpu().numpy()

# Protect the main function
if __name__ == '__main__':
    pre_frame = read_precip()[0:192,:,:]*0.1
    pet_frame = read_pet()
    d_frame_1=pre_frame-pet_frame
    print("Data loaded")
    # Calulate the L-moments
    lm_est = get_lmoments(d_frame_1,3)
    # Get the parameters of the GEV distribution
    para_mat = get_gev_lm_paras(lm_est)
    print("Parameters calculated")
    # Calculate the probability
    prob_mat = gev_cdf(d_frame_1,para_mat[0],para_mat[1],para_mat[2])
    print("Probability calculated")
    # Use the inverse of the standard normal distribution
    # Use the numba_stats package to speed up
    spei_mat = norm.ppf(prob_mat,loc=0,scale=1) # type: ignore
    print("SPEI calculated")

    # Use this daraset's metadata to create a new dataset
    ref_dataset = xr.open_dataset("scripts/outputs/PET/2000_01.nc",decode_coords="all")
    month = np.array([i for i in range(1,193)])
    latArr = sorted(ref_dataset.coords['y'])
    lonArr = sorted(ref_dataset.coords['x'])
    # Reverse the longitude
    spei_mat = np.flip(spei_mat,axis=1)
    # Create a new dataset of SPEI
    spei_frame = xr.Dataset(
    data_vars = {
        'spei':(['month','y','x'],spei_mat)
    },
    coords={
        'x': (['x'], lonArr),
        'y': (['y'], latArr),
        'month':month
    }
    )
    # Write coordinate system
    spei_frame.rio.write_crs(4326, inplace=True).rio.set_spatial_dims(x_dim="x",y_dim="y",inplace=True).rio.write_coordinate_system(inplace=True)
    # Save the dataset
    spei_frame.to_netcdf("scripts/outputs/SPEI/spei.nc")
    print("SPEI saved")
    input("Press Any key to continue...")