import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title('Iris 品種預測')
# 載入模型
svm = joblib.load('models/svm.joblib')
knn = joblib.load('models/knn.joblib')
RF = joblib.load('models/RF.joblib')
LR = joblib.load('models/LR.joblib')

# 左側欄輸入：選擇模型
s1 = st.sidebar.selectbox('選擇模型', ['Support Vector Machine', 'K-Nearest Neighbors', 
                                   'Random Forest', 'Logistic Regression'])

if s1 == 'Support Vector Machine':
    model = svm
elif s1 == 'K-Nearest Neighbors':
    model = knn
elif s1 == 'Random Forest':
    model = RF
else:
    model = LR

st.image('iris.png')

# 接收使用著特徵輸入：4個特徵
df = pd.read_csv('iris.csv')
set1 = st.slider('花萼長度(cm)', 
                float(df['sepal.length'].min())-0.5,
                float(df['sepal.length'].max())+0.8,
                float(df['sepal.length'].mean()))
set2 = st.slider('花萼寬度(cm)', 
                float(df['sepal.width'].min())-0.5,
                float(df['sepal.width'].max())+0.8,
                float(df['sepal.width'].mean()))
set3 = st.slider('花瓣長度(cm)', 
                float(df['petal.length'].min())-0.5,
                float(df['petal.length'].max())+0.8,
                float(df['petal.length'].mean()))
set4 = st.slider('花瓣寬度(cm)', 
                float(df['petal.width'].min())-0.5,
                float(df['petal.width'].max())+0.8,
                float(df['petal.width'].mean()))

labels = ['Setosa', 'Versicolor', 'Virginica']
if st.button('進行預測'):
    X = np.array([[set1, set2, set3, set4]])
    y = model.predict(X)
    st.write(f'### 預測結果: {y}')
    st.write(f'### 品種名稱: {labels[y[0]]}')
    