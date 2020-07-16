# coding: utf-8

# 将YoloJPEGimg里面的图片随机划分成训练集，验证集，测试集

import os, random, shutil


def copyFile(fileDir):
    global trainDir, validDir, testDir
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    #         # 获取所有图片的名字前缀
    #         total_pathdir_first = [i[:-4] for i in pathDir]
    #         print(len(total_pathdir_first))
    filenumber = len(pathDir)

    # 训练集比率
    train_rate = 0.8  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    train_picknumber = int(filenumber * train_rate)  # 按照rate比例从文件夹中取一定数量图片

    # 验证集比率
    valid_rate = 0.1  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    valid_picknumber = int(filenumber * valid_rate)  # 按照rate比例从文件夹中取一定数量图片

    # 测试集比率
    test_rate = 0.1  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    test_picknumber = int(filenumber * test_rate)  # 按照rate比例从文件夹中取一定数量图片

    # 剪切训练集
    train_sample_list = random.sample(pathDir, train_picknumber)  # 随机选取train_picknumber数量的样本图片
    for name in train_sample_list:
        shutil.copy(fileDir + name, trainDir + name)

    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    # 剪切验证集
    valid_sample_list = random.sample(pathDir, valid_picknumber)  # 随机选取train_picknumber数量的样本图片
    for name in valid_sample_list:
        shutil.copy(fileDir + name, validDir + name)

    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    # 剪切测试集
    test_sample_list = random.sample(pathDir, test_picknumber)  # 随机选取train_picknumber数量的样本图片
    for name in test_sample_list:
        shutil.copy(fileDir + name, testDir + name)

    return


def main():
    global trainDir, validDir, testDir

    # 指定划分数据集后的文件路径
    trainDir = './YoloPerson/img/train/'
    testDir = './YoloPerson/img/test/'
    validDir = './YoloPerson/img/valid/'


    if os.path.exists('./YoloPerson/img/'):
        shutil.rmtree('./YoloPerson/img/')
    os.makedirs('./YoloPerson/img/train/')
    os.makedirs('./YoloPerson/img/test/')
    os.makedirs('./YoloPerson/img/valid/')
    fileDir = "./VOCPerson/JPEGImages/"  # 源图片文件夹路径
    copyFile(fileDir)


if __name__ == '__main__':
    main()
