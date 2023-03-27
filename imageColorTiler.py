import cv2 as cv
import numpy as np
import sys


def getBySortingPixels (img):
    # Get the region of the image(ROI) by row and column
    imgCell = img[rowStart:rowEnd, columnStart:columnEnd]

    # Flatten the ROI by its colors and get their respective count
    colors, count = np.unique(imgCell.reshape(-1, channels), axis=0, return_counts=True)

    # Get the color having the most occurences (making it the most dominant one)
    return colors[count.argmax()]

def getByKmeans (img):
        pixels = np.float32(img.reshape(-1, 3))

        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 200, .1)
        flags = cv.KMEANS_RANDOM_CENTERS

        _, labels, palette = cv.kmeans(pixels, 1, None, criteria, 10, flags)
        _, counts = np.unique(labels, return_counts=True)

        return palette[np.argmax(counts)]


# Get the command line arguments
try:
    path = sys.argv[1]
    columns = int(sys.argv[2])
    rows = int(sys.argv[3])    
except ValueError:
    print('Missing argument: <path> <columns> <rows>')
    exit()

# Get image from the specified file path
img = cv.imread(cv.samples.findFile(path))

# Get the image metadata
height, width, channels = img.shape

if (columns <= 0 or columns > width):
    print('Can\'t have no columns or more columns tiles as the image pixel width')
    print('Image dimensions(WxH): ', width, 'x', height)
    exit()

if (rows <= 0 or rows > height):
    print('Can\'t have no rows or more rows tiles as the image pixel height')
    print('Image dimensions(WxH): ', width, 'x', height)
    exit()

# Get the number of pixels needed per rows and per columns
rowsCount = height//rows
columnsCount = width//columns

# Get the number of rows and columns that'll need an additional pixel
rowsOffset = height%rows
columnsOffset = width%columns

# Init rows start values
rowStart = 0
rowEnd = rowsCount

for row in range(rows):
    columnStart = 0
    columnEnd = columnsCount

    if (rowsOffset > row): rowEnd += 1

    for column in range(columns):
        if (columnsOffset > column): columnEnd += 1

        dominantColor = getBySortingPixels(img)
        #dominantColor = getByKmeans(img)

        # Replace the ROI in the image by its dominant color
        img[rowStart:rowEnd, columnStart:columnEnd] = np.full((rowEnd - rowStart, columnEnd - columnStart, 3), dominantColor)

        # Set column values for next iteration
        columnStart = columnEnd
        columnEnd += columnsCount
        if (columnEnd > width): columnEnd = width

    # Set row values for next iteration
    rowStart = rowEnd
    rowEnd += rowsCount
    if (rowEnd > height): rowEnd = height

print('Press any key to leave the image...')

cv.imshow('image', img)
cv.waitKey()
