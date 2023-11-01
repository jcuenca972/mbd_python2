from app.MenuView import MenuView
from app.GeneralView import GeneralView
from app.AppController import AppController

if __name__ == "__main__":
    menu_view = MenuView()
    general_view = GeneralView()
    controller = AppController(general_view, menu_view)
    controller.init_gui()
