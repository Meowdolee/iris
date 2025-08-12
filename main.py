import streamlit as st
import joblib

pg = st.navigation([
    st.Page('pages/p1.py', title = 'Iris 相關資訊', icon='🌸'),
    st.Page('pages/p2.py', title = '品種預測', icon='🌕')
])
pg.run()
