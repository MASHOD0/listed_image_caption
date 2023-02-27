"""
The command line interface for using the model.
"""
from Model import predict
import os
import time

path = r"C:\Users\mashh\Documents\git\listed_image_caption\inputs"
image_file_format = ['.png', '.jpg', '.jpeg']

if __name__ == '__main__':

    print("store the files in the inputs folder")
    num_return_sequences = int(input("enter the number of return sequences:"))

    start = time.time()

    for (root, dirs, file) in os.walk(path):
        for f in file:

            if '.png' or '.jpg' or '.jpeg' in f:

                image = os.path.join(root, f)
                print(f'filename : {f}')
                results = predict(image, num_return_sequences)

    end = time.time()

    print(f'execution time: {end - start}')