 # This file will write the true annotations to a txt file named 'image_annotation'
 # In the txt, the format should be
 # path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
 # path/to/img2.jpg 120,300,250,600,2
import os
from PIL import Image,ImageDraw

####
#### Read/Create files
####

# read images/bounding boxes
# this file is to save augmented data
train_path = '/home/qingyang/aiator/data/location_images/train'
val_path = '/home/qingyang/aiator/data/location_images/val'
annotation_path_train = '/home/qingyang/aiator/data/image_annotation_train.txt'
annotation_path_val = '/home/qingyang/aiator/data/image_annotation_val.txt'
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
# create new file
f_train = open(annotation_path_train, "x")
f_train = open(annotation_path_train, "a")

f_val = open(annotation_path_val, "x")
f_val = open(annotation_path_val, "a")

# read loaction file
l_f = open('/home/qingyang/aiator/data/location_images/targetLocation.csv','r')

####
#### initialize center_coordinate
####

# first line is headings
# TODO: hard_code for line_nb 105
line_nb = 105
center_coordinate = []
for cnt in range(line_nb):
    if cnt > 0:
        center_coordinate.append(list(map(float,l_f.readline().strip().split(","))))
    else:
        center_coordinate.append(list(map(str, l_f.readline().strip().split(","))))

# TODO: row_size and col_size hard-code
def c2b(x, y, row_size = 1624, col_size = 1236, x_offset = 150, y_offset = 30):

    ## center to bounding box(x_min,x_max,y_min,y_max)
    x_min = max(x - x_offset, 0)
    x_max = min(x + x_offset, row_size)
    y_min = max(y - y_offset, 0)
    y_max = min(y + y_offset, col_size)
    return (int(x_min),int(x_max),int(y_min),int(y_max))


#
for cnt in range(1,91):
    temp_path = os.path.join(train_path,str(cnt)+'.bmp')
    temp_coordinate = center_coordinate[cnt]

    x_1 = temp_coordinate[0]
    y_1 = temp_coordinate[1]
    x_2 = temp_coordinate[2]
    y_2 = temp_coordinate[3]
    x_1_min,x_1_max,y_1_min,y_1_max = c2b(x_1,y_1)
    x_2_min,x_2_max,y_2_min,y_2_max = c2b(x_2,y_2)
    content_1 = temp_path+' '+str(x_1_min)+','+str(y_1_min)+','+str(x_1_max)+','+str(y_1_max)+','+str(0)+' '+str(x_2_min)+','+str(y_2_min)+','+str(x_2_max)+','+str(y_2_max)+','+str(0)+'\n'
    f_train.write(content_1)


for cnt in range(101,105):
    temp_path = os.path.join(train_path,str(cnt)+'.bmp')
    temp_coordinate = center_coordinate[cnt]

    x_1 = temp_coordinate[0]
    y_1 = temp_coordinate[1]
    x_2 = temp_coordinate[2]
    y_2 = temp_coordinate[3]
    x_1_min,x_1_max,y_1_min,y_1_max = c2b(x_1,y_1)
    x_2_min,x_2_max,y_2_min,y_2_max = c2b(x_2,y_2)
    content_1 = temp_path+' '+str(x_1_min)+','+str(y_1_min)+','+str(x_1_max)+','+str(y_1_max)+','+str(0)+' '+str(x_2_min)+','+str(y_2_min)+','+str(x_2_max)+','+str(y_2_max)+','+str(0)+'\n'
    f_train.write(content_1)

for cnt in range(91,101):
    temp_path = os.path.join(val_path,str(cnt)+'.bmp')
    temp_coordinate = center_coordinate[cnt]

    x_1 = temp_coordinate[0]
    y_1 = temp_coordinate[1]
    x_2 = temp_coordinate[2]
    y_2 = temp_coordinate[3]
    x_1_min,x_1_max,y_1_min,y_1_max = c2b(x_1,y_1)
    x_2_min,x_2_max,y_2_min,y_2_max = c2b(x_2,y_2)
    content_1 = temp_path+' '+str(x_1_min)+','+str(y_1_min)+','+str(x_1_max)+','+str(y_1_max)+','+str(0)+' '+str(x_2_min)+','+str(y_2_min)+','+str(x_2_max)+','+str(y_2_max)+','+str(0)+'\n'
    f_val.write(content_1)

# augmentation including rotation (90 degree)


f_train.close()
f_val.close()

with open(annotation_path_train) as f_train:
    lines_train = f_train.readlines()
with open(annotation_path_val) as f_val:
    lines_val = f_val.readlines()


# transpose
for i in range(len(lines_train)):
    line = lines_train[i].split()
    image = Image.open(line[0])

    image = image.transpose(Image.TRANSPOSE)
    path = os.path.join(train_path,'rotate_'+os.path.split(line[0])[-1])
    boxes = [list(map(int, box.split(','))) for box in line[1:]]
    new_boxes = []
    for i,box in enumerate(boxes):
        new_box = []
        new_box.append(box[1])
        new_box.append(box[0])
        new_box.append(box[3])
        new_box.append(box[2])

        # ellipse_x = int((new_box[0] + new_box[2]) / 2)
        # ellipse_y = int((new_box[1] + new_box[3]) / 2)
        # draw = ImageDraw.Draw(image)
        # draw.ellipse([(ellipse_x - 10, ellipse_y - 10), (ellipse_x + 10, ellipse_y + 10)], fill=(0))
        # del draw

        if i == 0:
            new_box.append(0)
        else: new_box.append(0)
        new_boxes.append(new_box)

    image.save(path)
    content = path+' '+','.join(str(a) for a in new_boxes[0])+' '+','.join(str(a) for a in new_boxes[1])+'\n'
    # save into annotation
    with open(annotation_path_train,'a') as f_train:
        f_train.write(content)

# transpose
for i in range(len(lines_val)):
    line = lines_val[i].split()
    image = Image.open(line[0])

    image = image.transpose(Image.TRANSPOSE)
    path = os.path.join(val_path,'rotate_'+os.path.split(line[0])[-1])

    boxes = [list(map(int, box.split(','))) for box in line[1:]]
    new_boxes = []
    for i,box in enumerate(boxes):
        new_box = []
        new_box.append(box[1])
        new_box.append(box[0])
        new_box.append(box[3])
        new_box.append(box[2])

        # ellipse_x = int((new_box[0]+new_box[2])/2)
        # ellipse_y = int((new_box[1]+new_box[3])/2)
        # draw = ImageDraw.Draw(image)
        # draw.ellipse([( ellipse_x- 10, ellipse_y - 10), (ellipse_x + 10, ellipse_y + 10)], fill=(0))
        #
        #
        # ellipse_x_true = int((new_box[0] + new_box[2]) / 2)
        # ellipse_y_true = int((new_box[1] + new_box[3]) / 2)
        #
        # draw.rectangle([(ellipse_x_true - 30, ellipse_y_true - 150), (ellipse_x_true + 30, ellipse_y_true + 150)],
        #                    fill=(255))
        # del draw

        if i == 0:
            new_box.append(0)
        else: new_box.append(0)
        new_boxes.append(new_box)
    image.save(path)
    content = path+' '+','.join(str(a) for a in new_boxes[0])+' '+','.join(str(a) for a in new_boxes[1])+'\n'
    # save into annotation
    with open(annotation_path_val,'a') as f_val:
        f_val.write(content)