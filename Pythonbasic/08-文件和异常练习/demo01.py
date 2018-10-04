#使用Python编写一个程序，打印出图片文件的分辨率
def imgres(file_name):
    with open(file_name, 'rb') as img:
        img.seek(163)
        x=img.read(2)
        h=(x[0]<<8)+x[1]
        x=img.read(2)
        w=(x[0]<<8)+x[1]
        print("Resolution = ",w,'X',h)

imgres('E:/Python/demo/python/微信图片_20171102183931.jpg')
imgres('E:/Python/demo/python/IMG_李蒙蒙.jpg')