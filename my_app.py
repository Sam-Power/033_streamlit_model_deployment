import streamlit as st
import pickle
import pandas as pd


st.title('Car Prediction')
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML App </h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

modelxg = pickle.load(open('xgb_model','rb'))
modelrf = pickle.load(open('rf_model','rb'))


age = st.sidebar.selectbox("what is age of car",(1,2,3),0)
hp = st.sidebar.slider("What is the hp of car", 60,200,100,step=5)
km=st.sidebar.slider("What is the km of your car", 0,100000,50000, step=500)
car_model=st.sidebar.selectbox("Select model of your car", ('A1', 'A2', 'A3','Astra','Clio','Corsa','Espace','Insignia'),2)

my_dict = {
    "age": age,
    "hp": hp,
    "km": km,
    "model": car_model
}

df = pd.DataFrame.from_dict([my_dict])

columns = ['age','hp','km','model_A1',
'model_A2','model_A3','model_Astra',
'model_Clio','model_Corsa','model_Espace',
'model_Insignia']

df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
#st.table(df)
choice = st.selectbox("Select Your Model", ('XGBoost', 'RandomForest'))
if choice == 'XGBoost':
	prediction = modelxg.predict(df)
elif choice == 'RandomForest':
	prediction = modelrf.predict(df)

st.markdown("This configuration of your car is below")
st.table(pd.DataFrame.from_dict([my_dict]))

st.write("Press 'Predict' when configuration is set")
if st.button('Predict'):
	st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))












