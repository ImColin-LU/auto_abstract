import jieba
from seq2seqAttSum.string_replace import pyltp_model, preprocess

titles = []
contents = []
title = ''
content = ''
model = pyltp_model()

with open(r'C:\Users\only you\Downloads\news_sohusite_xml.smarty\news_sohusite_xml.smarty.txt', 'r', encoding='utf-8') as lines:
    for num, line in enumerate(lines):
        if len(titles) % 1000 == 0:
            print(num, len(titles))
        cur_num = num % 6
        if cur_num == 3:
            title = line[14:-16]
            title = title.replace('\u3000', ' ')
            title = preprocess(title, model)
        if cur_num == 4:
            content = line[9:-11]
            content = content.replace('\u3000', ' ')
            content = preprocess(content, model)
        if cur_num == 0:
            if len(title) == 0 or len(content) == 0:
                continue
            else:
                titles.append(title)
                contents.append(content)
                title = ''
                content = ''
        if len(titles) > 15000:
            break
total_datas = titles + contents

id=[]
with open(r'D:\python 项目\data\contents.txt', 'w+', encoding='utf-8') as f:
    for i ,element in enumerate(contents):
        if len(element)<200 or len(element)>500:
            id.append(i)
            continue
        f.write(" ".join([m.replace('TAGDATE','TAG_DATE').replace('S-Ni','TAG_NAME_EN').replace('S-Nh','TAG_NAME_EN').replace('TAGNUM','TAG_NUMBER') for m in element]) + '\n')
print(id)
with open(r'D:\python 项目\data\titles.txt', 'w+', encoding='utf-8') as f:
    for i,element in enumerate(titles):
        if i in id:
            continue
        f.write(" ".join([m.replace('TAGDATE','TAG_DATE').replace('S-Ni','TAG_NAME_EN').replace('S-Nh','TAG_NAME_EN').replace('TAGNUM','TAG_NUMBER') for m in element]) + '\n')