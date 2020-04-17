from PIL import Image
import pytesseract
import argparse
import cv2
import os

def tesseract_ocr(image_name, preprocess, showFlag):
    """ Application of tesseract on image
    :param: string: image_name: Specifies name of the image
    :param: string: preprocess: Specifies the preprocessing options [Default: thresh]
    :param: Bool: showFlag: Specifies if the processed image should be shown. [Default: False]
    """

    print(f"image_name: {image_name}")
    # load the example image and convert it to grayscale
    image = cv2.imread(image_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # apply thresholding
    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # median blurring for noise removal
    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary 
    # file so we can apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)

    # Shows the output images if desired
    if showFlag:
        cv2.imshow("Image", image)
        cv2.imshow("Output", gray)
        cv2.waitKey(0)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="Specifies the path of a given input image")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                    help="Specifies the type of preprocessing that is conducted. Default is Threshholding.")
    ap.add_argument("-s", "--show", type=bool, default=False,
                    help="Specifies if the processed image should be shown or not. Default is False")
    args = vars(ap.parse_args())

    if (args["image"][-3:] == "png"): 
        tesseract_ocr(args["image"], args["preprocess"], args["show"])
    else: 
        print("Please only enter images in .png format.")

    