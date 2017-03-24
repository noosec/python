# coding=utf-8

import re
import os
import urllib
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

def read(filename,bz):
    os.chdir(new_pwd)

    f=open(filename,'r')


    htmls2=f.readlines()
    htmls=str(htmls2)
    get=[]
    post=[]
    html=re.compile(r'''    \<url\>\<\!\[CDATA\[(.*?)\]\]\>\<\/url\>.*?Cookie: JSESSIONID=.*?\\n\', '\\n', '(.*?)]]>''')

    #html2=re.compile(r'''    \<request base64=\"false\"\>\<\!\[CDATA\[(\S.*?)\]\]\>\<\/request\>''')
    htt=html.findall(htmls)
    for i in range(len(htt)):
        str2=htt[i][0]
        str2_sp=str2.split('/',3)
        #print str2[len(str2):]
        if (htt[i][1]=='' and str2[len(str2)-3:]!='.js' and  str2[len(str2)-4:]!='.png' and str2[len(str2)-4:]!='.htm'):

            get.append(str2_sp[2]+'\tGet\t/'+str2_sp[3]+'\t  \t'+filename[:-4]+'\t'+bz+'\n')     #https://ts1.cslc.com.cn  长度为23,只输出其后内容
        elif htt[i][1]!='':
            #print htt[i][0],htt[i][1]
            post.append(str2_sp[2]+'\tPost\t/'+str2_sp[3]+'\t'+htt[i][1]+'\t'+filename[:-4]+'\t'+bz+'\n')

    for i in range(len(get)):

        o.write(get[i])


    for j in range(len(post)):

        o.write(post[j])


def sec(dir2,bz):
    dirs=os.listdir(dir2)   #获取当前路径下文件名
    #if not os.path.exists('ok11'):
    #    os.mkdir('ok11')
    print '[+] Begin...',bz
    for i in range(len(dirs)):
        read(dirs[i],bz)
        #print dirs[i]
    print '[+] Done ...'



def main():
    global pwd,o,new_pwd
    pwd=os.getcwd()
    o=open('all_data.txt','w+')
    list1=['ok','wx']

    for i in range(len(list1)):
        new_pwd=pwd+'\\'+list1[i]
        sec(new_pwd,list1[i])



if __name__ == '__main__':
    main()
