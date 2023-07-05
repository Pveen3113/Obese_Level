# This is a sample Python script.
# streamlit run --server.enableCORS false main.py
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit.components.v1 as components
import streamlit as st
import pandas as pd
import joblib
import numpy as np

#model = joblib.load("obeseLevelPred.joblib")
def predict(data):
    model = joblib.load('obeseLevelPred.joblib')
    prediction = model.predict(data)
    #print(prediction[0])
    return prediction[0]

def main():
    st.title('Obese Level Classification')
    gen = 0
    famhist = 0
    meals = 0.0
    smoke = 0
    water = 0
    physical = 0
    alcohol = 0
    # st.sidebar.title('Prediction App')
    # data_input = st.sidebar.text_input('Enter data:')
    # predict_button = st.sidebar.button('Predict')
    # testrun1 = [[0,	21.0,	1.62,	64.0,	1,	3.0	,0,	2.0	,0.0,3]]
    # print("lol: " , testrun1)
    genopt = st.radio( "Select your gender", options=["Male", "Female"])
    if(genopt == 'Male') : gen = 0
    if(genopt == 'Female') : gen = 1

    age_input = st.slider('How old are you?', 0, 100, 21)
    age = float(age_input)
    #st.write("I'm ", age, 'years old')

    height = st.number_input('State your height in metre')
    #st.write('The current number is ', height)

    weight = st.number_input('State your Weight in KG')
    #st.write('The current weight is ', weight)

    histopt = st.radio( "Does your family members has obesity history", options=["Yes", "No"])
    if(histopt == 'Yes') : famhist = 1
    if(histopt == 'No') : famhist = 0

    mealopt = st.selectbox(
        'How many meals do you have a day',
        ('One or Two', 'Three' , 'More Than Three'))
    if(mealopt=='One or Two') : meals = 1.0
    elif(mealopt=='Three') : meals = 2.0
    elif(mealopt=='More Than Three') : meals = 3.0

    smokeopt = st.radio( "Does you smoke", options=["Yes", "No"])
    if(smokeopt == 'Yes') : smoke = 1
    if(smokeopt == 'No') : smoke = 0

    water_input= 0
    wateropt = st.selectbox(
        'How much water do you consume a day',
        ('Less than a liter', 'Between 1 and 2L' , 'More Than 2L'))
    if(wateropt=='Less than a liter') : water_input = 1
    elif(wateropt=='Between 1 and 2L') : water_input = 2
    elif(wateropt=='More Than 2L') : water_input = 3
    water = float(water_input)


    physical_input= 0
    physicalopt = st.selectbox(
        'What is your physical activity frequency ?',
        ('Sedentary', 'Lightly active' , 'Moderately active', 'Very active'))
    if(physicalopt=='Sedentary') : physical_input = 0
    elif(physicalopt=='Lightly active') : physical_input = 1
    elif(physicalopt=='Moderately active') : physical_input = 2
    elif(physicalopt=='Very active') : physical_input = 3
    elif(physicalopt=='Extremely active') : physical_input = 3
    physical = float(physical_input)


    alcoholopt = st.selectbox(
        'How frequently do you consume alcohol',
        ('Always', 'Frequently' , 'Sometimes', 'Not at all'))
    if(alcoholopt=='Always') : alcohol = 0
    elif(alcoholopt=='Frequently') : alcohol = 1
    elif(alcoholopt=='Sometimes') : alcohol = 2
    elif(alcoholopt=='Not at all') : alcohol = 3




    #(st.write( 'Chosen :' , genopt))
    #age = 21.0
    #height = 1.62
    #weight = 64.0
    #famhist = 1
    #meals = 3.0
    #smoke = 0
    #water = 2.0
    #physical = 0.0
    #alcohol = 3
    testrun = [[gen, age, height, weight, famhist, meals, smoke, water, physical, alcohol]]
    print("lol2: " , testrun)

    if st.button("Predict"):
        prediction = predict(testrun)
        #st.write(prediction)
        st.write( predict(testrun))


    #st.write( predict(testrun))


if __name__ == '__main__':
    main()