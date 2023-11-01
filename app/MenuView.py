import streamlit as st
from app.data.EDATypes import EDATypes
from app.EDAController import EDAController
from app.PredictionsController import PredictionsController

class MenuView:

    _eda_charts = dict()

    def __init__(self, eda_controller: EDAController, predictions_controller: PredictionsController):
        self._eda_controller = eda_controller
        self._predictions_controller = predictions_controller
        self._eda_title = "EDA"
        self._predictions_title = "Predictions"
        self._logo = "img/logo.png"
        self._container = st.empty()

    def _reset_container(self):
        self._container.empty()
        self._container = st.empty()

    def show(self):
        st.sidebar.image(self._logo)

        st.sidebar.markdown("# Bike Sharing App")

        if self._eda_title not in st.session_state:
            st.session_state[self._eda_title] = True

        if st.sidebar.button(self._eda_title):
            st.session_state[self._eda_title] = True

        radio_placeholder = st.sidebar.empty()
        if st.session_state[self._eda_title]:
            self._reset_container()
            eda_selection = radio_placeholder.radio("Charts", [eda.value for eda in EDATypes])
            for eda in EDATypes:
                if eda_selection == eda.value:
                    self._eda_controller.show(self._container, eda)

        if st.sidebar.button(self._predictions_title):
            st.session_state[self._eda_title] = False
            radio_placeholder.empty()
            self._reset_container()
            self._predictions_controller.show(self._container)

        st.sidebar.markdown("### Team Members:")
        st.sidebar.markdown("""
        * ALAN CORRALES CORTEZ
        * JAVIER TORRES
        * JOSÉ MANUEL CUENCA LERMA
        * MORITZ VON DITFURTH
        * OMAR ALTARAKIEH
        * REGINA DE ALBA
        """)

