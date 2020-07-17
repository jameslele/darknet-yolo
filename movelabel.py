# 将训练集，验证集的数据对应的label文件移到label文件夹下面对应的文件中

import os, shutil


def main():
    train_data_label = './YoloPerson/labels/train/'
    valid_data_label = './YoloPerson/labels/valid/'

    if os.path.exists(train_data_label):
        shutil.rmtree(train_data_label)
    os.makedirs(train_data_label)

    if os.path.exists(valid_data_label):
        shutil.rmtree(valid_data_label)
    os.makedirs(valid_data_label)


    # 原始的所有label文件夹

    root_label = './YoloPerson/YoloLabels/'

    # 操作训练集
    count = 0
    for i in open('./finally_persontrain.txt', 'r'):
        temp = i[15:-5]
        # print(temp)
        shutil.copy(root_label + temp + '.txt', train_data_label + temp + '.txt')
        # count += 1
        # print(count)

    # 操作验证集
    for i in open('./finally_personvalid.txt', 'r'):
        temp = i[15:-5]
        # print(temp)
        shutil.copy(root_label + temp + '.txt', valid_data_label + temp + '.txt')
