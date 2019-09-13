# import classes from Pillow

from PIL import Image, ImageDraw, ImageFont
import random

def memeText(memer):
    memeTextInList = list(memer)
    postMemeText = []
    while True:
        if len(postMemeText) < len(memer):
            for a in memeTextInList:
                if random.randint(0,50) < 25:
                    postMemeText.append(a.upper())
                else:
                    postMemeText.append(a)
        return postMemeText


# Create an Image variable with the input Image

image = Image.open('spongebob.jpg')

# Initialize the drawing context with
# the image object as background

draw = ImageDraw.Draw(image)

# Create font object with the font file 
# and specify desired size

font = ImageFont.truetype('Roboto-Bold.ttf', size=45)

# starting position of the message

(x, y) = (50, 50)
message = input("What's the meme gonna be here boys?\n")

color = 'rgb(0, 0, 0)' # black color

# draw the message on the background

draw.text((x, y), ''.join(memeText(message)), fill=color, font=font)

# save the edited image
randomFileName = str(random.randint(0,10000000))
image.save(f'{randomFileName}.jpg')