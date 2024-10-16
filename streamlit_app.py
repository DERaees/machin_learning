import streamlit as st
import time
st.title('🤖 Machine Learning')

st.write('Hello world!')

def sidebar():
    st.sidebar.title("Sidebar Title")
    
    if st.sidebar.button('Cost Optimization', key="button1"):
        st.write('Cost Optimization clicked!')
        
    if st.sidebar.button('Security Optimization', key="button2"):
        st.write('Security Optimization clicked!')
        
    if st.sidebar.button('Performance Optimization', key="button3"):
        st.write('Performance Optimization clicked!')
      
def main():
    st.set_page_config(
        page_title="Custom Theme Streamlit App",
        page_icon=":memo:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Streamlit App with Custom Theme")
