import docx
import os
aaa = os.path.abspath('(涉交通）陶家夼隧道9车连撞.docx')


# path = r"D:\MaXin-Study\2021-10-3\DataClean\TEST\(涉交通）笃行路发生交通事故.docx"
doc = docx.Document(aaa)
texts = []
i = 0
for paragraph in doc.paragraphs:
    i += 1
    print(paragraph.text,"这是第{}段".format(i))

#     texts.append(paragraph.text)
# print('\n'.join(texts))