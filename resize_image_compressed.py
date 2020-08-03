import os
import time
import numpy as np
import imageio as im
from PIL import Image

dir_path = os.getcwd()  # Get current directory
image_list = []     # Initialize
image_filetype = ['jpg', 'png', 'jpeg']     
for f in os.scandir(dir_path):
    if f.name.split('.')[-1].lower() in image_filetype:
        image_list.append(f.name)
    
print('A total of %d images are found in this directory.'%(len(image_list)))

print("The first 5 image filenames are: ")
if len(image_list) > 5:
    for i in range(5):
        print(image_list[i])
else:
    for i in image_list:
        print(i)

print('\n\n')

# time.sleep(30) # Checkpoint

while True: # To allow error in user input
    user_input = input("Please enter the factors to be resized, i.e. 2,3.. etc,\n")
    try:
        resized_factor = float(user_input)
        break
    except ValueError:
        continue

# resized_factor = int(float(input()))
while float(resized_factor) == 0.0:
    print("Enter again, no zero")
    resized_factor = float(input())


for f_image in image_list:
    my_image = Image.open(f_image)
    width, height = my_image.size[0], my_image.size[1]
    width_new, height_new = int(width/resized_factor), int(height/resized_factor)
    print("Original (width*height): %d * %d image file" %(width, height))
    print("Resizing to %d * %d file" %(width_new, height_new))
    my_image = my_image.resize((width_new, height_new))
    # my_image.show()

    my_image.save(f_image)

print("Resize Done!")

os.system("pause")
