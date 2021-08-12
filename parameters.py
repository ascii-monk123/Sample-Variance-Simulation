import streamlit as st



def app():
    #save to session state
    def save():
        st.write(st.session_state.iters)
        st.write(st.session_state.samples)
        st.write(st.session_state.speed)
     #form to be displayed
    with st.form(key='my_form'):
        iterations = st.number_input('Iterations',min_value=1000,key="iters")
        samples = st.number_input('Population Size',min_value=100, key="samples")
        #waiting time after each iterattion
        speed=st.slider('Iteration waiting time (in seconds)',min_value=0.01,max_value=1.0,key="speed")
        submit_button = st.form_submit_button(label='Set Params', on_click=save)