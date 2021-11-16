import sys
sys.path.append("../")

import datetime
import json
import os
import shutil
import time
# from win32com import client
import docx
import re
import logging
from Utils.logcfg import LOGGING_CONFIG
from Utils.Logger import LoggerSingleton

LoggerSingleton().init_dict_config(LOGGING_CONFIG)


# 清洗数据写入json文件中
class CleanData(object):

    def __init__(self):
        # 目标文件夹
        if os.name == "nt":
            self.target_folders = r"D:\MaXin-Study\2021-10-3\DataClean\Data\BeforeCleanDocx"
            # 方便读取存入的变量
            self.files_format = r"D:\MaXin-Study\2021-10-3\DataClean\Data\BeforeCleanDocx\{}"
            # 转换之后的目标文件
            self.files_result = r"D:\MaXin-Study\2021-10-3\DataClean\Data\BeforeCleanDocx\{}.docx"
            # 查看目标问价夹下有哪些文件
            self.file_list = os.listdir(self.target_folders)
            #  清洗之后并转换成json的目标文件
            self.json_path = r'D:\MaXin-Study\2021-10-3\DataClean\Data\BeforeCleanJson\{}.json'

            # 转换成json之后的docx文件需要移动到AfterCleanDocx,防止运行时不停的读写
            self.after_docx = r"D:\MaXin-Study\2021-10-3\DataClean\Data\AfterCleanDocx\{}"

        else:
            self.target_folders = "/root/mx/PublicOpinionCleaning/Data/BeforeCleanDocx"
            # 方便读取存入的变量
            self.files_format = "/root/mx/PublicOpinionCleaning/Data/BeforeCleanDocx\{}"
            # 转换之后的目标文件
            self.files_result = "/root/mx/PublicOpinionCleaning/Data/BeforeCleanDocx\{}.docx"
            # 查看目标问价夹下有哪些文件
            self.file_list = os.listdir(self.target_folders)
            #  清洗之后并转换成json的目标文件
            self.json_path = "/root/mx/PublicOpinionCleaning/Data/BeforeCleanJson\{}.json"
            # 转换成json之后的docx文件需要移动到AfterCleanDocx,防止运行时不停的读写
            self.after_docx = "/root/mx/PublicOpinionCleaning/Data/AfterCleanDocx\{}"
        # 暂时以字典的方式存储
        self.items = {
            # 文件名称
            "fileName": "",
            # 标签
            "label": "",
            # 类型
            "fileType": "",
            # 内容标题
            "title": "",
            # 时间
            "time": "",
            # 网名
            "nickname": "",
            # 信息来源
            "infoSource": "",
            # 发布内容
            "content": "",
            # 原文链接
            "link": "",
            # 原文内容(文件原本内容)
            "fileContent": "",
        }

    # # 转换docx类型,把文件doc为后缀的传入
    # def convertDocx(self, file_doc):
    #     """
    #     :param file: 需要转换的文件名称
    #     :return:
    #     """
    #     try:
    #         word = client.Dispatch('Word.Application')
    #         # 把文件名称路径传入方法中
    #         path = self.files_format.format(file_doc)
    #         # 目标路径下的文件
    #         doc = word.Documents.Open(path)
    #         # 转换后的文件地址  先把 .doc 后缀名 删除
    #         modify_suffix = file_doc.replace('.doc', '')
    #         # 转化后路径下的文件
    #         new_fileName = self.files_result.format(modify_suffix)
    #         # 12 转换成docx模式
    #         doc.SaveAs(new_fileName, 12)
    #         doc.Close()
    #         word.Quit()
    #         return True
    #     except:
    #         logging.info("转换失败")
    #         return False
    #
    # # 先转换docx文件,再删除转换后的 doc文件
    # def removeDocx(self):
    #     for file in self.file_list:
    #         if file.endswith(".doc"):
    #             file_doc = file
    #             logging.info(file_doc, "=====>这是doc文件,需要转换")
    #             # 转换成docx
    #             file_docx = self.convertDocx(file_doc)
    #             if file_docx:
    #                 # 转换成功之后删除  file 等于 转换之前的doc文件
    #                 logging.info("转换成功")
    #                 os.remove(self.files_format.format(file))
    #                 logging.info("成功删除doc文件")
    #             else:
    #                 logging.info("没有转换成功")
    #     # 转换完成之后,原doc文件删除,只保留docx的
    #     print(self.file_list)

    # 获取整个doc文档内容
    def get_text(self, file_path):
        '''
        :param file_path: 文件路径
        :return:获取文档中的所有内容
        '''
        doc = docx.Document(file_path)
        texts = []
        for paragraph in doc.paragraphs:
            texts.append(paragraph.text)
        return '\n'.join(texts)

    # 清洗数据之后,存储数据
    def clean(self):
        # 先转换 docx 文件,再删除转换后的 doc 文件
        items = self.items.copy()
        # self.removeDocx()
        # 开始对目标文件夹下的docx文件进行清洗
        for file in self.file_list:
            print(file)
            # 文件全部内容
            # content = self.get_text(self.files_format.format(file))
            # （涉警）网民反映举报后被询问身份信息.docx
            content = self.get_text(r"/root/mx/PublicOpinionCleaning/Data/BeforeCleanDocx/（涉警）网民反映举报后被询问身份信息.docx")
            print(content)
            # 文件名称
            fileName = file.replace(".docx", "")
            logging.info("开始清洗")
            # 文件名称
            fileName_result = fileName
            items['fileName'] = fileName_result
            # 标签
            fileLabel_result = re.findall('[（(](涉.*)[）)]', fileName_result)
            if fileLabel_result:
                items['label'] = fileLabel_result[0]

            # 舆情类型
            fileType_result = re.findall("(即时.*)", content)
            if fileType_result:
                items['fileType'] = fileType_result[0]

            # 标题
            title_result = re.findall("(网民.*)", content)
            if title_result:
                items['title'] = title_result[0]

            # 时间
            time_result = re.findall("(.*月.*日)[，,]", content)
            if time_result:
                # 时间需要转化 由10月30日 转化成时间 2021-10-30 00:00:00
                time = self.conversionTime(time_result[0])
                items['time'] = str(time)


            # 网名
            nickname_result = re.findall('网民“(.*?)”在', content)
            if nickname_result:
                items['nickname'] = nickname_result[0]

            # 信息来源
            infoSource_result = re.findall('在“(.*?)”[发贴称发贴称]', content)
            if infoSource_result:
                items['infoSource'] = infoSource_result[0]

            # 发布内容
            content_result = re.findall('[发贴称发贴称][，,:：](.*?)[\s]原文链接', content)
            if content_result:
                items['content'] = content_result[0]

            # 原文链接
            link_result = re.findall('(http[s]://.*)', content)
            if link_result:
                items['link'] = link_result[0]

            # 原文内容
            fileContent_result = content
            items['fileContent'] = fileContent_result

            print(items)

            # 把清洗好的数据 写入文件中
            print("开始清洗")
            self.getFile(items=items)
            print("清洗结束")

            # 写入一个文件 就把原docx文件给一到另一个文件夹下
            print("开始移动")
            self.moveFile(file)
            print("移动结束")

    # 需要把写入好的docx文件给移除或者移动目录
    def moveFile(self, fileName):
        before_filePath = self.files_format.format(fileName)
        after_filePath = self.after_docx.format(fileName)
        shutil.move(before_filePath, after_filePath)

    # 把清洗之后的数据存入新的文件(或者其他方式-----待定)
    def getFile(self, items):
        resultFileName = items.get('fileName')
        resultPath = self.json_path.format(resultFileName)
        with open(resultPath, "w", encoding="utf-8") as f_json:
            json.dump(items, f_json, ensure_ascii=False, sort_keys=True, indent=4)
            logging.info("加载入文件完成...")


    # 转换时间
    def conversionTime(self,a_time):
        year = datetime.datetime.now().strftime('%Y')
        time_time = a_time.replace('月', '-').replace('日', '')

        time_str = year + "-" + time_time + " 00:00:00"

        dateTime_d = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        return dateTime_d

    def run(self):
        # 先转换doc格式的文件
        logging.info("开始")
        self.clean()


if __name__ == '__main__':
    tmp = CleanData()
    tmp.run()
