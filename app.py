import streamlit as st
import sample_variance
import information
import parameters

Pages={
    "Problem Statement":information,
    "Simulation":sample_variance,
    "Parameters":parameters

}

st.sidebar.title("Contents")
selection=st.sidebar.radio("Go to",list(Pages.keys()))
page=Pages[selection]
page.app()