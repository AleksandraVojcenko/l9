from PIL import Image

def k0():
    im = Image.open('8marta.jpg')
    im_crop = im.crop((10, 10, 300, 400))
    im_crop.save('new.jpg')
    im_crop.show()
def k1():
    s = {"8 марта": "8marta.jpg", "1 сентября": "1cen.jpg", "День рождение": "cdr.jpg"}
    g = input("Какой сейчас праздник? ")
    if g in s:
        image = Image.open(s[g])
        image.show()
    else:
        print("Такой открытки нет")

def k2():
    from PIL import Image, ImageDraw, ImageFont

    imechko = input("Введите имя получателя: ")
    filename = "cdr.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("calibri.ttf", 30)
    draw_text = ImageDraw.Draw(img)
    draw_text.text( (img.width // 2 - 100, 15),imechko + "- Ты самое лучшее, что есть в этом мире!",font=font, fill=('yellow'))
    img.show()

k1(), k2()
