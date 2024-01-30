# -*- coding:utf-8 -*-

import streamlit as st 
import matplotlib.pyplot as plt 

def main():
    v1=st.slider("number",0,100)
    st.write(v1)
    
    v2=st.sidebar.slider("number(sidebar)",0,100)
    st.sidebar.write(v2)
    
    with st.sidebar:
        v3=st.slider("number with sidebar",0,100)
        st.write(v3)
        
        st.markdown("Matplotlib")
        fig, ax=plt.subplots()
        ax.plot([1,2,3])
        st.pyplot(fig)
        
    fig, ax=plt.subplots()
    ax.plot([1,2,3])
    st.pyplot(fig)
    

if __name__ == "__main__":
    main()
    