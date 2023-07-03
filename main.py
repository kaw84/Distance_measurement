import board
import busio
import adafruit_vl53l0x
import numpy as np

def average():

    while True:
        values = []

        for i in range(10):
            number = vl53.range
            values.append(number)
            time.sleep(0.2)

        # mean of the measurements
        mean = sum(values)/len(values)

        # error in mean
        error = np.std(values)/np.sqrt(len(values))

        # calibration curve measured manually
        y = 1.3112 * mean - 102.63

        # error in y
        error_y = y * error/mean

        # print function
        print(round(y), round(error_y))




