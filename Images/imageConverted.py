'''
Data Augmentation Script:
As a result of insufficient datasets available online to effectively train our machine learning model,
we have utilised image processing techniques to increase the amount of data for training purposes. 
Through the rotating, altering the brightness and blurring the images, we are able to product our model with
adequate training while not causing our model to overfit through editing these images. Furthermore, this allows
our model to have a higher tolerance when categorising the different types of applesas its use case would be in factories
and supermarkets where there would be varying conditions in angle, lighting and quality of the photo taken.
'''

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

    factor = 0.7 #darkens the image
    im_output = enhancer.enhance(factor)
    im_output.save('darkened' +imageName+ '.png')

    factor = 1.5 #brightens the image
    im_output = enhancer.enhance(factor)
    im_output.save('brightened' +imageName+ '.png')

    #blurs the image
    im_output = im.filter(ImageFilter.GaussianBlur(2))
    im_output.save('GaussianBlur' +imageName+ '.png')
    return

imageGenerator(test.png)
