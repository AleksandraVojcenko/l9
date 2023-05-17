
from PIL import Image, ImageFilter

import os
def l00():
    h = ["1.png","2.jpg","3.png","4.jpg","5.png"]
    count = 0
    for file in h:
        if file.endswith('.jpg') or file.endswith('.png'):
            count += 1
            img = Image.open(file)
            newimg = img.filter(ImageFilter.EMBOSS)
            newimg.show()
            try:
                os.mkdir("C:/python/9.py/")
            except:
                pass
            newimg.save(f"C:/python/new_img{count}.png")

def l0():
    i = 0
    with open('ex.csv', 'r') as f:
        lines = f.readlines()
        print("Список покупок: ")
        for line in lines[1:]:
            product, quantity, price = line.strip().split(',')
            i += int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")
        print(f"Итоговая цена: {i} руб.")

l0()
