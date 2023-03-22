Deep Learning Installation

Étape pour le downloader de la base de donnée :
	Installer python : https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe
		Grâce à python on peut faire dans le powershell windows : (pip est déjà installé)
		pip install selenium
		pip install requests
		
Installer Firefox : https://www.mozilla.org/fr/firefox/download/thanks/

Script qui permet de télécharger les images sur google pour la base de donnée : download_images.py	
	
Étape pour le traitement d’image :
	pip install keyboard
	pip install matplotlib
	pip install numpy
	pip install os

Script qui permet de trier les images de la base de donnée : trier_images.py


Pour ce qui est des paramètres à changer dans chaque fichiers, ils sont tous dans la zone délimitée par les lignes de commentaire (#####...#)

Pour lancer les scripts, il faut lancer dans l’ordre :

	py download_images.py
	py trier_images.py
