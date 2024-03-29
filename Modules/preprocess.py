from PIL import Image
import numpy as np
import cvlib as cv
from glob import glob
from multiprocessing import Process
import time
import pickle

from Modules.image_shower import image_shower

class preprocess:
    file_list = []
    yolo_res = {}
    i_s = image_shower()

    def update_file_list(self, f_list):
        self.file_list = f_list

    def process(self):
        # save and preprocess
        for idx, f in enumerate(self.file_list):
            d = {}
            if f not in self.yolo_res:
                img = Image.open(f)
                img = self.i_s.resize(img, 720, 720)
                img = np.asarray(img)

                bbox, labels, confidence = cv.detect_common_objects(img)

                d = {
                    'bbox': bbox,
                    'labels': labels,
                    'confidence': confidence,
                    # 'img': img,
                }

            yield (idx, len(self.file_list), f, d)

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

