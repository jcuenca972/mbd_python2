from app.GeneralView import GeneralView
from app.MenuView import MenuView

class AppController:

    def __init__(self, view: GeneralView, menu_view: MenuView):
        self._view = view
        self._menu_view = menu_view

    def init_gui(self):
        self._menu_view.show()
