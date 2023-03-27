import os
import time
from PIL import Image
import io

# Import des packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests

########################################################################
# category : String qui permet de savoir dans quelle catégorie on souhaite 
#            trier les images (happy, sad, angry...)
# search : String qui prend correspond à la recherche sur google
# nbPic : Int qui correspond au nombre d'images que l'on veut télécharger
# time_for_scrolling : Int en seconde qui dépend de votre connexion internet
category = "angry"
search='angry woman'
nbPic = 200
time_for_scrolling = 2 # 1 si fibre ou entre 2 et 5 selon la connection wifi
########################################################################
# path 
directory = os.path.join("Images", category, "a_trier")

# Create the directory 
try: 
    if not os.path.exists(directory):
        os.makedirs(directory)
except OSError as error: 
    print("ERROR : {}".format(error)) 

#Opens up web driver and goes to Google Images
browser = webdriver.Firefox()

#load google image
browser.get('https://www.google.fr/imghp?hl=en')

delay = 10 # seconds
try:
    btnId="L2AGLb"
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID , btnId))) #id info-address-place-wrapper 
    elm=browser.find_element(By.ID , btnId)
    elm.click()
    print("Popup is passed!")
except TimeoutException as e:
    print("Loading took too much time!")


WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME , "gLFyf")))
# get and fill search bar
box = browser.find_element(By.CLASS_NAME , "gLFyf")
box.send_keys(search)
time.sleep(time_for_scrolling)
box.send_keys(Keys.ENTER)


#Will keep scrolling down the webpage until it cannot scroll no more
last_height = browser.execute_script('return document.body.scrollHeight')

passe = False
while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(time_for_scrolling)
    new_height = browser.execute_script('return document.body.scrollHeight')
        
    if (new_height == last_height):# and passe):
        break
    elif (new_height == last_height):
        element = browser.find_element(By.CLASS_NAME,"mye4qd")
        element.click()
        passe = True
        #break
    last_height = new_height
    

image_urls=[]
images_par_pourcent = nbPic/100
pourcent = 0
for i in range(1, nbPic+1):
    # Trouver et cliquer sur toutes les miniatures
    try:
        miniature = browser.find_element(By.XPATH,'//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
    
        miniature.click()

        # Récupérer l'url des images des miniature
        class_name = "n3VNCb"
        image_pour_url = browser.find_elements(By.CLASS_NAME, class_name)
        for k in range(len(image_pour_url)):
            url_image = image_pour_url[k]
            url = url_image.get_attribute("src")
            if(("http" in  url) and (not "encrypted" in url)):
                image = requests.get(url,timeout=5)
                image_from_web = Image.open(io.BytesIO(image.content))
                image_path = os.path.join(directory,str(i)+"."+image_from_web.format.lower())
                image_from_web.save(image_path)
    except:
        nbPic += 1
        pass

    if (i > (pourcent + 1) * images_par_pourcent):
        pourcent += 1
        print(str(pourcent) + "% des images ont été téléchargées.")

print(str(100) + "%.")
print("Fin du téléchargement, fermeture du navigateur")

browser.quit()
