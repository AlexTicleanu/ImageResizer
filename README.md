

# Image Resizer Application

## Introduction
This application allows users to resize images in two different ways, either by selecting a resolution from a list or by inputting a custom resolution. The user can select a single image or a folder of images to resize, and the output images are saved to a specified location.

![image](https://user-images.githubusercontent.com/48204339/234834883-8bf15ad5-bd1f-4ea8-a263-d44db1760cab.png)


## Prerequisites
- Python 3.x
- tkinter
- CustomTkinter(https://github.com/TomSchimansky/CustomTkinter)
- Pillow
- OpenCV

## Installation
1. Clone the repository
2. Install the required packages:
```sh
pip install -r requirements.txt
```
3. Run the application:
```sh
python main.py
```

## Usage
1. Click the `Browse` button to select an image file or a folder of image files.
2. If you selected an image file, the image will be displayed on the screen. If you selected a folder, a folder icon will be displayed on the screen.
3. Select a resolution from the drop-down list or input a custom resolution.
4. Click the `Submit` button to resize the image(s). The resized images will be saved to the specified location.

## Code Structure
- `main.py`: contains the main code of the application
- `image_functions.py`: contains functions for image processing and resizing
- `validations.py`: contains functions for input validation
- `resolution_dict.py`: contains the list of predefined resolutions and the dictionary of aspect ratios
