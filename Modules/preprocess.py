from PIL import Image
import numpy as np
import cvlib as cv
from glob import glob
from multiprocessing import Process
import time

class preprocess:
    file_list = []
    yolo_res = {}

    def update_file_list(self, f_list):
        self.file_list = f_list

    def process(self):
        # save and preprocess
        for idx, f in enumerate(self.file_list):
            if f not in self.yolo_res:
                img = np.asarray(Image.open(f))
                bbox, labels, confidence = cv.detect_common_objects(img)

                d = {
                    'bbox': bbox,
                    'labels': labels,
                    'confidence': confidence,
                    'img': img,
                }

                self.yolo_res[f] = d

            yield (idx, len(self.file_list))

def f(p):
    for i in p.process():
        print(i)

if __name__ == '__main__':
    pp = preprocess()
    pp.update_file_list(glob('../pictures\*.*'))


    # test in new process


    p = Process(target=f, args=(pp,))
    p.start()

    while True:
        print('lalala')
        time.sleep(1)

