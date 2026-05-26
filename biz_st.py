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
video_file = open("./data/성당.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

st.divider() # 구분선
