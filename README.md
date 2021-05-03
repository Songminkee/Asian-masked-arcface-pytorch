# Train with masked Asian-Celeb
- #### Step 1
  - Download [Asian-Celeb Dataset](https://github.com/deepinsight/insightface/wiki/Dataset-Zoo)
- #### Step 2
  - Extract image
  ```bash
  python extract_asian_celeb.py --idx_path [train.idx file] --rec_path [train.rec file] --write_path [dst path]
  ```
- #### Step 3
  - Make masked asian celen data
  ```bash
  cd MaskTheFace
  python mask_the_face.py --path [dst path in Step2]
  ``` 
- #### Step 4
  - Make dataset txt
  ```bash
  python make_mask_txt.py --img_path [dst_path in Step2] --mask_img_path [result path in Step 3]
  ```
- #### Step 5
  - train
  ```bash
  python train.py
  ```

<br>

# Test with masked lfw test dataset
- #### Step1
  - Download [lfw](https://pan.baidu.com/s/1tFEX0yjUq3srop378Z1WMA ) pwd : b2ec
- #### Step2
  - Make masked lfw
  ```bash
  cd MaskTheFace
  python mask_the_face.py --path [lfw dataset path]
  ```
- #### Step3
  - Make pair of lfw
  ```bash
  python make_masked_lfw_pair.py --lwf_test_pair [Path of lfw_test_pair.txt] --masked_lfw_path [result path of in Step2] --dst_root [dst path of result txt file]
  ```
- #### Step4
  - change `lfw_root`, `lfw_test_list` in `cofing/config.py`

- #### Step5
  - test
  ```bash
  python test.py
  ```

<br>

# Pretrained weight with Make masked asian celen data
- #### [DownLoad Link](https://drive.google.com/drive/folders/13Mp6qz9E9L3Z3C9ScKxcOytc2j6cK079)

<br>

# References
- https://github.com/ronghuaiyang/arcface-pytorch

- https://github.com/aqeelanwar/MaskTheFace

<br>

# pretrained model and lfw test dataset in (original repository)[https://github.com/ronghuaiyang/arcface-pytorch]
the pretrained model and the lfw test dataset can be download here. link: https://pan.baidu.com/s/1tFEX0yjUq3srop378Z1WMA pwd: b2ec
the pretrained model use resnet-18 without se. Please modify the path of the lfw dataset in config.py before you run test.py.
