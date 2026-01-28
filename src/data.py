import numpy as np
import os

PATH_DATA = 'data'

# this file should contain code related to working with the data... nothing else

def make_data(n: int = 100, low: int = 0, high: int = 25) -> np.array:
    '''
    Return an n*2 array of random integers between low and high (inclusive)
    '''
    return np.random.randint(low=low, high=high+1, size=(n,2))

def save_data(data: np.ndarray, filename: str) -> None:
    '''
    Save a numpy array to the default output folder,
    ensuring the folder exists.
    '''
    full_filename = os.path.join(PATH_DATA, filename)

    # Ensure the output directory exists
    if not os.path.exists(PATH_DATA):
        os.mkdir(PATH_DATA)

    if type(data) != np.ndarray:
        raise TypeError(f'Data should be a numpy array, but a {type(data)} was provided.')

    if os.path.exists(full_filename):
        raise FileExistsError(f'File {full_filename} already exists.')
    
    np.save(full_filename, data)

    return None

def load_data():
    '''
    Loads data from an .npy file located in the default data directory.
    ---
    I kinda lost track, so I have a placeholder.
    '''
    exclamation_of_success = 'Yay, this function works!'
    print(exclamation_of_success)
    return exclamation_of_success

# uv add jupyter
# uv run jupyter lab