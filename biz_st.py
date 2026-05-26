import streamlit as st

st.title('첫번째 웹 어플 만들기')

"###### 첫번째 웹 어플 만들기"

"""
# 비즈니스 모델 분석📚

[네이버](https://www.naver.com)  
[홍익대학교](https://hongik.oc.kr)

이것이 일반 본문 **이것이 굵은 글씨** *이것이 기울임 글씨* ~~이것이 취소선~~

:red[빨간색 글씨] :green[초록색 글씨] :blue[파란색 글씨]


```python
import streamlit as st

print("코드 블록")
```
"""
#streamlit magic 여러줄 쓸 수 있는 문자열
#``` 코드블럭 , ```옆에 python, r, c 쓰면 색 변함`
st.caption('캡션(작고 흐린 글씨로 표현됨)')

with st.echo():
    #이 블록의 코드와 결과를 출력
    name = "HyeonJu"
    st.write("Hello, Streamlit!", name)

st.latex('\int_a^b f(x)dx')
"$$\int_a^b f(x)dx$$"

# : 이미지, 오디오, 동영상'

# C:\Users\guswn\OneDrive\바탕 화면\test\data\python설명.jpeg (절대경로)
# 이미지, 오디오, 동영상 이름 바꿀때 잘 확인
# . -> 현재폴더
'#### : orange[이미지 : st.image()]'
st.image("./data/python설명.jpeg", caption="파이썬 로고", width=500)
# 현재폴더의 데이터 폴더에서 사진꺼내기
'#### :orange[오디오: st.audio()]'
st.audio("./data/bombinsound.mp3", format="audio/mpeg", loop=True)
'#### :orange[동영상: st.video()]'
# 'rb' : 바이너리 모드로 파일 열기
video_file = open("./data/연주.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st.divider() # 구분선

'# 📚 : 콜아웃'

'#### : orange[정보: st.info)]'
st.info(
    icon="ℹ️",
    body='''
    **:sunglasses: 이것은 정보를 제공하는 콜아웃입니다.**
    - :red[빨간색 텍스트]
        - :blue [파란색 텍스트]
    - :green [초록색 텍스트]
        - :orange[주황색 텍스트]
    '''
)
'#### :orange[경고: st.warning()]'
st.warning('This is a warning message', icon="⚠️")

'### :orange[에러: st.error()]'
st.error('This is an error message', icon="🚫")

'#### :orange[성공: st.success()]'
st.success('This is a success message', icon="✅")

'# :blue[데이터 테이블]'

'#### :orange[Pandas 데이터 프레임]'
import pandas as pd
df = pd.DataFrame(
    {'id':[1,2,3],
     'name':['Alice', 'Bob', 'Charlie'],
     'age':[24,34,45]
     }
)
df # 데이터프레임 출력

st.metric("Temperature", "70 °F", "1.2 °F")

'#### :orange[지표(Metric)]'
col1, col2, col3, col4 = st.columns (4) # 3개의 컬럼 생성
col1.metric("Temperature", "70 °F", "1.2 °F")
col1.write("이것은 온도 지표입니다.")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col4.metric("Pressure","1013 hPa", "+12 hPa")

col3.latex('\int_a^b f(x)dx')
st.divider() # 구분선

'''
|이름|학번|학과|
|---|---|---|
|홍길동|20230001|컴퓨터공학과|
|김철수|20230002|전자공학과|
|이영희|20230003|기계공학과|
'''

'# :blue[Streamlit 그래프]'
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
    )

'#### :orange [st.area_chart()]'
st.area_chart(chart_data)

'#### :orange[st.line_chart()]'
st.line_chart(chart_data)

'#### :orange[st.bar_chart()]'
st.bar_chart(chart_data)

'#### :orange[st.scatter_chart()]'
st.scatter_chart(chart_data)

'#### :orange[st.map()]'
df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    columns=["lat", "lon"],
)
st.map(df)

st.divider() 

