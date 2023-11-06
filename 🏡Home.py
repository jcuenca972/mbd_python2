from app.app_bar.app_bar import AppBarView
from app.home.HomeController import HomeController
from app.home.HomeView import HomeView
import streamlit as st

# Creation of the App
if __name__ == "__main__":
    bar_view = AppBarView()
    bar_view.show()

    view = HomeView()
    controller = HomeController(view)
    controller.show()
