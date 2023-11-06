from app.ml_description.MLController import MLController
from app.ml_description.MLModel import MLModel
from app.ml_description.MLView import MLView
from app.app_bar.app_bar import AppBarView
import streamlit as st

bar_view = AppBarView()
bar_view.show()

ml_view = MLView()
ml_model = MLModel()
ml_controller = MLController(ml_view, ml_model)

ml_controller.show(st.container())
