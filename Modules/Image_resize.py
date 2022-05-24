from PIL import ImageTk, Image

# With the help of this function, we can change the size of the photos to the desired size
def resize(path):
    # Load the desire image 
    load_img = Image.open(path)
    # Resize the image 
    resize_img = load_img.resize((75,40),Image.ANTIALIAS)
    # Create an object of tkinter ImageTk and pass the resized image to it
    img = ImageTk.PhotoImage(resize_img)
    return img


def volume_resize(path):
    # Load the desire image 
    load_img = Image.open(path)
    # Resize the image 
    resize_img = load_img.resize((30,25),Image.ANTIALIAS)
    # Create an object of tkinter ImageTk and pass the resized image to it
    img = ImageTk.PhotoImage(resize_img)
    return img