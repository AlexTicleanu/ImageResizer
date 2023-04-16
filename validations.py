import string
import random
from tkinter import filedialog


def validate_custom(input_1, input_2):
    try:
        int(input_1.get())
    except ValueError:
        print(ValueError("Width is not int"))
    try:
        int(input_2.get())
    except ValueError:
        print(ValueError("Height is not int"))


def output_path():
    from resolution_dict import path_var, output_var, width_image, height_image
    random_name = ''.join(random.choices(string.ascii_lowercase, k=5))
    output = filedialog.asksaveasfilename(
                defaultextension='.jpg', filetypes=[("JPEG", '*.jpg'), ("PNG", '*.png')],
                initialdir=path_var.get(), initialfile=f'image_{random_name}_w_{width_image.get()}_h_{height_image.get()}',
                title="Choose filename")
    output_var.set(output)


def dropdown_callback(*args):
    from resolution_dict import picture_sizes, dropdown_var, aspect_var
    try:
        return picture_sizes[aspect_var.get()][dropdown_var.get()]
    except KeyError:
        pass


def output_path_dir():
    from resolution_dict import output_var
    output = filedialog.askdirectory()
    output_var.set(output)