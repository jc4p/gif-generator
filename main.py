from PIL import Image
from moviepy.editor import ImageSequenceClip
from os import remove, walk
import sys

# The width and height for the outputted GIF. 
pic_size = 648, 432

# def get_frame(img, x, y):
#     return img.crop((x, y, x + pic_size[0], y + pic_size[1]))

def make_gif():
    files = []
    for (dirpath, dirnames, filenames) in walk("input"):
        files.extend(["input/" + x for x in filenames if ".jpg" in x])
    
    image_names = ["output/frame_{}.jpg".format(x) for x in range(len(files))]
    for i in range(len(files)):
        im = Image.open(files[i])
        im.thumbnail(pic_size, Image.ANTIALIAS)
        print image_names[i]
        im.save(image_names[i], quality=100)

    newName = "result.gif"

    clip = ImageSequenceClip(image_names, fps=4)
    clip.write_gif(newName, fuzz=False)

    for f in image_names:
        remove(f)
    print ""

if __name__ == "__main__":
    make_gif()