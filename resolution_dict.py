import tkinter as tk

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


aspect_var = tk.StringVar()
path_var = tk.StringVar()
output_var = tk.StringVar()
width_image = tk.StringVar()
width_image.set("-")
height_image = tk.StringVar()
height_image.set("-")
dropdown_var = tk.StringVar()
dropdown_var.set("-")
aspect_var.set("-")



