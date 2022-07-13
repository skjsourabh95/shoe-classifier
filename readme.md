## [EdgeNet - Shoe Image Classifier Challenge](https://www.topcoder.com/challenges/ea6839ca-fa82-4ac9-9665-65ca738a1d46)
- The objective of this challenge is to train a machine learning or deep learning model and wrap it into a function and a CLI) that can classify shoe images by type.


## Tech Stack
- [Anaconda Python3](https://www.anaconda.com/distribution/)


## Deploying Jupyter Notebook With python==3.9.5
```CMD
conda create -n tensor2 python==3.9.5 -y
conda activate tensor2
pip install jupyter tensorflow matplotlib scipy pandas scikit-image scikit-learn Flask wget tqdm
cd /to/solution directory/
jupyter notebook
```

## Solution Run Notebook
```CMD
cd /to/solution directory/
open your browser
open the notebook
```
## NOTE 
- If you are using windows OS and if you get an error of win32comapi please install 'pip install pywin32 and re-run jupyter notebooks

## Deploying API 
```CMD
conda activate tensor2
cd /to/solution directory/classify_images/API/
python main.py
```

## Solution Run CLI
```CMD
conda activate tensor2
cd /to/solution directory/classify_images/CLI/
python call_api.py --filepath=filepath.txt
```
## NOTE 
- When you run this script it will take some time since its reading the model.
- The URL images are stored in a temp folder
- Add file paths each in a new line to filepath.txt for sending it to API.
- The ouput is printed in the CLI

## CLI ARGUMENTS 
--filepath - Text File Path Containing images(An example is present in the json)

## OUTPUT
- A predictions.csv is saved in the `predictions` directory inside the submisison after successfull completion of code in the inference notebook

## DATASET
- Dataset can be downloaded from [here](https://drive.google.com/file/d/1qz9fyraNTLzSKlqHIbWn9KenhmgZ_2uy/view?usp=sharing)
- The structure of the dir:
    - train - training the model - 2800 images
        - "boots"
        - "flip_flops"
        - "loafers"
        - "sandals"
        - "sneakers"
        - "soccer_shoes"
        - "no_shoe"
    - test - validating the model - 1050 images
        - "boots"
        - "flip_flops"
        - "loafers"
        - "sandals"
        - "sneakers"
        - "soccer_shoes"
        - "no_shoe"
    - val - inference's the model - any no of images (replace this with your images to test)
        - "boots"
        - "flip_flops"
        - "loafers"
        - "sandals"
        - "sneakers"
        - "soccer_shoes"
        - "no_shoe"
