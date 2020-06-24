# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:03:28 2020

@author: Wang Tianyu AND CUMT PixelShine
"""

import pandas as pd
from aip import AipNlp
import codecs


APP_ID = '20366338'
API_KEY = 'edwCzK59s10iVkfW6WtajAP4'
SECRET_KEY = 'n0sTr3doqBGnzx1j6DrGcgIpmmwIy8Ey'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def get_sentiments(text):
    try:
        count=1
        sitem=client.sentimentClassify(text)

        while (not sitem.get('items',{})) and (count<10):
            count+=1
            sitem = client.sentimentClassify(text)

        sitems=sitem['items'][0]
        positive=sitems['positive_prob']
        confidence=sitems['confidence']
        sentiment=sitems['sentiment']
        output='{}\t{}\t{}\t{}\n'.format(text,positive,confidence,sentiment)
        f=codecs.open('sentiment.xls','a+','gb18030')
        f.write(output)
        f.close()
        print('Done')

    except Exception as e:
        print(repr(e))

def get_content():
    data=pd.DataFrame(pd.read_csv('0201.csv'))
    data.columns=['NickName','UserLevel','Location','Text','Response','Time']
    return data


data=get_content()
for i in range(data.shape[0]):
    print('正在处理第{}条,还剩{}条'.format(i,data.shape[0]-i))
    cur_Text=data.Text[i]
    get_sentiments(cur_Text)