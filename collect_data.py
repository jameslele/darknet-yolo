import SelectVOC2012Person
import XML2Yolo
import split_train_valid
import creatrtxt
import txtadd_data
import movelabel
import os, random, shutil
from PIL import Image


def del_unimportant_files():
    persontrain_txt = './persontrain.txt'
    personvalid_txt = './personvalid.txt'
    finally_persontrain_txt = './finally_persontrain.txt'
    finally_personvalid_txt = './finally_personvalid.txt'
    os.remove(finally_persontrain_txt)
    os.remove(finally_personvalid_txt)
    os.remove(persontrain_txt)
    os.remove(personvalid_txt)
    # delete images that not important


def cp_voc_into_darknet():
    """
    Move train.txt, valid.txt, images, labels from voc into darknet
    """
    darknet_train_path = './darknet/data/img/train/'
    darknet_valid_path = './darknet/data/img/valid/'

    if os.path.exists(darknet_train_path):
        shutil.rmtree(darknet_train_path)
    os.makedirs(darknet_train_path)

    if os.path.exists(darknet_valid_path):
        shutil.rmtree(darknet_valid_path)
    os.makedirs(darknet_valid_path)

    # copy path describer
    finally_persontrain_txt = './finally_persontrain.txt'
    finally_personvalid_txt = './finally_personvalid.txt'
    train_txt = './darknet/data/train.txt'
    valid_txt = './darknet/data/valid.txt'

    if os.path.exists(train_txt):
        os.remove(train_txt)
    if os.path.exists(valid_txt):
        os.remove(valid_txt)

    # move all images path into train.txt and valid.txt
    print("convert train.txt and valid.txt from voc into darknet")
    with open(finally_persontrain_txt, 'r') as f:
        files_path = f.read()
        with open(train_txt, 'a+') as s:
            s.write(files_path)

    with open(finally_personvalid_txt, 'r') as f:
        files_path = f.read()
        with open(valid_txt, 'a+') as s:
            s.write(files_path)

    # copy images
    print("copy images from voc to darknet")
    voc_images_train_path = './YoloPerson/img/train/*'
    voc_images_valid_path = './YoloPerson/img/valid/*'
    os.system('cp {} {}'.format(voc_images_train_path, darknet_train_path))
    os.system('cp {} {}'.format(voc_images_valid_path, darknet_valid_path))

    # copy labels
    print("copy labels from voc to darknet")
    voc_labels_train_path = './YoloPerson/labels/train/*'
    voc_labels_valid_path = './YoloPerson/labels/valid/*'
    os.system('cp {} {}'.format(voc_labels_train_path, darknet_train_path))
    os.system('cp {} {}'.format(voc_labels_valid_path, darknet_valid_path))


def collect_data_from_VOC(class_ids=['person']):
    # extract person images
    SelectVOC2012Person.main()
    # extract persion xml and transfer into txt in yolo format
    XML2Yolo.main()
    # split images into train and valid two directories
    split_train_valid.main()
    # 根据训练数据集和验证数据集persontrain.txt and personvalid.txt
    creatrtxt.main()
    # ./images/valid/2011_000342.jpg -> data/images/valid/2011_000342.jpg
    txtadd_data.main()
    # 将YoloLabels中存在一起的训练集，验证集的数据对应的label移到YoloPerson中label文件夹下面对应的文件中
    movelabel.main()
    # Move train.txt, valid.txt, images, labels from voc into darknet
    cp_voc_into_darknet()


def cp_data_from_yolomark_to_darknet():
    """
    From Yolo-mark labeled images
    """
    # split_train_valid, copy image and label together from "Yolo_mark/x64/Release/data/img/" to "darknet/data/train/" and "darknet/data/valid/"
    train_images_in_darknet = []
    valid_images_in_darknet = []
    # firstly split into two parts
    train_txt_in_yolomark = './Yolo_mark/x64/Release/data/train.txt'
    train_txt_in_darknet = './darknet/data/train.txt'
    valid_txt_in_darknet = './darknet/data/valid.txt'
    yolomark_path = './Yolo_mark/x64/Release/'
    darknet_path = './darknet/'

    with open(train_txt_in_yolomark, 'r') as f:
        lines = f.readlines()
        filenumber = len(lines)

    # 训练集比率
    train_rate = 0.9  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    train_picknumber = int(filenumber * train_rate)  # 按照rate比例从文件夹中取一定数量图片

    # ['x64/Release/data/img/0459.png\n', ...]
    train_sample_list = random.sample(lines, train_picknumber)
    valid_sample_list = list(set(lines).difference(set(train_sample_list)))

    for i in train_sample_list:
        file_name_in_yolomark = i[12:-5]
        train_file_name_in_darknet = file_name_in_yolomark.replace('img/', 'img/train/')

        train_label_in_yolomark = yolomark_path + file_name_in_yolomark + '.txt'
        train_image_in_yolomark = yolomark_path + file_name_in_yolomark + '.png'
        train_label_in_darknet = darknet_path + train_file_name_in_darknet + '.txt'
        train_image_in_darknet = darknet_path + train_file_name_in_darknet + '.png'

        # copy image
        shutil.copy(train_image_in_yolomark, train_image_in_darknet)
        # copy label
        shutil.copy(train_label_in_yolomark, train_label_in_darknet)
        # copy file path
        train_images_in_darknet.append(train_image_in_darknet.replace(darknet_path, '') + '\n')

    for i in valid_sample_list:
        file_name_in_yolomark = i[12:-5]
        valid_file_name_in_darknet = file_name_in_yolomark.replace('img/', 'img/valid/')

        valid_label_in_yolomark = yolomark_path + file_name_in_yolomark + '.txt'
        valid_image_in_yolomark = yolomark_path + file_name_in_yolomark + '.png'
        valid_label_in_darknet = darknet_path + valid_file_name_in_darknet + '.txt'
        valid_image_in_darknet = darknet_path + valid_file_name_in_darknet + '.png'

        # copy image
        shutil.copy(valid_image_in_yolomark, valid_image_in_darknet)
        # copy label
        shutil.copy(valid_label_in_yolomark, valid_label_in_darknet)
        # copy file path
        valid_images_in_darknet.append(valid_image_in_darknet.replace(darknet_path, '') + '\n')

    # copy file path
    with open(train_txt_in_darknet, 'a+') as f:
        f.writelines(train_images_in_darknet)
    with open(valid_txt_in_darknet, 'a+') as f:
        f.writelines(valid_images_in_darknet)


def cp_two_files_from_yolomark_to_darknet():
    obj_names_in_yolomark = './Yolo_mark/x64/Release/data/obj.names'
    obj_data_in_yolomark = './Yolo_mark/x64/Release/data/obj.data'
    obj_names_in_darkent = './darknet/data/obj.names'
    obj_data_in_darknet = './darknet/data/obj.data'
    shutil.copy(obj_names_in_yolomark, obj_names_in_darkent)
    shutil.copy(obj_data_in_yolomark, obj_data_in_darknet)


def collect_data_from_custom_data():
    """
    From Yolo-mark labeled images
    """
    # split_train_valid, image and label together from "Yolo_mark/x64/Release/data/img/" to "darknet/data/train/" and "darknet/data/valid/"
    cp_data_from_yolomark_to_darknet()
    # move obj.data, obj.names from "Yolo_mark/x64/Release/data/" to "darknet/data"
    cp_two_files_from_yolomark_to_darknet()


def convert_jpg_to_png():
    print("convert_jpg_to_png...")
    train_txt = './darknet/data/train.txt'
    for i in open(train_txt, 'r'):
        if i[-4:-1] == 'jpg':
            jpg = './darknet/' + i.replace('\n', '')
            png = jpg.replace('jpg', 'png')

            im = Image.open(jpg)
            im.save(png)
            os.remove(jpg)

    valid_txt = './darknet/data/valid.txt'
    for i in open(valid_txt, 'r'):
        if i[-4:-1] == 'jpg':
            jpg = './darknet/' + i.replace('\n', '')
            png = jpg.replace('jpg', 'png')
            im = Image.open(jpg)
            im.save(png)
            os.remove(jpg)

    # change all jpg to png in train.txt and valid.txt


if __name__ == "__main__":
    print("Collect data from VOC2012\n")
    collect_data_from_VOC()
    # collect custom data from yolomark
    print("Collect custom data\n")
    collect_data_from_custom_data()
    # del_unimportant_txt()
    del_unimportant_files()
    # convert_jpg_to_png in darknet
    # convert_jpg_to_png()