from PIL import Image

img_name = input("Image name: \n")
use_dither = input("\nUse dithering for gray areas? (y/n): \n").lower() == 'y'

if(not use_dither):
    thr = input("\nThershold: \n")


# Load the image
image = Image.open(img_name)

# Convert to grayscale
gray_image = image.convert("L")

if use_dither:
    # Convert to 1-bit with dithering (Floyd-Steinberg)
    bw_image = gray_image.convert("1")  # default uses dithering
else:
    # Ask for a threshold value
    thr = int(input("Threshold (0-255): \n"))
    bw_image = gray_image.point(lambda x: 0 if x < thr else 255, '1')

# Save the image
bw_image.save(img_name.split(".")[0]+".bmp")
