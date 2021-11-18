import sys
import time

sys.path.append("../")

import json
import os
import re
import shutil
from settings.setting import resultItems
from settings.setting import READJSONPATH,PATHFORMAT,AFTERPATHFORMAT,RESULT_JSON
import logging
from Utils.logcfg import LOGGING_CONFIG
from Utils.Logger import LoggerSingleton

LoggerSingleton().init_dict_config(LOGGING_CONFIG)


# 提取数据入到完整的数据格式中
class ExtractData(object):
    def __init__(self):
        if os.name == "nt":
            # 需要提取的文件 的目录
            self.readPath = r"D:\MaXin-Study\2021-10-3\DataClean\Data\BeforeCleanJson"
            self.pathFormat = r"D:\MaXin-Study\2021-10-3\DataClean\Data\BeforeCleanJson\{}"
            self.afterPathFormat = r"D:\MaXin-Study\2021-10-3\DataClean\Data\AfterCleanJson\{}"
            # 最终数据的文件夹
            self.resultJson = r"D:\MaXin-Study\2021-10-3\DataClean\ResultData\result.json"

        else:
            self.readPath = READJSONPATH
            self.pathFormat = PATHFORMAT
            self.afterPathFormat = AFTERPATHFORMAT
            # 最终数据的文件夹
            self.resultJson = RESULT_JSON

    # 舆情详细数据
    def publicOpinionDetails(self, json_data):
        # 平台
        infoSource = json_data['infoSource']
        # 标题
        title = json_data['title']
        # 标签
        label = json_data['label']
        # 时间
        time = json_data['time']
        # 网名
        nickname = json_data['nickname']
        # 内容
        content = json_data['content']
        # 链接
        link = json_data['link']
        # 文件原本内容
        fileContent = json_data['fileContent']
        details = {
            "title": title,
            "content": content,
            "time": time,
            "nickname": nickname,
            "label": label,
            "platform": infoSource,
            "link": link,
            "fileContent": fileContent
        }
        return details

    def writeFile(self, results):
        with open(self.resultJson, 'w', encoding='utf8')as fl:
            json.dump(results, fl, ensure_ascii=False, sort_keys=True, indent=4)
        logging.info("添加数据到result.json完成")

    # 需要把写入好的json文件给移除或者移动目录
    def moveFile(self, fileName):
        logging.info("开始移动BeforeJson文件")
        before_filePath = self.pathFormat.format(fileName)
        after_filePath = self.afterPathFormat.format(fileName)
        shutil.move(before_filePath, after_filePath)
        logging.info("移动到AfterJson文件下成功")

    # 如果需要增加数据,需要先把原本的数据提取出来,再把新的数据添加进去,最后就可以写入了
    def getJson(self, items):
        with open(self.resultJson, 'r', encoding="UTF-8") as fl:
            json_data = json.load(fl)
            detailslist = json_data['platformDetails']
            detailslist.append(items)
            return detailslist

    # 提取文件信息 写入信息
    def getInfo(self):
        try:
            # 如果该目录下有文件,说明需要清洗,如果没有 就说明文件已经清洗完毕
            file_list = os.listdir(self.readPath)
            if file_list:
                # 如果有文件需要提取
                for _ in file_list:
                    print(_)
                    if _.endswith('.json'):
                        path = self.pathFormat.format(_)
                        with open(path, 'r', encoding='utf8')as fl:
                            json_data = json.load(fl)
                        #  获取相对应的需要的数据
                        # 遍历 舆情详细数据 ,转化成json文件
                        details = self.publicOpinionDetails(json_data)
                        # 先读取json文件中内容并提取,然后把新获取的数据增加进去,然后写入文件
                        detailslist = self.getJson(details)
                        resultItems['platformDetails'] = detailslist
                        print(resultItems)
                        self.writeFile(resultItems)
                        # 移动存好的json文件到新的目录下
                        self.moveFile(_)
                    else:
                        logging.info("不是清洗之后的json文件")
            else:
                logging.info("暂时没有文件可以提取")
        except Exception as msg:
            logging.exception(logging.exception("出现异常错误{}".format(msg)))

    def run(self):
        self.getInfo()


if __name__ == '__main__':
    tmp = ExtractData()
    while True:
        tmp.run()
        time.sleep(30)
