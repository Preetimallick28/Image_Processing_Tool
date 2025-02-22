# import os
# import PIL
# import tkinter as tk
# from tkinter import filedialog, messagebox
# from tkinter.filedialog import *
#
# from PIL import Image
#
# image = Image.open("photo.jpg")
# image.show()
#
# # Display basic properties of the image
# print("Image format:", image.format)
# print("Image mode:", image.mode)
# print("Image size:", image.size)
#
# # resizing a image
# new_image = image.resize((500,500))
# new_image.save('photo_resize.jpg')
#
# # converting jpg to png
# img = Image.open("photo.jpg")
# img.save("photo_new.png")
#
# # to convert the image from png to jpg
#
# img_png = Image.open("photo_new.png")
# img_png.save("photo_jpg.jpg")
#
# # compress a image
# file_path = askopenfilename()
# img_compressor_before = PIL.Image.open(file_path)
# myHeight , myWidth = img_compressor_before.size
# img_after_compression = img_compressor_before.resize((myHeight , myWidth) , PIL.Image.ANTIALIAS)
# save_path = asksaveasfilename()
# img_after_compression.save(save_path+"_compressed.JPG")
