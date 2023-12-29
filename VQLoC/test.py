import os
import sys
import decord
import numpy as np
import json
import imageio

def cut_query(clip_path, anno, query_path):
    video_reader = decord.VideoReader(clip_path, num_threads=1)
    visual_crop = anno['visual_crop']
    frame_number = visual_crop['frame_number']
    x, y = visual_crop['x'], visual_crop['y']
    width, height = visual_crop['width'], visual_crop['height']
    ori_width, ori_height = visual_crop['original_width'], visual_crop['original_height']

    frame = video_reader[frame_number].asnumpy()
    
    query = frame[y:y+height, x:x+width]
    # query = frame[x:x+width, y:y+height]
    imageio.imwrite(query_path, query)

def get_query_path(clip_name, data_dir, sample):

    image_name = int(sample["frame_number"])# "{}/frame_{:07d}.jpg"
    image_path = os.path.join(data_dir, 'images_hw', "{}/frame_{:07d}.jpg".format(clip_name, image_name + 1))
    return image_path

def main():
    data_dir = sys.argv[1]
    with open(os.path.join(data_dir, 'vq_val.json'), 'r') as f:
        anno = json.load(f)
    tmp_dict = dict()
    for clip_name, v in anno.items():
        clip_path = os.path.join(data_dir, 'clips', clip_name+'.mp4')
        clip_anno = v['annotations'][0]
        query_set = clip_anno['query_sets']
        os.makedirs(os.path.join(data_dir, 'images_hw', clip_name), exist_ok=True)
        for n, q_anno in query_set.items():
            if not q_anno['is_valid']:
                continue
            tmp_dict = dict()
            visual_crop = q_anno['visual_crop']
            query_path = get_query_path(clip_name, data_dir, visual_crop)
            tmp_dict['visual_crop'] = visual_crop
            # print(clip_path)
            # print(query_path)
            cut_query(clip_path, tmp_dict, query_path)

if __name__ == '__main__':
    main()

