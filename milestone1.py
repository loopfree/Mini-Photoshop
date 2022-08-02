from numpy import array, empty, fliplr, flipud, ndarray, resize, rot90, uint8
from copy import deepcopy

def negatif(image):
    result = deepcopy(image)

    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j][0] = 255 - result[i][j][0]
            result[i][j][1] = 255 - result[i][j][1]
            result[i][j][2] = 255 - result[i][j][2]

    return result

def grayscale(image):
    result = deepcopy(image)

    for i in range(len(result)):
        for j in range(len(result[i])):
            avg = (0.299 * result[i][j][0] + 0.587 * result[i][j][1] + 0.144 * result[i][j][2])
            result[i][j][0] = uint8(avg) 
            result[i][j][1] = uint8(avg) 
            result[i][j][2] = uint8(avg)

    return result

def komplemen(image):
    result = deepcopy(image)

    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j][0] = 255 - result[i][j][0]
            result[i][j][1] = 255 - result[i][j][1]
            result[i][j][2] = 255 - result[i][j][2]

    return result

def rot_left(image):
    result = resize(image, (len(image[0]), len(image), len(image[0][0])))
    for i in range(len(image[0])):
        for j in range(len(image)):
            for k in range(len(image[j][i])):
                result[i][j][k] = image[j][i][k]

    return result

def rot_right(image):
    result = resize(image, (len(image[0]), len(image), len(image[0][0])))
    
    row_count = len(image) - 1
    col_count = len(image[0]) - 1

    for i in range(len(image[0])):
        for j in range(len(image)):
            for k in range(len(image[j][i])):
                result[i-col_count][j-row_count][k] = image[j][i][k]

    return result

def flip_left_right(image):
    result = deepcopy(image)

    col_count = len(result[0]) - 1

    for i in range(len(result)):
        for j in range(len(result[i])//2):
            temp = deepcopy(result[i][j])
            result[i][j] = deepcopy(result[i][col_count-j])
            result[i][col_count-j] = temp

    return result

def flip_up_down(image):
    result = deepcopy(image)

    row_count = len(result) - 1

    for i in range(len(result)//2):
        for j in range(len(result[i])):
            temp = deepcopy(result[i][j])
            result[i][j] = deepcopy(result[row_count-i][j])
            result[row_count-i][j] = temp

    return result

def zoom_in(image):
    result = resize(image, (len(image)//2, len(image[0])//2, len(image[0][0])))

    m = 0
    n = 0
    for i in range(len(result)):
        n = 0
        for j in range(len(result[i])):
            for k in range(len(result[i][j])):
                if k == 3:
                    break
                count = 0
                total = 0
                if m < len(image) and n < len(image[m]):
                    total += int(image[m][n][k])
                    count += 1
                if m < len(image) and n+1 < len(image[m]):
                    total += int(image[m][n+1][k])
                    count += 1 
                if m+1 < len(image) and n+1 < len(image[m+1]):
                    total += int(image[m+1][n][k])
                    count += 1
                if m+1 < len(image) and n+1 < len(image[m]):
                    total += int(image[m+1][n+1][k])
                    count += 1 
                if count != 0:
                    avg = total // count
                    result[i][j][k] = uint8(avg)
            n += 2
        m += 2 
    return result

def zoom_out(image):
    result = resize(image, (len(image)*2, len(image[0])*2, len(image[0][0])))
    print(len(image) * 2)

    m = 0
    n = 0
    for i in range(len(image)):
        n = 0
        for j in range(len(image[0])):
            if m >= len(image) or n >= len(image[0]):
                continue
            result[m][n] = image[i][j]
            result[m][n+1] = image[i][j]
            result[m+1][n] = image[i][j]
            result [m+1][n+1] = image[i][j]
            n += 2
        m += 2

    print(m)

    return result
