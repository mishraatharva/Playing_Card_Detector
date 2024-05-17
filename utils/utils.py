import base64


# def decodeImage(imgstring, fileName):
#     imgdata = base64.b64decode(imgstring)
#     with open("./"+fileName, 'wb') as f:
#         f.write(imgdata)
#         f.close()


# def encodeImageIntoBase64(croppedImagePath):
#     with open(croppedImagePath, "rb") as f:
#         return base64.b64encode(f.read())
    
class ImageProcessing:
    def __init__(self):
        pass

    def decodeImage(self,imgstring,filename):
        imagedata=  base64.b64decode(imgstring)
        with open("./"+filename,'wb') as f:
            f.write(imagedata)

    def encodeImageIntoBase64(self,croppedImagePath):
        with open(croppedImagePath, "rb") as f:
            return base64.b64encode(f.read())