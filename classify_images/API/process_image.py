import os
import tensorflow as tf 
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import numpy as np
from skimage import transform
import wget
import json
import tqdm

def load(filename):
    '''
        Input: ImagePath
        Output : Process image array
    '''
    np_image = Image.open(filename) # open image
    np_image = np.array(np_image).astype('float32')/255 # normalize image
    np_image = transform.resize(np_image, (256, 256, 3)) # resize image
    np_image = np.expand_dims(np_image, axis=0)
    return np_image

def download_image(url,dest='temp'):
    '''
        Input: Image URL
        Output : Path of the downloaded image
    '''

    if not os.path.exists(dest):
        os.mkdir(dest)

    filename = 'temp.jpg'
    filename = os.path.join(dest, filename)
    wget.download(url, filename)

    return filename

def classify_images(image_paths):  
    '''
        Input: List of image local paths or URLs
        Output : List of predicted labels
    '''
    # load config file
    with open('config.json','r') as f:
        CONFIG = json.load(f)

    # get saved model path from config
    model_path = CONFIG['model_path']

    # get label indexes from config
    classes = CONFIG['classes']

    # load model in memory - may take few mins
    model = tf.keras.models.load_model(model_path)

    response = []
    for image_path in tqdm.tqdm(image_paths):
        if 'http' in image_path:
            # if path is a URL
            local_path = download_image(image_path) # download image
            image = load(local_path) # process image
            preds = model.predict(image) # predict label index
            output = classes[np.argmax(preds,axis=1)[0]] # get the label
            response.append(output)
        else:
            # image path is a local path
            image = load(image_path) # process image
            preds = model.predict(image) # predict label index
            output = classes[np.argmax(preds,axis=1)[0]] # get the label
            response.append(output)

    return {'response':response}