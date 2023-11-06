from app.menu.MenuView import MenuView
from deprecated import deprecated

@deprecated("We are moving to streamlit pages")
class MenuController:

    def __init__(self, menu_view: MenuView):
        self._view = menu_view

    def init_gui(self):
        self._view.show()
