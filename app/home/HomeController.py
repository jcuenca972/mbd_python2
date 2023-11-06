from app.home.HomeView import HomeView

class HomeController:

    def __init__(self, view: HomeView):
        self._view = view

    def show(self):
        self._view.show()