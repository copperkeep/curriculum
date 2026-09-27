def is_image(filename):
    name = filename.lower()
    return name.endswith(".png") or name.endswith(".jpg")
