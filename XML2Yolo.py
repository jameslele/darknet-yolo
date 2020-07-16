import shutil
import xml.etree.ElementTree as ET
import os
from PIL import Image


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    global none_counts, classes
    # 输入文件xml
    in_file = open('./VOCPerson/Annotations/%s.xml' % (image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    # 这里对不标准的xml文件（没有size字段）做了特殊处理，打开对应的图片，获取h, w
    if size == None:
        # print('{}不存在size字段'.format(image_id))
        img = Image.open('./VOCPerson/JPEGImages/' + image_id + '.jpg')
        w, h = img.size  # 大小/尺寸
        # print('{}.xml缺失size字段, 读取{}图片得到对应 w：{} h：{}'.format(image_id, image_id, w, h))
        none_counts += 1
        # return
    else:
        w = int(size.find('width').text)
        h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls) + 1
        #             print('cls_id is {}'.format(cls_id))
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        # 输出label txt
        out_file = open('./YoloPerson/YoloLabels/%s.txt' % (image_id), 'w')
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


def main():
    global none_counts, classes

    classes = ["person"]  # 为了获得cls id

    if not os.path.exists('./YoloPerson/YoloLabels'):
        os.makedirs('./YoloPerson/YoloLabels')
    else:
        shutil.rmtree('./YoloPerson/YoloLabels')
        os.makedirs('./YoloPerson/YoloLabels')

    xml_count = 0
    none_counts = 0
    list_file = os.listdir('./VOCPerson/Annotations/')
    for file in list_file:
        image_id = file.replace('.xml', '')
        convert_annotation(image_id)
        xml_count = xml_count + 1
    print('没有size字段的xml文件数目：{}'.format(none_counts))
    print('转换的总xml个数是 {}'.format(xml_count))


if __name__ == '__main__':
    main()
