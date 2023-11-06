from app.menu.MenuView import MenuView
from app.eda.EDAView import EDAView
from app.menu.MenuController import MenuController
from app.eda.EDAController import EDAController
from app.simulator.SimulatorController import SimulatorController
from app.simulator.SimulatorView import SimulatorView
from app.eda.EDAModel import EDAModel
from app.simulator.SimulatorModel import SimulatorModel
from app.ml_description.MLView import MLView
from app.ml_description.MLController import MLController
from app.ml_description.MLModel import MLModel

# Creation of the App
if __name__ == "__main__":
    # Create GUI elements
    eda_view = EDAView()
    # Create Plotly Charts
    eda_model = EDAModel()
    # Manage GUI Elements and Charts
    eda_controller = EDAController(eda_view, eda_model)

    # Create ML Description
    ml_view = MLView()
    ml_model = MLModel()
    ml_controller = MLController(ml_view, ml_model)

    # Create ML Objects
    simulator_view = SimulatorView()
    simulator_model = SimulatorModel()
    # Manage GUI Elements and ML operations
    simulator_controller = SimulatorController(simulator_view, simulator_model)

    # Create GUI Menu and open screens
    menu_view = MenuView(eda_controller, simulator_controller, ml_controller)
    # Manage Menu Operations
    menu_controller = MenuController(menu_view)

    # Init App
    menu_controller.init_gui()
