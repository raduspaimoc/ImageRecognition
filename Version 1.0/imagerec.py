import numpy as np
import matplotlib.pyplot as plt
import time
import cv2
import PIL
from PIL import Image
from collections import Counter
from resizeimage import resizeimage


# def image_copy(image_array):
#     image_copy = np.copy(image_array)
#     vis_util.visualize_boxes_and_labels_on_image_array(
#         image_copy,
#         np.squeeze(boxes),
#         np.squeeze(classes).astype(np.int32),
#         np.squeeze(scores),
#         category_index,
#         use_normalized_coordinates=True,
#         line_thickness=8)
#     return image_copy

def whatNumIsThis(filepath):
    matchedAr = []

    loadExamps = open('numArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filepath)
    i = i.convert('L')
    iar = np.array(i)
    #iar = threshold(iar)
    iarl = iar.tolist()

    inQuestion = str(iarl)
    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x=0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x += 1

    print matchedAr
    x = Counter(matchedAr)
    print x

    graphX = []
    graphY = []
    for eachThing in x:
        print eachThing
        graphX.append(eachThing)
        print x[eachThing]
        graphY.append(x[eachThing])

    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4), (0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4), (1,0), rowspan=3, colspan=4)

    ax1.imshow(iar)
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(300)
    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    plt.show()

def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersWeHave = range(0, 10)
    versionsWeHave = range(1, 10)

    for eachNum in numbersWeHave:
        for eachVersion in versionsWeHave:
            imageFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVersion) + '.png'
            ei = Image.open(imageFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())

            lineToWrite = str(eachNum) + '::' + eiar1 + '\n'
            numberArrayExamples.write(lineToWrite)

def threshold(imageArray):

    balanceAr = []
    newAr = imageArray
    from statistics import mean
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:len(eachPix)-1])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:len(eachPix)-1]) > balance:
                for i in range(0, len(eachPix)):
                    eachPix[i] = 255

                #eachPix[0] = 255
                #eachPix[1] = 255
                #eachPix[2] = 255
                #eachPix[3] = 255
            else:
                for i in range(0, len(eachPix) - 1):
                    if i == len(eachPix):
                        eachPix[i] = 255
                    else:
                        eachPix[i] = 0
                # eachPix[0] = 0
                # eachPix[1] = 0
                # eachPix[2] = 0
                # eachPix[3] = 255
    return newAr

if __name__ == '__main__':

    #imageFilePath = 'test.png'
    #imageFilePath = 'images/numbers/0.1.png'

    # imageFilePath = 'images/numbers/3.6.png'
    # ei = Image.open(imageFilePath)
    # ei = ei.convert('L')
    # #ei = ei.convert('RGB')
    # eiar = np.array(ei)
    # eiar.tolist()
    # print eiar
    #
    # print('\n' + '-----------------------' + '\n')

    imageFilePath = 'test.png'
    ei = Image.open(imageFilePath)
    ei = ei.convert('L')
    #ei = ei.convert('RGB')
    eiar = np.array(ei)
    eiar.tolist()
    list = []
    for row in eiar:
        aux = []
        for number in row:
            if number < 200:
                aux.append(0)
            else:
                aux.append(255)
        list.append(aux)
    eiar = list
    print eiar
    print('\n' + '-----------------------' + '\n')
    numbersWeHave = range(0, 10)
    versionsWeHave = range(1, 10)

    matchedAr = []
    for eachNum in numbersWeHave:
        for eachVersion in versionsWeHave:
            imageFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVersion) + '.png'
            ei = Image.open(imageFilePath)
            ei = ei.convert('L')
            eiar1 = np.array(ei)
            #eiar1 = str(eiar.tolist())
            #print("Num: 3 version: ", eachVersion)
            #print eiar1

            y = 0
            x = 0
            #print x , "x i :. ", len(eiar1)
            while x < len(eiar1):
                y = 0
                while y < 8:
                    #print "comparing:::", eiar1[x][y], " with: ", eiar[x][y]
                    if eiar1[x][y] == eiar[x][y]:
                        matchedAr.append(int(eachNum))
                    y += 1
                x += 1

    print matchedAr
    x = Counter(matchedAr)
    print x
    #whatNumIsThis('test.png')

    # Step 1 ===> Convert image to black and white
    # originalImage = cv2.imread('images-to-resize/numred3.jpg')
    # grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    # (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    #
    # cv2.imshow('Black white image', blackAndWhiteImage)
    # cv2.imwrite("image_processed.png", blackAndWhiteImage)

    # Step 2 ===> Resize image to 8x8px
    # fd_img = open('image_processed.png')
    # img = Image.open(fd_img)
    # img = resizeimage.resize_thumbnail(img, [8, 8], resample=Image.LANCZOS)
    # img.save('test.png', 'png')


    #cv2.imshow('Original image',originalImage)
    #cv2.imshow('Gray image', grayImage)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # img = Image.open(fd_img)
    # img = resizeimage.resize_thumbnail(img, [8, 8], resample=Image.LANCZOS)
    # #img = resizeimage.resize_cover(img, [8, 8])
    # img.save('test.png', 'png')
    # fd_img.close()
    # whatNumIsThis('test.png')
