import streamlit as st


def footer_home():

    name = "Swayam Borade"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items:align-center">
            <p style="font-weight:bold; color:white;"> Created with ❤️ by  <span style="color:black;"> {name} </span></p>
        </div>   
                
                """, unsafe_allow_html=True)
    
def footer_dashboard():

    name = "Swayam Borade"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items:align-center">
            <p style="font-weight:bold; color:black;"> Created with ❤️ by  <span style="color:red;"> {name} </span></p>
        </div>   
                
                """, unsafe_allow_html=True)
