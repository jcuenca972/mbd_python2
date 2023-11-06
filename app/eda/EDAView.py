import streamlit as st

class EDAView:

    def __init__(self):
        self._main_container = None

    def init_container(self, general_container: st):
        with general_container.container():
            with st.container():
                self._main_container = st.container()

    def write_titles(self, title: str, instructions: str):
        with self._main_container:
            st.title(title)
            st.header(instructions)

    def plotly_show(self, fig):
        with self._main_container:
            st.plotly_chart(fig, use_container_width=True)

