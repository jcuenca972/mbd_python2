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

    def write_number_inputs(self, *input_names):
        input_numbers = []
        with self._main_container:
            for name in input_names:
                number = st.number_input(name, min_value=0)
                input_numbers.append(number)
        return tuple(input_numbers)

    def write_binary_select_inputs(self, *input_names):
        options = {
            'False': 0,
            'True': 1
        }
        input_numbers = []
        with self._main_container:
            for name in input_names:
                selected_label = st.selectbox(name, options.keys())
                input_numbers.append(options[selected_label])

        return tuple(input_numbers)

    def plotly_show(self, fig):
        with self._main_container:
            st.plotly_chart(fig, use_container_width=True)

    def write_text(self, text):
        with self._main_container:
            st.write(text)