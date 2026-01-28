import matplotlib.pyplot as plt
import numpy as np
import os

PATH_FIGURES = 'figures'

# This file should only contain code related to making figure, not for computing data.

def make_figure(data: np.ndarray, filename: str) -> None:
    '''
    Inputs:
        data: A 2xN numpy array
        filename: The file will be saved in the default figures folder
    '''

    full_filename = os.path.join(PATH_FIGURES, filename)

    if not os.path.exists(PATH_FIGURES):
        os.mkdir(PATH_FIGURES)

    plt.figure(figsize=(6,6))
    plt.scatter(data[:,0], data[:,1])
    plt.savefig(full_filename, bbox_inches='tight')
    plt.show()
    return None