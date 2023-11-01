from app.MenuView import MenuView
from app.GeneralView import GeneralView
from app.MenuController import MenuController
from app.EDAController import EDAController
from app.PredictionsController import PredictionsController
from app.EDAModel import EDAModel
from app.PredictionsModel import PredictionsModel

# Creation of the App
if __name__ == "__main__":
    # Create GUI elements
    view = GeneralView()

    # Create Plotly Charts
    eda_model = EDAModel()
    # Manage GUI Elements and Charts
    eda_controller = EDAController(view, eda_model)

    # Create ML Objects
    predictions_model = PredictionsModel()
    # Manage GUI Elements and ML operations
    predictions_controller = PredictionsController(view, predictions_model)

    # Create GUI Menu and open screens
    menu_view = MenuView(eda_controller, predictions_controller)
    # Manage Menu Operations
    menu_controller = MenuController(menu_view)

    # Init App
    menu_controller.init_gui()
