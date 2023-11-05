from app.menu.MenuView import MenuView

class MenuController:

    def __init__(self, menu_view: MenuView):
        self._view = menu_view

    def init_gui(self):
        self._view.show()
