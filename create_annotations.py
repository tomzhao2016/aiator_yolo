 # This file will write the true annotations to a txt file named 'image_annotation'
 # In the txt, the format should be
 # path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
 # path/to/img2.jpg 120,300,250,600,2
import os

####
#### Read/Create files
####

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
# create new file
f_train = open("/home/qingyang/aiator/data/image_annotation_train.txt", "x")
f_train = open("/home/qingyang/aiator/data/image_annotation_train.txt", "a")

f_test = open("/home/qingyang/aiator/data/image_annotation_test.txt", "x")
f_test = open("/home/qingyang/aiator/data/image_annotation_test.txt", "a")

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
def c2b(x, y, row_size = 1624, col_size = 1236, x_offset = 100, y_offset = 100):

    ## center to bounding box(x_min,x_max,y_min,y_max)
    x_min = max(x - x_offset, 0)
    x_max = min(x + x_offset, row_size)
    y_min = max(y - y_offset, 0)
    y_max = min(y + y_offset, col_size)
    return (int(x_min),int(x_max),int(y_min),int(y_max))


#
for cnt in range(1,91):
    temp_path = os.path.join('/home/qingyang/aiator/data/location_images/train',str(cnt)+'.bmp')
    temp_coordinate = center_coordinate[cnt]

    x_1 = temp_coordinate[0]
    y_1 = temp_coordinate[1]
    x_2 = temp_coordinate[2]
    y_2 = temp_coordinate[3]
    x_1_min,x_1_max,y_1_min,y_1_max = c2b(x_1,y_1)
    x_2_min,x_2_max,y_2_min,y_2_max = c2b(x_2,y_2)
    content_1 = temp_path+' '+str(x_1_min)+','+str(y_1_min)+','+str(x_1_max)+','+str(y_1_max)+','+str(0)+' '+str(x_2_min)+','+str(y_2_min)+','+str(x_2_max)+','+str(y_2_max)+','+str(1)+'\n'
    f_train.write(content_1)


for cnt in range(101,105):
    temp_path = os.path.join('/home/qingyang/aiator/data/location_images/train',str(cnt)+'.bmp')
    temp_coordinate = center_coordinate[cnt]

    x_1 = temp_coordinate[0]
    y_1 = temp_coordinate[1]
    x_2 = temp_coordinate[2]
    y_2 = temp_coordinate[3]
    x_1_min,x_1_max,y_1_min,y_1_max = c2b(x_1,y_1)
    x_2_min,x_2_max,y_2_min,y_2_max = c2b(x_2,y_2)
    content_1 = temp_path+' '+str(x_1_min)+','+str(y_1_min)+','+str(x_1_max)+','+str(y_1_max)+','+str(0)+' '+str(x_2_min)+','+str(y_2_min)+','+str(x_2_max)+','+str(y_2_max)+','+str(1)+'\n'
    f_train.write(content_1)

for cnt in range(91,101):
    temp_path = os.path.join('/home/qingyang/aiator/data/location_images/val',str(cnt)+'.bmp')
    temp_coordinate = center_coordinate[cnt]

    x_1 = temp_coordinate[0]
    y_1 = temp_coordinate[1]
    x_2 = temp_coordinate[2]
    y_2 = temp_coordinate[3]
    x_1_min,x_1_max,y_1_min,y_1_max = c2b(x_1,y_1)
    x_2_min,x_2_max,y_2_min,y_2_max = c2b(x_2,y_2)
    content_1 = temp_path+' '+str(x_1_min)+','+str(y_1_min)+','+str(x_1_max)+','+str(y_1_max)+','+str(0)+' '+str(x_2_min)+','+str(y_2_min)+','+str(x_2_max)+','+str(y_2_max)+','+str(1)+'\n'
    f_test.write(content_1)
