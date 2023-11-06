import streamlit as st

class GeneralView:

    def __init__(self):
        self._main_container = None

    def init_container(self, general_container: st):
        with general_container.container():
            self._main_container = st.container()

    def write_titles(self, title: str, instructions: str):
        with self._main_container:
            st.title(title)
            st.header(instructions)

    def write_number_input(self, name):
        with self._main_container:
            value = st.number_input(name, min_value=0.0, step=1.0)
        return value

    def write_selector(self, label, start, *input_names):
        options = dict()
        for index, name in enumerate(input_names):
            options[name] = index + start
        with self._main_container:
            selected_label = st.selectbox(label, options.keys())
            value_return = options[selected_label]
        return value_return

    def plotly_show(self, fig):
        with self._main_container:
            st.plotly_chart(fig, use_container_width=True)

    def write_text(self, text):
        with self._main_container:
            st.write(text)

    def write_slider(self, label, start, finish, step):
        with self._main_container:
            value = st.slider(label, start, finish, step)
        return value

    def write_header(self, text):
        with self._main_container:
            st.header(text)
