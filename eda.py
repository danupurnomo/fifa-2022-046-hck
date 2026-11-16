import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px

def run():
    # Membuat Title
    st.title('Aplikasi Prediksi Rating Pemain FIFA 2022')

    # Membuat Sub Header
    st.subheader('Page ini berisi Exploratory Data Analysis')

    # Menulis baris
    st.write('By *Danu Purnomo*')
    st.write('# Hello')
    st.write('## Hello')

    # Memasukkan Dataset
    df = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.4/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(df)

    # Memasukkan Gambar
    img = Image.open('soccer.jpg')
    st.image(img, caption='EDA FIFA 2022')

    # Menampilkan Histogram of Rating
    st.write('### Histogram of Rating')
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df['Overall'], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Histogram berdasarkan input user
    st.write('### Histogram berdasarkan input user')
    fig = plt.figure(figsize=(15, 5))
    opsi = st.selectbox('Pilih Column', ('Weight', 'Height', 'ShootingTotal'))
    sns.histplot(df[opsi], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat Plotly Plot
    st.write('### Plotly Plot - Rating vs Price')
    fig = px.scatter(df, x='Overall', y='ValueEUR', hover_data=['Name', 'Age'])
    st.plotly_chart(fig)


if __name__ == '__main__':
    run()