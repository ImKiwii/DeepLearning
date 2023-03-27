import numpy as np
from PIL import Image
import io
import os


folder_path = "Images"
categories = os.listdir(folder_path)
print(categories)

for category in categories:
    images_path = os.path.join(folder_path, category, "triees")

    images = os.listdir(images_path)

    for i in range(np.size(images)):
        path_image = os.path.join(images_path,images[i])
        extensions = images[i].split('.')
        extension = extensions[1]
        os.rename(path_image,os.path.join(images_path , category + str(i) + "." + extension))