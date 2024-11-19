# 예측 모델 웹앱 만들기
import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model.pkl')

# 2.모델 설명
st.title('학생들의 수면의 질 예측 프로그램')
st.subheader('당신의 수면의 질을 예측해드립니다!')
st.write(' 모델 설명 ')
st.write(' - 기계학습 알고리즘 : 선형회귀 ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/datasets/arsalanjamal002/student-sleep-patterns')
st.write(' - 훈련    데이터 : 350건')
st.write(' - 테스트 데이터 : 150건')
st.write(' - 인공지능 모델 정확도 : ')

# 3.데이터 시각화
col1, col2, col3 = st.columns(2)  
with col1:
      st.subheader('데이터시각화1')
      st.image('시각화1.png' )   # 이미지 불러오기
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화2.png' )   # 이미지 불러오기

# 4.모델 활용
st.subheader('모델 활용')
st.write('**** 다음을 입력하세요.. 인공지능이 당신의 수면의 질을 알려드립니다! ')
st.write('**** 당신이 입력한 데이터는 다른 목적으로 절대 사용되지 않습니다. ')

a = st.number_input(' 수강과목수 입력 ', value=0)      #초기값은 0
b = st.number_input(' 공부시간 입력 ', value=0.0 )     # 초기값은 0.0
c = st.selectbox('공지확인 입력(확인한다:0, 확인하지않는다:1', [0,1])
                                                            # 사용자가  0,1 중에 선택

if st.button('점수예측'):            # 사용자가 '점수예측' 버튼을 누르면
        input_data = [[a,b,c]]     # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
        st.write('인공지능의 예측 점수는', p)
