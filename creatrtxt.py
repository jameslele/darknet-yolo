# -*-coding:utf-8-*-

# 根据训练数据集和验证数据集persontrain.txt and personvalid.txt
import os


def text_save(root, filename, data):  # filename为写入txt文件的路径，data为要写入数据列表.
    root = root.replace('/YoloPerson', '')
    file = open(filename, 'a')
    for i in range(len(data)):
        s = root + data[i] + '\n'
        file.write(s)
    file.close()
    print("保存文件成功")


def main():
    trainDir = './YoloPerson/img/train/'
    validDir = './YoloPerson/img/valid/'

    train_pathDir = os.listdir(trainDir)  # 取图片的原始路径
    print('训练集图片数目: {}'.format(len(train_pathDir)))

    valid_pathDir = os.listdir(validDir)  # 取图片的原始路径
    print('验证集图片数目: {}'.format(len(valid_pathDir)))


    # 删除persontrain.txt and personvalid.txt

    if(os.path.exists('./persontrain.txt')):
         os.remove('./persontrain.txt')
         print('删除persontrain.txt成功')


    if(os.path.exists('./personvalid.txt')):
         os.remove('./personvalid.txt')
         print('删除personvalid.txt成功')

    text_save(trainDir, './persontrain.txt', train_pathDir)
    text_save(validDir, './personvalid.txt', valid_pathDir)

    print('persontrain.txt 有 {} 行'.format(len([i for i in open('./persontrain.txt', 'r')])))
    print('personvalid.txt 有 {} 行'.format(len([i for i in open('./personvalid.txt', 'r')])))


if __name__ == '__main__':
    main()
