import string
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageOps
import cv2
import customtkinter
import random


picture_sizes = {
    'Custom': {},
    '1:1': {
        '1080x1080': (1080, 1080),
        '1200x1200': (1200, 1200),
        '2048x2048': (2048, 2048)
    },
    '3:2': {
        '1024x683': (1024, 683),
        '1920x1280': (1920, 1280),
        '2400x1600': (2400, 1600)
    },
    '2:3': {
        '683x1024': (683, 1024),
        '1280x1920': (1280, 1920),
        '1600x2400': (1600, 2400)
    },
    '4:3': {
        '800x600': (800, 600),
        '1024x768': (1024, 768),
        '1600x1200': (1600, 1200)
    },
    '16:9': {
        '1280x720': (1280, 720),
        '1920x1080': (1920, 1080),
        '3840x2160': (3840, 2160)
    }
}


def original_image_data(filename):
    try:
        img = cv2.imread(filename)
        return img.shape[1], img.shape[0]
    except AttributeError:
        pass


def browse_file():
    try:
        filename = filedialog.askopenfilename()
        x, y = original_image_data(filename)
        path_var.set(filename)
        width.set(x)
        height.set(y)
        image_obj = Image.open(filename)
        image_obj = ImageOps.exif_transpose(image_obj)
        w = 350
        if x/y > 1:
            h = round(y/x * w)
        elif x/y < 1:
            h = 350
            w = round((x/y) * h)
        else:
            h = w
        image_obj = image_obj.resize((w, h), Image.LANCZOS)

        image_asset = customtkinter.CTkImage(image_obj, size=(w, h))
        image_label.configure(image=image_asset, width=w, height=h)
        image_label.image = image_asset
        if filename != '':
            if input_1.get() != '' and input_2.get() != '' or aspect_var.get() != "Custom" and dropdown_var.get() != "-":
                submit_button.configure(state='enable')
        else:
            submit_button.config(state="disabled")
    except TypeError:
        pass


def output_path():
    random_name = ''.join(random.choices(string.ascii_lowercase, k=5))
    output = filedialog.asksaveasfilename(
                defaultextension='.jpg', filetypes=[("JPEG", '*.jpg'), ("PNG", '*.png')],
                initialdir=path_var.get(), initialfile=f'image_{random_name}_w_{width.get()}_h_{height.get()}',
                title="Choose filename")
    output_var.set(output)


def validate_custom():
    try:
        int(input_1.get())
    except ValueError:
        print(ValueError("Width is not int"))
    try:
        int(input_2.get())
    except ValueError:
        print(ValueError("Height is not int"))


def dropdown_callback(*args):
    try:
        return picture_sizes[aspect_var.get()][dropdown_var.get()]
    except KeyError:
        pass


def aspect_call(*args):
    if aspect_var.get() == 'Custom':
        dropdown.set('-')
        # submit_button.configure(state="disabled")


def validate_input_submit(*args):
    if input_1.get() != '' and input_2.get() != '' and submit_button.cget('state') == 'enabled':
        pass
    elif path_var.get() != '':
        if input_1.get() != '' and input_2.get() != '':
            submit_button.configure(state="enabled")
        else:
            submit_button.configure(state="disabled")
    else:
        submit_button.configure(state="disabled")


def validate_dropdown_submit(*args):
    if aspect_var.get() != "Custom" and dropdown_var.get() != "-" and submit_button.cget('state') == 'enabled':
        pass
    elif path_var.get() != '':
        if aspect_var.get() != "Custom" and dropdown_var.get() != "-":
            submit_button.configure(state="enabled")
        else:
            submit_button.configure(state="disabled")
    else:
        submit_button.configure(state="disabled")


def resize_image(image_route, width_int, height_int):
    image = cv2.imread(image_route)
    img_after = cv2.resize(image, (width_int, height_int))
    return img_after


def submit():
    # validate_filename_not_empty()
    validate_custom()
    output_path()
    if aspect_var.get() == 'Custom':
        img = resize_image(path_var.get(), int(input_1.get()), int(input_2.get()))
    else:
        (x, y) = dropdown_callback()
        img = resize_image(path_var.get(), x, y)
    cv2.imwrite(output_var.get(), img)


def update_resolutions(*args):
    submit_button.configure(state="disabled")
    aspect_ratio_set = aspect_var.get()
    if aspect_ratio_set == 'Custom':
        dropdown.configure(state='disabled')
        input_label.grid(row=10, column=0, padx=5, pady=5, sticky="w")
        input_1.grid(row=11, column=0, padx=5, pady=5, sticky="w")
        input_2.grid(row=12, column=0, padx=5, pady=5, sticky="w")
        input_1.configure(placeholder_text="Width")
        input_2.configure(placeholder_text="Height")
    else:
        dropdown.configure(state='enabled')
        input_1.delete(0, tk.END)
        input_2.delete(0, tk.END)
        input_label.grid_forget()
        input_1.grid_forget()
        input_2.grid_forget()
        resolutions = list(picture_sizes[aspect_ratio_set].keys())
        dropdown.configure(values=resolutions)


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("ImageResizer")
root.geometry("410x550")
root.minsize(650, 500)
root.maxsize(650, 500)
aspect_var = tk.StringVar()
path_var = tk.StringVar()
output_var = tk.StringVar()
width = tk.StringVar()
width.set("-")
height = tk.StringVar()
height.set("-")
dropdown_var = tk.StringVar()
dropdown_var.set("-")
aspect_var.set("-")
dropdown_var.trace("w", dropdown_callback)
aspect_var.trace('w', update_resolutions)

left_frame = customtkinter.CTkFrame(root)
right_frame = customtkinter.CTkFrame(root)
default_image = Image.open("placeholder.jpg")
default_image = default_image.resize((400, 400), Image.LANCZOS)

browse_button = customtkinter.CTkButton(left_frame, text="Upload File", command=browse_file)
browse_folder_button = customtkinter.CTkButton(left_frame, text="Upload Folder", command=browse_file)
output_value = customtkinter.CTkLabel(right_frame, textvariable=path_var)

width_label = customtkinter.CTkLabel(left_frame, text="Image Width:")
width_value = customtkinter.CTkLabel(left_frame, textvariable=width)
height_label = customtkinter.CTkLabel(left_frame, text="Image Height:")
height_value = customtkinter.CTkLabel(left_frame, textvariable=height)

dropdown_label = customtkinter.CTkLabel(left_frame, text="Change to:")
aspect_ratios = list(picture_sizes.keys())
aspect_dropdown = customtkinter.CTkOptionMenu(left_frame, variable=aspect_var, values=aspect_ratios, command=aspect_call)
dropdown = customtkinter.CTkOptionMenu(master=left_frame, values=[], variable=dropdown_var, command=validate_dropdown_submit)
input_label = customtkinter.CTkLabel(left_frame, text="Custom resolution(width,height):")

input_1 = customtkinter.CTkEntry(master=left_frame)
input_1.bind("<KeyRelease>", lambda event: validate_input_submit())

input_2 = customtkinter.CTkEntry(master=left_frame)
input_2.bind("<KeyRelease>", lambda event: validate_input_submit())

image = customtkinter.CTkImage(light_image=default_image, dark_image=default_image, size=(350, 350))
image_label = customtkinter.CTkLabel(right_frame, image=image, text='')

submit_button = customtkinter.CTkButton(root, text="Submit", command=submit, state='disabled')

#Frames
left_frame.grid(row=0, column=0, rowspan=13, padx=5, pady=5)
right_frame.grid(row=0, column=1, rowspan=13, padx=5, pady=5)

#File browsing section
browse_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")
browse_folder_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")
output_value.grid(row=13, column=1, padx=5, pady=5, sticky="w")

# Image preview section
image_label.grid(row=0, column=1, rowspan=13, padx=5, pady=5)

# Image dimensions section
width_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
width_value.grid(row=4, column=0, padx=5, pady=5, sticky="w")
height_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
height_value.grid(row=6, column=0, padx=5, pady=5, sticky="w")

# Dropdown selection section
dropdown_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
aspect_dropdown.grid(row=8, column=0, padx=5, pady=5, sticky="w")
dropdown.grid(row=9, column=0, padx=5, pady=5, sticky="w")

# Submit button
submit_button.grid(row=14, column=0, columnspan=2, padx=5, pady=5, sticky="s")

root.mainloop()
