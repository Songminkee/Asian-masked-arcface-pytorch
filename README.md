# Dataset
- #### Step 1
  - Download [Asian-Celeb Dataset](https://github.com/deepinsight/insightface/wiki/Dataset-Zoo)
- #### Step 2
  - Extract image
  ```bash
  python extract_asian_celeb.py --idx_path [train.idx file] --rec_path [train.rec file] --write_path [dst_path]
  ```

# References
https://github.com/deepinsight/insightface

https://github.com/auroua/InsightFace_TF

https://github.com/MuggleWang/CosFace_pytorch

# pretrained model and lfw test dataset
the pretrained model and the lfw test dataset can be download here. link: https://pan.baidu.com/s/1tFEX0yjUq3srop378Z1WMA pwd: b2ec
the pretrained model use resnet-18 without se. Please modify the path of the lfw dataset in config.py before you run test.py.
