from copy import deepcopy
from math import ceil, sqrt
from numpy import array, exp, fft, matmul, meshgrid, ndarray, real, resize, square, uint8 

def gaus(mat_l,sigma):
    e = 2.71828182845904
    pi = 3.1415926535897
    Matrix = [[0.0 for x in range(mat_l)] for y in range(mat_l)] 
    for x in range(-(int(mat_l/2)),(int(mat_l/2))+1):
        for y in range(-(int(mat_l/2)),(int(mat_l/2))+1):
            ee = pow(e,(-(((pow(x,2)+pow(y,2))/(2*(pow(sigma,2)))))))
            aa = (1/(2*pi*pow(sigma,2)))
            result = ee*aa
            Matrix[x+int(mat_l/2)][y+int(mat_l/2)] = round(result,6)

    temp_sum: float = 0
    for m in Matrix:
        for n in m:
            temp_sum += n

    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            Matrix[i][j] = Matrix[i][j] / temp_sum

    return Matrix

def matrix_convolve(image,kernel, mul=1):
    img_x, img_y = (image.shape[0], image.shape[1])
    kernel_x, kernel_y = kernel.shape
    a, b = (kernel_x // 2, kernel_y // 2)

    result = deepcopy(image)
    for i in range(img_x):
        for j in range(img_y):
            for k in range(len(image[i, j])):
                if k == 3:
                    break
                summ = 0
                for s in range(-a,a+1):
                    if i+s < 0 or i+s >= img_x:
                        continue
                    for t in range(-b,b+1):
                        if j+t < 0 or j+t >= img_y:
                            continue
                        summ += kernel[s+a,t+b] * image[i+s,j+t, k]
                result[i, j, k] = ceil(mul*summ)
    return result

def gaussian_blur(image):
    sigma = 2
    sample = 1 + 2 * ceil(sigma * 3)
    print("Creating Gaus Kernel")
    kernel = gaus(sample, sigma)
    kernel = array([i for i in kernel])

    print("Finishing Gaussian Blur")
    return matrix_convolve(image,kernel,1)

def sharpening(image):
    #w stands for width
    #h stands for height
    #c stands for color
    result = deepcopy(image)

    og_w, og_h, og_c = image.shape

    padded_image = resize(image, (og_w*2, og_h*2, og_c))

    padded_w, padded_h, padded_c = padded_image.shape

    #seperate image into r and g and b channels

    red_chan = ndarray((og_w*2, og_h*2))
    green_chan = ndarray((og_w*2, og_h*2))
    blue_chan = ndarray((og_w*2, og_h*2))

    for i in range(padded_w):
        for j in range(padded_h):
            for k in range(padded_c):
                if k == 3:
                    break
                if i > og_w or j > og_h:
                    padded_image[i, j, k] = uint8(0)
                if k == 0:
                    red_chan[i, j] = padded_image[i, j, k]
                elif k == 1:
                    green_chan[i, j] = padded_image[i, j, k]
                elif k == 2:
                    blue_chan[i, j] = padded_image[i, j, k]
    
    red_fourier = fft.fft2(red_chan)
    green_fourier = fft.fft2(green_chan)
    blue_fourier = fft.fft2(blue_chan)

    D0 = 0.05 * padded_w

    u = [i for i in range(padded_w)]
    v = [i for i in range(padded_h)]

    for (index, elem) in enumerate(u):
        if elem > padded_w // 2:
            u[index] -= padded_w

    for (index, elem) in enumerate(v):
        if elem > padded_h // 2:
            v[index] -= padded_h
    
    V, U = meshgrid(v, u)

    x, y = V.shape

    D = deepcopy(V)

    for i in range(x):
        for j in range(y):
            D[i, j] = sqrt(V[i, j]**2 + U[i, j]**2)

    H = exp(-(square(D)) // (2 * D0**2))

    H = 1 - H

    red_LPF = H * red_fourier
    green_LPF = H * green_fourier
    blue_LPF = H * blue_fourier

    red_HPF = real(fft.ifft2(red_LPF))
    green_HPF = real(fft.ifft2(green_LPF))
    blue_HPF = real(fft.ifft2(blue_LPF))

    for i in range(og_w):
        for j in range(og_h):
            result[i, j, 0] = red_HPF[i, j]
            result[i, j, 1] = green_HPF[i, j]
            result[i, j, 2] = blue_HPF[i, j]

    return result