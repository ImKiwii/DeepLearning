import keyboard
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

import os
import time


########################################################################
# category : String qui permet de savoir dans quelle catégorie on souhaite 
#            trier les images (happy, sad, angry...)
category = "happy"
########################################################################


path = os.path.join("Images", category, "a_trier")
path_dest = os.path.join("Images", category, "triees")
path_del = os.path.join("Images", category, "a_supprimer")

try: 
    if not os.path.exists(path_dest):
        os.makedirs(path_dest)
except OSError as error: 
    print("ERROR : {}".format(error)) 

try: 
    if not os.path.exists(path_del):
        os.makedirs(path_del)
except OSError as error: 
    print("ERROR : {}".format(error)) 

list = os.listdir(path)
nb_images = (np.size(list))
print(list)

plt.ion()
plt.show()

for imag in list:
    if((not 'del' in imag[0]) and (not "ok" in imag[0:1])):
        file=os.path.join(path,imag)
        image = img.imread(file)
        plt.imshow(image)
        plt.pause(0.5)
        plt.draw()
        
        while(True):
            key = keyboard.read_key()
            match key:
                case 'droite':
                    # Valider l'image donc le déplacer
                    os.rename(file,path_dest+"/"+imag)
                    print("image OK")
                    break
                case 'gauche':
                    # Ne pas valider l'image donc la supprimer
                    os.rename(file,path_del+"/"+imag)
                    print("besoin de delete")
                    break
                case _:
                    print("Mauvaise touche, vous ne pouvez toucher que la flèche droite ou gauche.")
                    time.sleep(.5)

    

