import numpy as np

import os

folder_path = "Images"
categories = os.listdir(folder_path)
print(categories)

for category in categories:
    images_path = os.path.join(folder_path, category, "triees")

    images = os.listdir(images_path)

    for i in range(np.size(images)):
        print(images[i])
        os.rename(images[i],path_dest+"/"+ str(passage) + "_"+imag)