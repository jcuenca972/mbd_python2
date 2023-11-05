import streamlit as st

class MLView:

    def __init__(self):
        self._main_container = None

    def init_container(self, general_container: st):
        with general_container.container():
            self._main_container = st.container()

    def show_title(self):
        with self._main_container:
            st.title("ML Description")
            st.write("")
            st.write("")
