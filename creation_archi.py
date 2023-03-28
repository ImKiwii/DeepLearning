import os

folder_path = "Images"
folder_path_dest = "Images_DB"
if not(os.path.exists(folder_path_dest)):
    os.makedirs(folder_path_dest)
categories = os.listdir(folder_path)
print(categories)

for category in categories:
    if (category != "train" and category != "validation" and category != "test"):
        images_path = os.path.join(folder_path, category, "triees")

        images = os.listdir(images_path)

        nb_images = len(images)

        nb_images_train = round(nb_images * 3 / 4)
        nb_images_validation = round(nb_images / 8)
        nb_images_test = nb_images - nb_images_train - nb_images_validation

        images_deplacees = 0

        dir = os.path.join(folder_path_dest, "train", category)
        if not(os.path.exists(dir)):
            os.makedirs(dir)
        dir = os.path.join(folder_path_dest, "validation", category)
        if not(os.path.exists(dir)):
            os.makedirs(dir)
        dir = os.path.join(folder_path_dest, "test", category)
        if not(os.path.exists(dir)):
            os.makedirs(dir)

        for train in range(nb_images_train):
            path_image_src = os.path.join(images_path, images[images_deplacees])
            path_image_dest = os.path.join(folder_path_dest, "train", category, images[images_deplacees])
            os.rename(path_image_src,path_image_dest)
            images_deplacees += 1

        for train in range(nb_images_validation):
            path_image_src = os.path.join(images_path, images[images_deplacees])
            path_image_dest = os.path.join(folder_path_dest, "validation", category, images[images_deplacees])
            os.rename(path_image_src,path_image_dest)
            images_deplacees += 1

        for train in range(nb_images_test):
            path_image_src = os.path.join(images_path, images[images_deplacees])
            path_image_dest = os.path.join(folder_path_dest, "test", category, images[images_deplacees])
            os.rename(path_image_src,path_image_dest)
            images_deplacees += 1