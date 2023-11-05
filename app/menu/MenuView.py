import streamlit as st
from app.data.EDATypes import EDATypes
from app.eda.EDAController import EDAController
from app.predictions.PredictionsController import PredictionsController
from app.ml_description.MLController import MLController

class MenuView:

    _eda_charts = dict()

    def __init__(self, eda_controller: EDAController, predictions_controller: PredictionsController,
                 ml_controller: MLController):
        self._radio_placeholder = None
        self._eda_controller = eda_controller
        self._predictions_controller = predictions_controller
        self._eda_title = "EDA"
        self._predictions_title = "Predictions"
        self._logo = "img/logo.png"
        self._container = st.empty()
        self._radio_key = "radio_key"
        self._ml_controller = ml_controller
        self._ml_title = "Model Creation"

    def show(self):
        st.sidebar.image(self._logo)

        st.sidebar.markdown("# Bike Sharing App")

        # Cache Management
        if self._eda_title not in st.session_state:
            st.session_state[self._eda_title] = True
        if self._predictions_title not in st.session_state:
            st.session_state[self._predictions_title] = False
        if self._ml_title not in st.session_state:
            st.session_state[self._ml_title] = False
        if self._radio_key not in st.session_state:
            st.session_state[self._radio_key] = 0

        # EDA View Management
        if st.sidebar.button(self._eda_title):
            st.session_state[self._predictions_title] = False
            st.session_state[self._ml_title] = False
            st.session_state[self._eda_title] = True
            st.session_state[self._radio_key] += 1

        self._radio_placeholder = st.sidebar.empty()
        if st.session_state[self._eda_title]:
            eda_selection = self._radio_placeholder.radio(
                "Charts",
                [eda.value for eda in EDATypes],
                key=f"radio_{st.session_state[self._radio_key]}"
            )
            for eda in EDATypes:
                if eda_selection == eda.value:
                    self._eda_controller.show(self._container, eda)

        # ML Model Description
        if st.sidebar.button(self._ml_title):
            st.session_state[self._eda_title] = False
            st.session_state[self._ml_title] = True
            st.session_state[self._predictions_title] = False
            self._radio_placeholder.empty()

        # Predictions Management
        if st.sidebar.button(self._predictions_title):
            st.session_state[self._eda_title] = False
            st.session_state[self._ml_title] = False
            st.session_state[self._predictions_title] = True
            self._radio_placeholder.empty()

        if st.session_state[self._predictions_title]:
            self._predictions_controller.show(self._container)

        if st.session_state[self._ml_title]:
            self._ml_controller.show(self._container)

        # Credits
        st.sidebar.markdown("### Team Members:")
        st.sidebar.markdown("""
        * ALAN CORRALES CORTEZ
        * JAVIER TORRES
        * JOSÉ MANUEL CUENCA LERMA
        * MORITZ VON DITFURTH
        * OMAR ALTARAKIEH
        * REGINA DE ALBA
        """)
