# DLCV Final Project ( Visual Queries 2D Localization Task )

# 環境
* python=3.8
* conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.6 -c pytorch -c conda-forge
* pip install -r requirement.txt

# How to run your code?
* 前置作業：
    *  進入VQLoC資料夾
    *  到[這裡](https://utexas.box.com/shared/static/3j3q9qsc1kovpwfxtnsful7pvdy234q6.tar)下載pretrained weight
    * 建立放資料的資料夾(下稱data path)，裡面要有vq_val.json, vq_train.json, vq_test_unannotated.json, clips(放clip的資料夾)
    * 執行：python3 test.py {data path}
    * 至以下檔案改路徑
        * inference_predict.py 124行，將 "/data/jason/DLCV_vq2d_data" 改成 data path
        * inference_result.py 151行，將 "/data/jason/DLCV_vq2d_data" 改成 data path
        * dataset/base_dataset.py 33行開始，將 "/data/jason/DLCV_vq2d_data" 改成 data path；將 "/data/jason/DLCV_vq2d_dataclips" 改成 data path/clips
        * evaluation/task_inference_predict.py 28行，將 "/data/jason/DLCV_vq2d_dataclips" 改成 data path/clips
        * evaluation/task_inference_result.py 43行，將 "/data/jason/DLCV_vq2d_dataclips" 改成 data path/clips
        * 至config/eval.yaml 40行，將ckpt path修改成pretrained weight路徑
    
* TODO: Please provide the scripts for TAs to reproduce your results, including training and inference.

```
# train script:
bash train.sh
# inference script
bash inference_predict.sh
python3 inference_result.py --cfg config/eval.yaml --eval
```
可以在 output/ego4d_vq2d/eval/eval裡面看到json檔，這是我們的輸出
裡面的bash檔都使用四顆GPU訓練，可以把他們改成其他除了1以外的數量

