import os

# [frame number] [identity number] [bbox left] [bbox top] [bbox width] [bbox height] [DET: detection score,
# GT: ignored class flag] [class] [visibility ratio]

data = './video_data/3_gt_fps15.txt'
convert_result = ''
for line in open(data, 'r').readlines():
    frame_number = int(line.split(',')[0].replace('.png', ''))
    identity_number = int(line.split(',')[1])
    bbox_left = int(line.split(',')[2])
    bbox_top = int(line.split(',')[3])
    bbox_width = int(line.split(',')[4])
    bbox_height = int(line.split(',')[5])
    DET_score = -1
    class_id = int(line.split(',')[6])
    visibility_ratio = 0
    tmp_line = '{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}\n'.format(str(frame_number), str(identity_number),
                                                                      str(bbox_left), str(bbox_top), str(bbox_width),
                                                                      str(bbox_height), str(DET_score), str(class_id),
                                                                      str(visibility_ratio))
    convert_result += tmp_line
write_data = open('./video_data/3_gt_fps15_re.txt', 'w')
write_data.write(convert_result)
write_data.close()
print('Convert Finished')
