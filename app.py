import streamlit as st
import joblib

st.set_page_config(page_title='Iris classification ',page_icon='👽')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
	content:'Made with ❤️ by om pramod'; 
	visibility: visible ;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Flower Classification</h2>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)

st.image("app.png")

st.markdown("*****")

SepalLengthCm = st.slider("select length of sepal (in cm)",4.3,7.9)
SepalWidthCm =  st.slider("select width of sepal (in cm)",2.0,4.4)
PetalLengthCm =  st.slider("select length of petal (in cm)",1.0,6.9)
PetalWidthCm =  st.slider("select width of petal (in cm)",0.1,2.5)

mj = joblib.load("mymodel_joblib")

prediction = mj.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])

if st.button("classify") :
    st.markdown("*****")
    st.success(prediction[0])