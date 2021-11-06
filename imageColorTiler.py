import cv2 as cv
import numpy as np

# TODO Make these variables bash arguments 
columns = 10
rows =  1
path = './example/example.jpg'

# Get image from the specified file path
img = cv.imread(cv.samples.findFile(path))

# Get the image metadata
height, width, channels = img.shape

# Get the number of pixels needed per rows and per columns
rowsCount = height//rows
columnsCount = width//columns

# Get the number of rows and columns that'll need an additional pixel
rowsOffset = height%rows
columnsOffset = width%columns

# Init rows start values
rowStart = 0
rowEnd = rowsCount

# TODO Add a loading in bash ?

for row in range(rows):
    columnStart = 0
    columnEnd = columnsCount

    if (rowsOffset > row): rowEnd += 1

    for column in range(columns):
        if (columnsOffset > column): columnEnd += 1

        # Get the region of the image(ROI) by row and column
        imgCell = img[rowStart:rowEnd, columnStart:columnEnd]

        # Flatten the ROI by its colors and get their respective count
        colors, count = np.unique(imgCell.reshape(-1, channels), axis=0, return_counts=True)

        # Get the color having the most occurences (making it the most dominant one)
        dominantColor = colors[count.argmax()]

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

# TODO Add instruction on leaving file

cv.imshow("image", img)
cv.waitKey()
