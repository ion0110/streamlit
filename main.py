'''
カレントディレクトリで
streamlit run main.py
を実行
'''

#https://www.youtube.com/watch?v=zp-kAt1Ih5k&t=417s
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')
'''
API
https://docs.streamlit.io/en/stable/api.html
'''




st.write('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'読み込み中... {i + 1}%')
    bar.progress(i + 1)
    time.sleep(0.01)


'Done!!!'




#2カラム
left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字表示')
if button:
    right_column.write('ここは右カラム')



#expander
expander = st.beta_expander('問い合わせ' )
expander.write('問い合わせに対する回答')




#サイドバー
st.sidebar.write('サイドバー')
#textbox(interactive)
text = st.sidebar.text_input('あなたの趣味は？')
#slider
condision = st.sidebar.slider('あなたの調子は',0, 100, 50)

'あなたの趣味は', text
'コンディション:', condision

#checkbox
if st.checkbox('画像表示'):
    #画像読み込み
    img = Image.open('sample.png')
    st.image(img, caption='キャプション', width=300, use_column_width=False)

#selectbox
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は', option, 'です'



#データフレーム
st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=400, height=300)

#staticな表を作るとき
st.table(df.style.highlight_min(axis=1))



#マジックコマンド
'''
https://docs.streamlit.io/en/stable/api.html#display-text
# 章
## 節
### 項


```python
import stream as st
import numpy as np
import pandas as pd
```
'''



#グラフ
'''
https://docs.streamlit.io/en/stable/api.html#display-charts
'''
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns = ['a', 'b', 'c']
)
st.area_chart(df2)




#マッププロット
df3 = pd.DataFrame(
    #新宿付近
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns = ['lat', 'lon']
)
st.map(df3)
