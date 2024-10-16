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

if __name__ == "__main__":
    # main()
    time.sleep(2)
    sidebar()

    # Add inline CSS to style the sidebar and main content area
    st.markdown(
        """
        <style>
        .sidebar {
            background-color: yellow;
            padding: 10px;
        }
        .css-1gkm2gq {
            background-color: yellow !important;
        }
        .main {
            background-color: purple;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
