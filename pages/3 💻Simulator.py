from app.simulator.SimulatorController import SimulatorController
from app.simulator.SimulatorModel import SimulatorModel
from app.simulator.SimulatorView import SimulatorView
from app.app_bar.app_bar import AppBarView
import streamlit as st

bar_view = AppBarView()
bar_view.show()

simulator_view = SimulatorView()
simulator_model = SimulatorModel()
simulator_controller = SimulatorController(simulator_view, simulator_model)

simulator_controller.show(st.container())
