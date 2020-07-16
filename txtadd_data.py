# 用于转换persontrain.txt 和 personvalid.txt的格式与train.txt valid.txt格式一样
# ./images/valid/2011_000342.jpg -> data/images/valid/2011_000342.jpg

import os


def main():
    # 待转换的txt
    persontrain_txt = './persontrain.txt'
    personvalid_txt = './personvalid.txt'


    # 先删除赶紧转换后的txt
    if(os.path.exists('./finally_persontrain.txt')):
         os.remove('./finally_persontrain.txt')
         print('删除finally_persontrain.txt成功')

    if(os.path.exists('./finally_personvalid.txt')):
         os.remove('./finally_personvalid.txt')
         print('删除finally_personvalid.txt成功')


    finally_personvalid = './finally_personvalid.txt'
    finally_persontrain = './finally_persontrain.txt'

    # 开始转换 oldpersontrain_txt
    for i in open(persontrain_txt, 'r'):
        temp = 'data' + i[1:]
        file = open(finally_persontrain, 'a')
        file.write(temp)
    print("finally_persontrain created")

    # 开始转换oldpersonvalid_txt
    for i in open(personvalid_txt, 'r'):
        temp = 'data' + i[1:]
        file = open(finally_personvalid, 'a')
        file.write(temp)
    print("finally_personvalid created")


if __name__ == '__main__':
    main()
