from PIL import Image

def image2txt():
    image = Image.open("01.png")
    zom = image.size[0]/image.size[1]
    # print(zom)
    image_out = image.convert("L").resize((int(300*zom),int(300)))# 表示灰色,resize重定义图片大小
    # image_out.show()
    width, height = image_out.size
    print(image_out.size)

    texts = ""
    asciis = "%#&^@$.* "

    for i in range(height):
        for j in range(width):
            pixel = image_out.getpixel((j,i))
            texts += asciis[int(pixel / 255 * 8)]
        texts += "\n"
    with open("01.txt","w") as f:
        f.write(texts)

if __name__=='__main__':
    image2txt()