import streamlit as st

class HomeView:

    def __init__(self):
        self._main_container = None

    def init_container(self, general_container: st):
        with general_container.container():
            self._main_container = st.container()

    def show(self):
        st.image("img/landing.png")

        st.title("Empowering Urban Mobility: Data-Driven Bike-Sharing Solutions for Washington D.C.")

        st.header("The Challenge: Optimizing Bike-Sharing for a Dynamic City")
        st.write("Washington D.C.’s vibrant urban landscape is punctuated by the hum of cyclists navigating through its iconic streets. The city’s bike-sharing service has become integral to its transportation ecosystem, offering a sustainable and flexible option for residents and visitors alike. Yet, the efficient allocation of resources to meet fluctuating demand remains a pressing challenge. With ridership data from 2011 and 2012 at our disposal, we stand on the cusp of transforming how the Capital anticipates and fulfills its cycling needs.")

        st.header("Our Mission: Insightful Analysis for Strategic Service Enhancement")
        st.write("We delve deep into the heart of Washington’s cycling patterns, unlocking the story told by raw numbers. Our comprehensive web application will not only serve as a repository of historical data but also a lens into the city’s pulse. By understanding usage trends, peak times, and user preferences, we can inform strategic decisions to enhance service quality, reduce unnecessary costs, and ensure that every ride is a testament to the city’s commitment to exemplary public service.")

        st.header("The Solution: Predictive Modeling for Hourly Demand")
        st.write("Imagine a future where bike availability aligns seamlessly with rider demand, each hour, every day. Our predictive model, fueled by machine learning, is designed to forecast hourly bike usage with precision. This technological marvel will empower the Department of Transportation to proactively distribute bikes across the city, ensuring optimal service readiness. The outcome? A more sustainable model of bike-sharing that not only meets demand but also significantly reduces financial overhead by streamlining operations.")

        st.header("Interactive, Engaging, Enlightening: The Web Application")
        st.write("Our web application is not just a tool; it’s a gateway to understanding urban mobility. Interactive and user-friendly, it provides the Head of Transportation Services with real-time analytics, visualizations of complex data, and predictive insights. This digital platform is the embodiment of our commitment to harnessing the power of data to drive informed policymaking and operational excellence in bike-sharing services.")

        st.header("Join Us on the Journey to Smarter Mobility")
        st.write("We invite the administration of Washington D.C. to partner with us in this groundbreaking endeavor. Together, we will set a new standard for public transportation services, one pedal stroke at a time. Let’s ride towards a future of intelligent mobility, empowered by data and innovation.")
