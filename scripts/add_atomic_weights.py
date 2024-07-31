from ase import Atoms
from ase.io import read, write
import numpy as np


data = read('train.xyz', index=':')

for i in range(len(data)):
    data[i].arrays["atomic_weights"] = np.ones(len(data[i].get_positions())).reshape(-1,1)*50
    #data[i].arrays["atomic_weights"] *= 0.1

write('train_weights.xyz', data)