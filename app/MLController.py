from app.MLView import MLView

class MLController:

    def __init__(self, view: MLView):
        self._view = view

    def show(self, container):
        self._view.init_container(container)
        self._view.show_title()
