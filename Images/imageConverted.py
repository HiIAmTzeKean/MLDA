from PIL import Image, ImageEnhance, ImageFilter

def imageGenerator(imageName):
    #read the image
    im = Image.open(imageName + ".png")
    #image brightness enhancer
    enhancer = ImageEnhance.Brightness(im)

    #--------------------- Rotate image ---------------
    rotated60 = im.rotate(60)
    rotated60.save(imageName + "60" + ".png")

    rotated120  = im.rotate(120)
    rotated120.save(imageName + "120" + ".png")

    rotated1180  = im.rotate(180)
    rotated1180.save(imageName + "180" + ".png")

    rotated240  = im.rotate(240)
    rotated240.save(imageName + "240" + ".png")

    rotated300  = im.rotate(300)
    rotated300.save(imageName + "300" + ".png")
    #------------------------------------------------------

    factor = 1 #gives original image
    im_output = enhancer.enhance(factor)
    im_output.save('enhanced' + imageName + '.png')

    factor = 0.9 #darkens the image
    im_output = enhancer.enhance(factor)
    im_output.save('darkened' +imageName+ '.png')

    factor = 1.5 #brightens the image
    im_output = enhancer.enhance(factor)
    im_output.save('brightened' +imageName+ '.png')

    im_output = im.filter(ImageFilter.GaussianBlur(2))
    im_output.save('GaussianBlur' +imageName+ '.png')
    return

imageGenerator("test")