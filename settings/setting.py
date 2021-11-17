# 数据汇总



TIMESLEEP = 30
# 需要循环提取的目标文件
TARGET_FOLDERS = "/home/analysis/upload/"
# 方便读取存入的变量
FILES_FORMAT = "/home/analysis/upload/{}"
# 转换之后的目标文件  现在不用
FILES_RESULT = "/home/analysis/upload/{}.docx"
# 清洗之后并转换成json的目标文件
JSON_PATH = "/root/mx/PublicOpinionCleaning/Data/BeforeCleanJson/{}.json"
# 转换成json之后的docx文件需要移动到AfterCleanDocx,防止运行时不停的读写
AFTER_DOCX = "/root/mx/PublicOpinionCleaning/Data/AfterCleanDocx/{}"



# 读取解析之后的json文件路径
READJSONPATH = "/root/mx/PublicOpinionCleaning/Data/BeforeCleanJson"
# format变量
PATHFORMAT = "/root/mx/PublicOpinionCleaning/Data/BeforeCleanJson/{}"
# format变量
AFTERPATHFORMAT = "/root/mx/PublicOpinionCleaning/Data/AfterCleanJson/{}"
# 最终数据的文件夹
RESULT_JSON = "/home/analysis/data/result.json"




resultItems = {
    # 平台详情
    "platformDetails": [
        # {
        # # 舆情数据详情
        # "title": "",
        # "content": "",
        # "time": "",
        # "nickname": "",
        # "label": "",
        # # 平台
        # "platform": "",
        # },
    ],
}



