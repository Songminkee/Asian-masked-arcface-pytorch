from mxnet import recordio
import mxnet as mx
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

def extract_asian_celeb_images(args):
    imgrec = recordio.MXIndexedRecordIO(args.idx_path, args.rec_path, 'r')

    last = 0
    cnt = 0
    for i in range(2830146):
        header, s = recordio.unpack(imgrec.read_idx(i+1))
        img = mx.image.imdecode(s).asnumpy()

        dst = os.path.join(args.write_path,str(int(header.label[0])))
        if not os.path.exists(dst):
            os.makedirs(dst)
            last = int(header.label[0])
            cnt=0


        cv2.imwrite(os.path.join(dst,f'{cnt}.jpg'),cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        cnt+=1

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(descriptions="Extract Asian Celeb")
    parser.add_argument('--idx_path',type=str, help = 'train.idx file path of faces_glintasia' , default='./dataset/faces_glintasia/train.idx')
    parser.add_argument('--rec_path',type=str, help = 'train.rec file path of faces_glintasia' , default='./dataset/faces_glintasia/train.rec')
    parser.add_argument('--write_path',type=str, help = 'Write path of extracted image' , default='./dataset/faces_glintasia/images')
    args = parser.parse_args()

    extract_asian_celeb_images(args)