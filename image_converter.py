







            # HELLO EVERYONE , TODAY I HAVE CREATED A IMAGE PROCESSING TOOL
            # USING PYTHON... IT IS VERY SIMPLE TOOL IN WHICH FOR UI HAVE USED
            # TKINTER AND FOR IMAGE PROCESSING I HAVE USED PILLOW ...
            # SO LET US SEE FRIENDS , HOW THE IMAGE PROCESSING TOOL WORKS












import os
import PIL
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image


def resize_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    image = Image.open(file_path)
    new_image = image.resize((200, 200))
    save_path = os.path.join(os.path.dirname(file_path), "resized_image.jpg")
    new_image.save(save_path)
    messagebox.showinfo("Success", f"Image resized successfully! Saved at {save_path}")


def convert_jpg_to_png():
    file_path = filedialog.askopenfilename(filetypes=[("JPG files", "*.jpg")])
    if not file_path:
        return
    img = Image.open(file_path)
    save_path = os.path.join(os.path.dirname(file_path), "converted_image.png")
    img.save(save_path)
    messagebox.showinfo("Success", f"Image converted to PNG! Saved at {save_path}")


def convert_png_to_jpg():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if not file_path:
        return
    img = Image.open(file_path)
    save_path = os.path.join(os.path.dirname(file_path), "converted_image.jpg")
    img.save(save_path)
    messagebox.showinfo("Success", f"Image converted to JPG! Saved at {save_path}")


def compress_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    img = Image.open(file_path)
    myHeight, myWidth = img.size
    img_after_compression = img.resize((myHeight, myWidth))
    save_path = os.path.join(os.path.dirname(file_path), "compressed_image.jpg")
    img_after_compression.save(save_path)
    messagebox.showinfo("Success", f"Image compressed successfully! Saved at {save_path}")


def main():
    root = tk.Tk()
    root.title("Image Converter, Resizer & Compressor")
    root.geometry("400x400")

    tk.Label(root, text="Image Processing Tool", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(root, text="Resize Image", command=resize_image).pack(pady=5)
    tk.Button(root, text="Convert JPG to PNG", command=convert_jpg_to_png).pack(pady=5)
    tk.Button(root, text="Convert PNG to JPG", command=convert_png_to_jpg).pack(pady=5)
    tk.Button(root, text="Compress Image", command=compress_image).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()





                SO FRIENDS , THIS WAS ALL ABOUT MY PROJECT
                THIS PROJECT WILL BE GOING TO UPLOAD IN GITHUB ALSO
                                THANK YOU




