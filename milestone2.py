from copy import deepcopy
from math import log2

from numpy import uint8

from helper import clamp


def brightening_image(image):
	result = deepcopy(image)
	for i in range(len(result)):
		for j in range(len(result[i])):
			for k in range(len(result[i][j])):
				if k == 3:
					break
				result[i][j][k] = clamp(result[i][j][k] + 50, 0, 255)

	return result

def contrast_stretching(image):
	result = deepcopy(image)

	for i in range(len(result)):
		for j in range(len(result[i])):
			max_i = max(result[i][j])
			min_i = min(result[i][j])
			diff_i = max_i - min_i

			max_o = 255
			min_o = 0
			diff_o = max_o - min_o

			result[i][j][0] = (result[i][j][0] - min_i) * (diff_o // diff_i + min_o)
			result[i][j][1] = (result[i][j][1] - min_i) * (diff_o // diff_i + min_o)
			result[i][j][2] = (result[i][j][2] - min_i) * (diff_o // diff_i + min_o)

	return result

def transformasi_log(image):
	result = deepcopy(image)
	for i in range(len(result)):
		for j in range(len(result[i])):
			for k in range(len(result[i][j])):
				if k == 3:
					break
				result[i][j][k] = uint8(24 * log2(1 + result[i][j][k])) 
	return result

def transformasi_pangkat(image):
	result = deepcopy(image)
	for i in range(len(result)):
		for j in range(len(result[i])):
			for k in range(len(result[i][j])):
				if k == 3:
					break
				result[i][j][k] = uint8(1 * result[i][j][k]**0.67) 
	return result