# -*- coding:utf-8 -*-

import streamlit as st 
import seaborn as sns 
import pandas as pd 
import matplotlib.pyplot as plt


@st.cache_data #decorator 
def load_data():
    #df=sns.load_dataset('iris')
    df=sns.load_dataset('tips')
    return df

def main():
    st.write(st.__version__)
    st.write(sns.__version__)
    st.write(pd.__version__)
    
    tips=load_data()
    st.dataframe(tips,use_container_width=True)
    
    st.write("-"*50)
    st.title('st.numeric()')
    tip_max=tips['tip'].max()
    tip_min=tips['tip'].min()
    
    st.metric(label='tip high',value=tip_max,delta=tip_max-tip_min)
    st.metric(label='tip low',value=tip_min,delta=tip_min-tip_max)
    
if __name__ == "__main__":
    main()