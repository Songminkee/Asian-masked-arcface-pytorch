import os
import glob
import numpy as np 

def make_mask_txt(args):
    root_path = [args.img_path]+args.mask_img_path

    with open(f'{args.dataset_name}_all.txt','w') as f:
        for root in root_path:
            folders = glob.glob(os.path.join(root,'*'))
            print(folders)
            for folder in folders:
                images  = glob.glob(os.path.join(folder,'*'))
                for img in images:
                    f.writelines(img+'\n')

    f = open(f'{args.dataset_name}_all.txt','r')
    lines = np.array(f.readlines())

    np.random.shuffle(lines)

    val_len = int(len(lines)*args.ratio)
    test_len = val_len
    val = lines[:val_len]
    train = lines[val_len:]

    with open(f'{args.dataset_name}_train.txt','w') as f:
        for t in train:
            f.writelines(t)

    with open(f'{args.dataset_name}_val.txt','w') as f:
        for v in val:
            f.writelines(v)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Extract Asian Celeb")
    parser.add_argument('--img_path',type=str, help = 'The path of original image path' , default='./dataset/faces_glintasia/images')
    parser.add_argument('--mask_img_path',type=str, nargs='+',help = 'The path of masked image path' , default=['./dataset/faces_glintasia/images_masked'])
    parser.add_argument('--dataset_name',type=str, help = 'Name of your dataset' , default='asian')
    parser.add_argument('--ratio',type=float, help = 'Ratio of validation dataset' , default=0.3)
    args = parser.parse_args()
    print(args.mask_img_path)
    #make_mask_txt(args)