import numpy as np
import matplotlib.pyplot as plt
import time
import PIL
from PIL import Image
from collections import Counter

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
    iar = np.array(i)
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
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr

if __name__ == '__main__':

    whatNumIsThis('images/test2.png')
