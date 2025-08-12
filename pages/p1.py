
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Iris 相關資訊')
df = pd.read_csv('iris.csv')
st.write(df.head())#展示前五筆資料

st.write('### Iris 樣品散布圖')
fig, ax = plt.subplots()
mapping = {'Setosa':0, 'Versicolor':1, 'Virginica':2}
colors = ['red', 'green', 'blue']
# 依tab顯示不同的分布情形
tab1, tab2 = st.tabs(['「依花萼長度」', '「依花萼寬度」'])

with tab1:
    for i, s in mapping.items():
        subset = df[df['variety'] == i]
        ax.scatter(subset['sepal.length'], subset['sepal.width'], label=i, c=colors[s])
    ax.set_xlabel('sepal.length')
    ax.set_ylabel('sepal.width')
    ax.legend()
    st.pyplot(fig)

fig2, ax2 = plt.subplots()
with tab2:
    for i, s in mapping.items():
        subset = df[df['variety'] == i]
        ax2.scatter(subset['petal.length'], subset['petal.width'], label=i, c=colors[s])
    ax2.set_xlabel('petal.length')
    ax2.set_ylabel('petal.width')
    ax2.legend()
    st.pyplot(fig2)