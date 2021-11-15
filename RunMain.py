from operation.DocxCleanMain import CleanData
from operation.ExtractData import ExtractData


class Main(object):
    def __init__(self):
        self.CleanData = CleanData()
        self.ExtractData = ExtractData()

    def run(self):
        # 先遍历文件并清洗文件
        self.CleanData.run()
        # 再把 清理之后的数据写入需要的格式中
        self.ExtractData.run()


if __name__ == '__main__':
    run = Main()
    run.run()
