import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import torch
import xarray as xr
import os


if torch.cuda.is_available():
    torch.set_default_device('cuda')
else:
    torch.set_default_device('cpu')


def read_precip():
    data_frame_list = []
    for i in os.listdir(os.path.join("scripts/outputs/PRECIP")):
        filename  = os.path.join("scripts/outputs/PRECIP",i)
        data_frame = xr.open_dataset(filename,decode_coords="all").to_array()[0,:,:,:]
        data_frame_list.append(data_frame)
    return np.concatenate(data_frame_list,axis=0)

def read_pet():
    data_frame_list = []
    for i in os.listdir(os.path.join("scripts","outputs","PET")):
        data_frame_list.append(xr.open_dataset(os.path.join("scripts","outputs","PET",i),decode_coords="all").to_array())
    return np.concatenate(data_frame_list,axis=0)


def samlmusmall(x, nmom=5):
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
        return [l1, l2]

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
        return [l1, l2, l3]

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
        return [l1, l2, l3, l4]

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

    return [l1, l2, l3, l4, l5]
    try:
        x = torch.as_tensor(x, dtype=torch.float64)
        n = x.shape[0]
        x.sort(dim=0)
    except ValueError:
        raise ValueError("Input data to estimate L-moments must be numeric.")

    if nmom <= 0 or nmom > 5:
        raise ValueError("Invalid number of sample L-moments")

    if n < nmom:
        raise ValueError("Insufficient length of data for specified nmoments")

    # First L-moment

    l1 = torch.sum(x,dim=0) / sp.special.comb(n, 1, exact=True)

    if nmom == 1:
        return l1

    # Second L-moment

    comb1 = range(n)
    coefl2 = 0.5 / sp.special.comb(n, 2, exact=True)
    sum_xtrans = sum([(comb1[i] - comb1[n - i - 1]) * x[i] for i in range(n)])
    l2 = coefl2 * sum_xtrans

    if nmom == 2:
        return [l1, l2]

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
        return [l1, l2, l3]

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
        return [l1, l2, l3, l4]

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

    return [l1, l2, l3, l4, l5]

def get_lm_paras(d_seq:np.array) -> np.array:
    lm_est = torch.as_tensor(np.asarray(samlmusmall(d_seq,3)))
    kappa = (0.488138*lm_est[2]**1.70839)-(1.7631*lm_est[2]**0.981824)+0.285706
    alpha = (1.023602813*lm_est[2]**1.8850974-2.95087636*lm_est[2]**1.195591244+1.759614982)*lm_est[1]
    zeta = (-0.0937*lm_est[2]**4-0.2198*lm_est[2]**3+1.407*lm_est[2]**2-1.4825*lm_est[2]-0.6205)*lm_est[1]+lm_est[0]
    return np.asarray([kappa.cpu().numpy(),zeta.cpu().numpy(),alpha.cpu().numpy()])


if __name__ == '__main__':
    pre_frame = read_precip()[0:192,:,:]*0.1
    pet_frame = read_pet()
    d_frame=np.float64(pre_frame-pet_frame)
    print("Data loaded")
    para_mat = get_lm_paras(d_frame)

    np.save("scripts/outputs/para_mat.npy",para_mat)