import streamlit as st

class GeneralView:

    def __init__(self):
        self._top_container = None
        self._main_container = None
        self._bottom_container = None

    def init_container(self, general_container: st, columns_num=1):
        with general_container.container():
            with st.container():
                self._top_container = st.container()
                self._main_container = st.columns(columns_num)
                self._bottom_container = st.container()

    def write_titles(self, title: str, instructions: str, num_column=0):
        with self._main_container[num_column]:
            st.title(title)
            st.header(instructions)

    def write_titles_top(self, title: str, instructions: str):
        with self._top_container:
            st.title(title)
            if instructions != "":
                st.header(instructions)

    def write_number_input(self, name, num_column=0):
        with self._main_container[num_column]:
            value = st.number_input(name, min_value=0.0, step=1.0)
        return value

    def write_selector(self, label, start, num_column=0, *input_names):
        options = dict()
        for index, name in enumerate(input_names):
            options[name] = index + start
        with self._main_container[num_column]:
            selected_label = st.selectbox(label, options.keys())
            value_return = options[selected_label]
        return value_return

    def plotly_show(self, fig, num_column=0):
        with self._main_container[num_column]:
            st.plotly_chart(fig, use_container_width=True)

    def write_text(self, text, num_column=0):
        with self._main_container[num_column]:
            st.write(text)

    def write_text_bottom(self, text):
        with self._bottom_container:
            st.write(text)

    def write_slider(self, label, start, finish, step, num_column=0):
        with self._main_container[num_column]:
            value = st.slider(label, start, finish, step)
        return value

    def write_header(self, text, num_column=0):
        with self._main_container[num_column]:
            st.header(text)

    def write_header_top(self, text):
        with self._top_container:
            st.header(text)
