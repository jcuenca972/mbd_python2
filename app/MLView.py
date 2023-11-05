import streamlit as st

class MLView:

    def __init__(self):
        self._main_container = None

    def init_container(self, general_container: st):
        self._main_container = general_container.container()

    def show_title(self):
        with self._main_container:
            st.title("ML Description")
            st.write("")
            st.write("")
