# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re

content = """矛盾风险隐患类： 
1、涉文登河景东城
文登河景东城业主因供暖问题，文登王军军组织业主10月28日（周四）到文登信访局维权，并在群内发起接龙。
姓名：王军军，男，手机号码: 13061194588，身份证号：370827199008282013，地址: 文登区天福路街道文山路11号扬程少年宫五楼。
2、涉访群体
此群体为多个事件上访人员组成，计划联合维权。荣成张忠平煽动群内成员到省检察院维权。
姓名：张忠平，手机号：13573717567，身份证号：370633195007146739，地址：荣成市港湾街道办事处大鱼岛村3区301号。
3、涉信广金服投资
信广金服投资人因投资受损，荣成张明柱煽动投资人游行维权。
姓名：张明柱，男，手机号码: 18310185916，身份证号230822194803277314，地址: 山东省威海市荣成市斥山街道佰凤凰湖D区。
4、涉环翠瑞德碧和府
环翠瑞德碧和府业主因对物业不满，乳山王彬鼓动业主到温泉政府上访。
姓名：王彬，男，手机号码：18963162009，身份证号：371083198001212518，地址：山东省威海市乳山市午极镇上万口村35号。
5、涉环翠华润湾九里
环翠华润湾九里业主因对物业不满，河南张伏龙鼓动业主上访。
姓名：张伏龙，男，手机号码:17538146354，身份证号：410922200006102711，地址: 河南省濮阳市清丰县大屯乡东纪庄村2排。
6、涉乳山假日港湾小区
乳山假日港湾小区部分业主因房屋建设与前期开发商宣传不符，乳山马婉娣组织业主到乳山市政府反映诉求。
姓名：马婉娣，女，手机号码: 13216660709，身份证号330219195107090422，地址：乳山银滩假日港湾35幢601室。
专项监测任务：
1、涉恒大今日情况 
环翠恒大海上帝景，环翠王爱田组织业主到住建局维权。
姓名：王爱田，男，手机号码: 15562158339，身份证220603197006181215，地址: 山东省威海市环翠区威海恒大海上帝景27号楼1301。
2、银信、诺金、汇利群体动态
今日无新增
 3、涉捷越今日情况 
今日无新增。"""


type = re.findall("(即时.*)", content)[0]
print(type)
# 标题
title = re.findall("(网民.*)", content)[0]
print(title)
# 时间
time = re.findall("(.*月.*日)[，,]", content)[0]
print(time)
# 昵称
name = re.findall('网民“(.*?)”在', content)[0]
print(name)
# 发布平台
web = re.findall('在“(.*?)”[发贴称发贴称]', content)[0]
print(web)
# 内容
contents = re.findall('[发贴称发贴称][，,:：](.*?)[\s]原文链接', content)
print(contents)
# 原文链接
link = re.findall('(http[s]://.*)', content)
print(link)
