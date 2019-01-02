#  https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E7%BE%8E%E5%A5%B3&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis
import os
import json

import requests
# 简单的网络请求 json操作,循环,字符串操作,io相关  异常处理
keyword = "美女"
count=20
page=5

# range(start, stop[, step])
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例：range（0， 5,2） 結果0,2,4

for i in range(0,count*page,count):
    url = "https://www.toutiao.com/search_content/?offset="+str(i)+"&format=json&keyword="+keyword+"&autoload=true&count="+str(count)+"&cur_tab=1&from=search_tab&pd=synthesis"
    print(url)
    response = requests.get(url)
    # print(response.text)
    print(type(response.text))  # <class 'str'>
    # str字符串类型 字典或者列表 转换成json
    # 获得的数据{} 字典,[]是列表
    dict = json.loads(response.text)
    # <class 'dict'> key-value
    # print(type(dict))
    # print(dict['count'])
    # 读取data 列表,每个元素是字典, 读取key 'image_list'
    # image_list 列表里面是 元素字典, 读取url,得到地址 不带http 所以得拼接http
    data = dict["data"]
    for item in data:  # data列表
        # print("data 类型",type(item))
        # item["image_list"] imagelist列表
        # print(item)
        try:
            for urlItem in item['image_list']:
                # print(urlItem)
                # print("image_list类型",type(urlItem))
                imageUrl = "http:" + urlItem["url"]
                # http: // p1 - tt.bytecdn.cn /list /pgc - image / 152775065065407282bb42b
                print(imageUrl)
                #       保存图片ff,wb 表示写入二进制文件
                #         切割图片的名称,字符串操作,读取最后一个数据
                imageUrls = imageUrl.split("/");
                imageNmae = imageUrls[-1]
                imageDir = imageUrls[-2]
                # 创建报错文件的目录
                dir = "./" + imageDir
                isExist = os.path.exists(dir)
                if not isExist:
                    os.mkdir(dir)
                imageFile = open(dir + "/" + imageNmae + ".jpg", "wb")
                imageResponse = requests.get(imageUrl, stream=True)
                for stream in imageResponse:
                    imageFile.write(stream)
                imageFile.close()

        except Exception as e:
            print(e)
            print(item)  # 部分数据没有image_list 节点 导致错误,打印报错数据
