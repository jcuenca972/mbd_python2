from app.data_models.EDATypes import EDATypes
from app.eda.EDAController import EDAController
from app.eda.EDAModel import EDAModel
from app.eda.EDAView import EDAView
from app.app_bar.app_bar import AppBarView
import streamlit as st

bar_view = AppBarView()
bar_view.show()

eda_view = EDAView()
eda_model = EDAModel()
eda_controller = EDAController(eda_view, eda_model)

st.title("Exploratory Data Analysis")
for eda in EDATypes:
    with st.expander(eda.value):
        eda_controller.show(st.container(), eda)


