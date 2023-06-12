import streamlit as st
import logging

def startRecording():
        logging.info(f"startRecording called.")
        session_variable_name = "recordingStarted"
        if not does_session_variable_exist(session_variable_name):
                st.session_state[session_variable_name] = ''
        st.session_state[session_variable_name] = True

def update_session_state(key_name, value):
        if key_name not in st.session_state:
                st.session_state[key_name] = value
        else:
                st.session_state[key_name] = value
                
def updateElapsedTime(value):
        logging.info(f"updateElapsedTime : {value}")
        session_variable_name = "elapsedTime"
        if not does_session_variable_exist(session_variable_name):
                st.session_state[session_variable_name] = ''
        st.session_state[session_variable_name] = value
        
def does_session_variable_exist(key_name):
        if key_name not in st.session_state:
                return False
        else:
                return True
                
def calculateTimeElapsed():
            minutes = total_time_in_seconds//60
            seconds = total_time_in_seconds%60
            progress_value = total_time_in_seconds%100
            mm, ss = minutes, seconds
                            
st.write(st.session_state)
single_element_container = st.empty()
record_button = single_element_container.button("Press to record", on_click=startRecording)

if record_button:
        single_element_container.empty()
        #multi_elements_container = st.container()
        #multi_elements_container.button("Stop")
        #multi_elements_container.button("Pause")
        multi_elements_container1, multi_elements_container2 = st.columns([1,3])
        
        with multi_elements_container1:
                metric_container = st.empty()
                elapsed_time_in_seconds = 0
                metric_container.metric("Recording...", "00:00")
                updateElapsedTime(elapsed_time_in_seconds)
        with multi_elements_container2:
                progress_bar_container = st.empty()
                progress_bar_container.progress(50, text="")
                multi_elements_container21, multi_elements_container22 = multi_elements_container2.columns(2)
                multi_elements_container21.button("Stop")
                multi_elements_container22.button("Pause")
        
