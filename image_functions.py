import cv2


def original_image_data(filename):
    try:
        img = cv2.imread(filename)
        return img.shape[1], img.shape[0]
    except AttributeError:
        pass


def resize_image(image_route, width_int, height_int):
    image = cv2.imread(image_route)
    img_after = cv2.resize(image, (width_int, height_int))
    return img_after


def reset_app():
    from resolution_dict import aspect_var, path_var, width_image, height_image, dropdown_var
    path_var.set('')
    width_image.set('-')
    height_image.set('-')

