import cv2
import pytesseract
from PIL import Image
import easyocr
import imutils



PICA_PATH = '/home/gordon-workspace/local_workspace/experiment_ground/Adonis_Akl_16.4.2021_13.57_out.jpg'
PICB_PATH = '/home/gordon-workspace/local_workspace/experiment_ground/Adonis_Akl_19.4.2021_14.04_out.jpg'

PIC_1 = '/media/sf_BLOB_STORAGE/boomgate_weekly/2.jpg'

img = cv2.imread(PIC_1)

img = cv2.cvtColor(img, cv2.COLOR_)

# Noise reduction 

bfilter = cv2.bilateralFilter(img,11,17,17)
edged = cv2.Canny(bfilter, 30, 200)


cv2.imshow('Result', img)

cv2.waitKey(0)

print(pytesseract.image_to_string(img))

# print(pytesseract.image_to_string(Image.open(PIC_1)))








































# pytesseract
    # .image_to_data
    # .image_to_string

# cv2 

# img = cv2.imread(PICA_PATH,0)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# sct = cv2()
# # print(pytesseract.image_to_boxes(Image.open(PICA_PATH)))

# sct.imshow('testing', PICA_PATH)

# if waitKey:
#     sct.waitKey(0)

# # We import the necessary packages
# #import the needed packages

  
# #We then Construct an Argument Parser
# ap=argparse.ArgumentParser()
# ap.add_argument("-i","--image",
#                 required=True,
#                 help="Path to the image folder")
# ap.add_argument("-p","--pre_processor",
#                 default="thresh", 
#                 help="the preprocessor usage")
# args=vars(ap.parse_args())
  
# #We then read the image with text
# images=cv2.imread(args["image"])
  
# #convert to grayscale image
# gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
  
# #checking whether thresh or blur
# if args["pre_processor"]=="thresh":
#     cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
# if args["pre_processor"]=="blur":
#     cv2.medianBlur(gray, 3)
      
# #memory usage with image i.e. adding image to memory
# filename = "{}.jpg".format(os.getpid())
# cv2.imwrite(filename, gray)


# text = pytesseract.image_to_string(Image.open(filename))


# os.remove(filename)
# print(text)
  
# # show the output images
# cv2.imshow("Image Input", images)
# cv2.imshow("Output In Grayscale", gray)
# cv2.waitKey(0)

