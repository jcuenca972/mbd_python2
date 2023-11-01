from app.MenuView import MenuView
from app.GeneralView import GeneralView
from app.MenuController import MenuController
from app.EDAController import EDAController
from app.PredictionsController import PredictionsController
from app.EDAModel import EDAModel

if __name__ == "__main__":
    view = GeneralView()

    eda_model = EDAModel()
    eda_controller = EDAController(view, eda_model)

    predictions_controller = PredictionsController(view)

    menu_view = MenuView(eda_controller, predictions_controller)
    menu_controller = MenuController(menu_view)

    menu_controller.init_gui()
