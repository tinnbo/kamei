import streamlit as st
st.title('初めてのstreamlit')
st.write('これから。')
text=st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は,'+text+'です')
condition=st.slider('あなたの最近の調子は？',0,100,50)
#最初値,最大値,スタート位置
st.write('コンディション:',condition)
option=st.selectbox('好きな数字を教えてください',list(['1番','2番','3番','4番']))
'あなたが選択したのは,'+option+'です'
import time
st.sidebar.write('プログレスバーの表示')
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
 latest_iteration.text(f'Iteration{i+1}')
 bar.progress(i +1)
 time.sleep(0.1)
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラムです')
from PIL import Image #PILをpip install pillowを実施する
img = Image.open("S__74104853.jpg")
#自分の画像のファイル名にする(room.jpgは例えば)
#自分のPCの画像を同じフォルダに入れて指定する
st.image(img, caption='生活場面', use_column_width=True)
import pandas as pd
import numpy as np
df = pd.DataFrame(
np.random.rand(100,2)/[50,50] + [35.69,139.70],
columns = ['lat','lon',]#lat lon 緯度と経度
)
#緯度と経度から地図に書き込む
st.map(df)
import numpy as np
df = pd.DataFrame(
np.random.rand(20,3), #20行3列
columns = ['a','b','c']
)
#表として表示する
st.table(df.style.highlight_max(axis=0))
st.bar_chart(df)