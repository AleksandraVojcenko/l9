from PIL import Image

filename = "so"
with Image.open(filename) as img:
    img.load()

img.show()
width, height = img.size
format = img.mode

print("Ширина", width)
print("Высота", height)
print("Формат", format)
print("Цветовая модель:", mode)

def O2():
    from PIL import Image
    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()
new_img = img.resize((img.width // 3, img.height // 3))
new_img.save("resized_sobaken.jpg")
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.save("image_flipsobaken_top.jpg")
converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
converted_img.save("image_flip_sobaken.jpg")

def O3():
    from PIL import Image, ImageFilter
    filenames = ["1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg"]
    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.EMBOSS)
            new_img.show()
            new_img.save("new_" + file)
