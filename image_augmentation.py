from PIL import Image,ImageDraw
import os

# this file is to save augmented data
train_path = '/home/qingyang/aiator/data/location_images/train'
val_path = '/home/qingyang/aiator/data/location_images/val'

# augmentation including rotation (90 degree)

# read images/bounding boxes
annotation_path_train = '/home/qingyang/aiator/data/image_annotation_train.txt'
annotation_path_test = '/home/qingyang/aiator/data/image_annotation_test.txt'

with open(annotation_path_train) as f_train:
    lines_train = f_train.readlines()

with open(annotation_path_test) as f_val:
    lines_val = f_val.readlines()


# rotate clockwise
for i in range(len(lines_train)):
    line = lines_train[i].split()
    image = Image.open(line[0])
    img_width,img_height = image.size
    image = image.rotate(90)
    path = os.path.join(train_path,'rotate_'+os.path.split(line[0])[-1])
    image.save(path)
    boxes = [list(map(int, box.split(','))) for box in line[1:]]
    new_boxes = []
    for i,box in enumerate(boxes):
        new_box = []
        new_box.append(img_height-box[1])
        new_box.append(box[0])
        new_box.append(img_height-box[3])
        new_box.append(box[2])

        ellipse_x = int((new_box[0] + new_box[2]) / 2)
        ellipse_y = int((new_box[1] + new_box[3]) / 2)
        draw = ImageDraw.Draw(image)
        draw.ellipse([(ellipse_x - 10, ellipse_y - 10), (ellipse_x + 10, ellipse_y + 10)], fill=(0))
        del draw

        if i == 0:
            new_box.append(3)
        else: new_box.append(4)
        new_boxes.append(new_box)
    content = path+' '+','.join(str(a) for a in new_boxes[0])+' '+','.join(str(a) for a in new_boxes[1])+'\n'
    # save into annotation
    with open(annotation_path_train,'a') as f_train:
        f_train.write(content)

# rotate clockwise
for i in range(len(lines_val)):
    line = lines_val[i].split()
    image = Image.open(line[0])
    img_width,img_height = image.size
    image = image.rotate(90)
    path = os.path.join(val_path,'rotate_'+os.path.split(line[0])[-1])

    boxes = [list(map(int, box.split(','))) for box in line[1:]]
    new_boxes = []
    for i,box in enumerate(boxes):
        new_box = []
        new_box.append(img_height-box[1])
        new_box.append(box[0])
        new_box.append(img_height-box[3])
        new_box.append(box[2])

        ellipse_x = int((new_box[0]+new_box[2])/2)
        ellipse_y = int((new_box[1]+new_box[3])/2)
        draw = ImageDraw.Draw(image)
        draw.ellipse([( ellipse_x- 10, ellipse_y - 10), (ellipse_x + 10, ellipse_y + 10)], fill=(0))
        del draw

        if i == 0:
            new_box.append(3)
        else: new_box.append(4)
        new_boxes.append(new_box)
    image.save(path)
    content = path+' '+','.join(str(a) for a in new_boxes[0])+' '+','.join(str(a) for a in new_boxes[1])+'\n'
    # save into annotation
    with open(annotation_path_test,'a') as f_test:
        f_test.write(content)
