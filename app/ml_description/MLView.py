import streamlit as st

class MLView:

    def __init__(self):
        self._main_container = None

    def init_container(self, general_container: st):
        with general_container.container():
            self._main_container = st.container()

    def show_title(self, title):
        with self._main_container:
            st.title(title)

    def show_data_highlighs(self, missing_values, continuos_plot,
                            correlation, daylight_code,
                            correlation_daylight):
        with self._main_container:
            st.header("Missing Values")
            st.write(missing_values)
            st.header("Plotting box plot for continuos variables")
            st.plotly_chart(continuos_plot)
            st.header("Correlation Heatmap of Bike Rental Dataset")
            st.pyplot(correlation)
            st.header("Calculate Daylight Hours")
            st.code(daylight_code)
            st.header("Correlation Heatmap of Bike Rental Dataset After Daylight")
            st.pyplot(correlation_daylight)

    def show_model_highlights(self, links):
        with self._main_container:
            st.header("Framework")
        self._show_pycaret_support(links)


    def _show_pycaret_support(self, links):
        with self._main_container:
            st.write("""
            Pycaret is an open source library to automatize the ML workflow. We choose this library because 
            it has been implemented in 2023 remarkable projects like: 
            """)
            st.markdown(f"""
            Bina Nusantara University used it in a project to predict Diabetes ([Indonesia]({links['Indonesia']})).
            Moreover, the National Taipei University of Technology observed that the auto-ML Pycaret model performed better than the XGBoost model ([Taiwan]({links['Taiwan']})).
            Additionaly, University of Sfax integred it in a system to predict positive cases of waterborne diseases ([Tunisia]({links['Tunisia']})).
            """)





