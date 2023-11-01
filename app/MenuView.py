import streamlit as st
from app.data.EDATypes import EDATypes

class MenuView:

    _eda_charts = dict()

    def __init__(self):
        self._eda_title = "EDA"
        self._predictions_title = "Predictions"
        self._logo = "img/logo.png"

    def add_eda_chart(self):
        pass

    def show(self):
        st.sidebar.image(self._logo)

        st.sidebar.markdown("# Bike Sharing App")

        content_placeholder = st.empty()

        if self._eda_title not in st.session_state:
            st.session_state[self._eda_title] = True

        if st.sidebar.button(self._eda_title):
            st.session_state[self._eda_title] = True

        radio_placeholder = st.sidebar.empty()
        if st.session_state[self._eda_title]:
            eda_selection = radio_placeholder.radio("Charts", [eda.value for eda in EDATypes])
            for eda in EDATypes:
                title = eda.value
                if eda_selection == title:
                    content_placeholder.markdown(f"# {title}")

        if st.sidebar.button(self._predictions_title):
            st.session_state[self._eda_title] = False
            radio_placeholder.empty()
            content_placeholder.markdown("# ML Prediction")

        st.sidebar.markdown("### Team Members:")
        st.sidebar.markdown("""
        * ALAN CORRALES CORTEZ
        * JAVIER TORRES
        * JOSÉ MANUEL CUENCA LERMA
        * MORITZ VON DITFURTH
        * OMAR ALTARAKIEH
        * REGINA DE ALBA
        """)

