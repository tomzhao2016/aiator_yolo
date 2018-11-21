import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image


# def detect_img(yolo):
#     while True:
#         img = input('Input image filename:')
#         try:
#             image = Image.open(img)
#         except:
#             print('Open Error! Try again!')
#             continue
#         else:
#             r_image = yolo.detect_image(image)
#             r_image.show()
#     yolo.close_session()

# rewrite this function
def detect_img(yolo):
    # annotation_path = '/home/qingyang/aiator/data/image_annotation_val.txt'
    # with open(annotation_path) as f:
    #     lines = f.readlines()
    # ids = [20181106142906050,20181106143433440,20181106143824597,20181106144053796,20181106144327859]
    for i in range(1,21):
        img = '/home/qingyang/aiator/data/huizhou_3/'+str(i)+'.bmp'
        try:
            image = Image.open(img).convert('RGB')
            # line = lines[i].split()
            # image = Image.open(line[0]).convert('RGB')
            # box = [list(map(int, box.split(','))) for box in line[1:]]
            # print(box)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image,test=True,boxes_true=None)
            r_image.save('results_test/detected_'+str(i)+'.jpg')
            print(str(i)+' is detected!')
#     yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='./path2your_video',
        help = "Video input path"
    )

    parser.add_argument(
        "--output", nargs='?', type=str, default="",
        help = "[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))
    elif "input" in FLAGS:
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
