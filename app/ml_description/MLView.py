import streamlit as st
from PIL import Image

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

    def show_model_highlights(self, links_pycaret, links_metrics):
        with self._main_container:
            st.header("Framework")
        self._show_pycaret_support(links_pycaret)
        with self._main_container:
            st.header("Metrics")
        self._show_metrics_support(links_metrics)


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

    def _show_metrics_support(self, links):
        with self._main_container:
            st.markdown(f"""
            After checking similar projects[[1]({links["1"]}), [2]({links["2"]}), [3]({links["3"]})], we decide to use the following metrics to compute the models performance: R^2, MAE and RMSE
            """)

    def show_model_creation(self, targets, cnt_models, cnt_error, cnt_metrics,
                            casual_models, casual_error, casual_metrics,
                            registered_models, registered_error, registered_metrics):
        with self._main_container:
            st.header("Regression Targets")
            st.write(targets)
            st.header("Model for 'cnt'")
            st.write(cnt_models)
            st.image(Image.open(cnt_error), caption="CNT Error Graph")
            st.write("Test Results")
            st.write(cnt_metrics)
            # st.header("Model for 'casual'")
            # st.write(casual_models)
            # st.image(Image.open(casual_error), caption="Casual Error Graph")
            # st.write("Test Results")
            # st.write(casual_metrics)
            # st.header("Model for 'registered'")
            # st.write(registered_models)
            # st.image(Image.open(registered_error), caption="Registered Error Graph")
            # st.write("Test Results")
            # st.write(registered_metrics)

    def show_software_architecture(self, img):
        with self._main_container:
            st.header("Software Architecture")
            st.image(Image.open(img), caption="")
