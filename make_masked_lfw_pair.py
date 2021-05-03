import os


def make_masked_lfw_pair(args):
    f = open(args.lfw_test_pair,'r')
    lines = f.readlines()
    f.close()

    with open( os.path.join(args.dst_root,'lfw_test_mask_pair.txt'),'w') as f:
        for line in lines:
            fig1,fig2,_ = line.split()
            fig1 = os.path.join(args.maksed_lfw_path,fig1)
            fig2 = os.path.join(args.maksed_lfw_path,fig2)
            if not os.path.exists(fig1) or not os.path.exists(fig2):
                continue
            f.writelines(line)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(descriptions="Extract Asian Celeb")
    parser.add_argument('--lfw_test_pair',type=str, help = 'The path of lfw_test_pair' , default='./lfw_test_pair.txt')
    parser.add_argument('--maksed_lfw_path',type=str, help = 'The path of masked image path' , default='./dataset/128_masked/')
    parser.add_argument('--dst_root',type=str, help = 'folder of dst txt file' , default='./dataset')
    args = parser.parse_args()

    make_mask_txt(args)