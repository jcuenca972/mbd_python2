import streamlit as st

class AppBarView:

    def show(self):
        st.set_page_config(
            page_title="Python 2",
            page_icon="🚲",
        )
        st.sidebar.image("img/logo.png")

        st.sidebar.markdown("### Team Members:")
        st.sidebar.markdown("""
                * ALAN CORRALES CORTEZ
                * JAVIER TORRES
                * JOSÉ MANUEL CUENCA LERMA
                * MORITZ VON DITFURTH
                * OMAR ALTARAKIEH
                * REGINA DE ALBA
                """)