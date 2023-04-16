import cv2
import os



def find_faces(image_path):
    image = cv2.imread(image_path)

    # make a copy to prevent us from modifying the original
    color_img = image.copy()

    filename = os.path.basename(image_path)

    # opencv works best with gray images
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    # use opencv's built-in haar classifier
    haar_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

    faces = haar_classifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

    for (x, y, width, height) in faces:
        crop = image[y:y+height, x:x+width]

        # show the faces / eyes found
        return (crop, True)
    return (0,False)

if __name__ == '__main__':

    folder_path = "Images_DB"
    ensembles = os.listdir(folder_path)

    for ensemble in ensembles:
        path_ensemble = os.path.join(folder_path,ensemble)
        categories = os.listdir(path_ensemble)

        for category in categories:
            path_category = os.path.join(path_ensemble, category)
            images = os.listdir(path_category)

            for image in images:
                print(image)
                image_path = os.path.join(path_category, image)
                croped, booleen = find_faces(image_path)
                if(booleen):
                    cv2.imwrite(image_path, croped)