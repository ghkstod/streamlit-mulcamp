# -*- coding:utf-8 -*-

import streamlit as st 
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as ex
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly


@st.cache_data #decorator 
def load_data():
    #df=sns.load_dataset('iris')
    df=sns.load_dataset('tips')
    return df

def main():
    tips=load_data()
    fig, ax=plt.subplots()
    ax.plot(tips['tip'])
    ax.set_title('A')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    st.pyplot(fig)
    
    fig, ax = plt.subplots()
    sns.lineplot(tips['tip'])
    st.pyplot(fig)
    
    fig=go.Figure()
    fig.add_trace(go.Line(y=tips['tip']))
    st.plotly_chart(fig,use_container_width=True)
    
    
if __name__ == "__main__":
    main()