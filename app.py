#python -m venv streamlit_env
#cd streamlit_env
#.\Scripts\activate
#mkdir src
#cd src  
#pip install streamlit
#streamlit hello
#streamlit run app.py
#pip install numpy
#pip install pickle  




import streamlit as st
import numpy as np
import pickle
from sklearn.exceptions import InconsistentVersionWarning
import warnings
warnings.simplefilter("error", InconsistentVersionWarning)
from sklearn.ensemble import RandomForestClassifier


model = pickle.load(open("model_RandomForest.sav", "rb"))

def make_prediction(input_data):
    input_data = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_data) 
    print(prediction)
    return prediction[0]

def main():
    st.title("Heart Attack Prediction")

    with st.form("heart_attack_prediction"):

        age = st.number_input("Enter your age", min_value=0, max_value=100, value=20)
        st.write(f"Your age is {age}")
        sex = st.selectbox("Select your sex", ["1=Male", "0=Female"],[1,0])
        st.write(f"Your sex is {sex}")
        cp = st.selectbox("Select your chest pain type", ["1=Typical Angina", "2=Atypical Angina", "3=Non-Anginal Pain", "4=Asymptomatic"],[1,2,3,4])
        st.write(f"Your chest pain type is {cp}")
        trtbps = st.number_input("Enter your resting blood pressure", min_value=0, max_value=200, value=120)
        st.write(f"Your resting blood pressure is {trtbps}")
        chol = st.number_input("Enter your cholesterol level", min_value=0, max_value=600, value=200)
        st.write(f"Your cholesterol level is {chol}")
        fbs = st.selectbox("Select your fasting blood sugar level", ["1=Yes", "0=No"],[1,0])
        st.write(f"Your fasting blood sugar level is {fbs}")
        rest_ecg = st.selectbox("Select your resting electrocardiographic results", ["1=Normal", "2=ST-T Wave Abnormality", "3=Left Ventricular Hypertrophy"],[1,2,3])
        st.write(f"Your resting electrocardiographic results are {rest_ecg}")
        thalach = st.number_input("Enter your maximum heart rate achieved", min_value=0, max_value=200, value=150)
        st.write(f"Your maximum heart rate achieved is {thalach}")
        exang = st.selectbox("Select if you have exercise induced angina", ["1=Yes", "0=No"],[1,0])
        st.write(f"You have exercise induced angina: {exang}")
        oldpeak = st.number_input("Enter your ST depression induced by exercise relative to rest", min_value=0, max_value=10, value=0)
        st.write(f"Your ST depression induced by exercise relative to rest is {oldpeak}")
        slp = st.selectbox("Select your slope of the peak exercise ST segment", ["1=Upsloping", "2=Flat", "3=Downsloping"],[1,2,3])
        st.write(f"Your slope of the peak exercise ST segment is {slp}")
        caa = st.number_input("Enter your number of major vessels (0-3) colored by flourosopy", min_value=0, max_value=3, value=0)
        st.write(f"Your number of major vessels colored by flourosopy is {caa}")
        thall = st.selectbox("Select your thalassemia", ["1=Normal", "2=Fixed Defect", "3=Reversable Defect"],[1,2,3])
        st.write(f"Your thalassemia is {thall}") 

        submit_button = st.form_submit_button(label="Predict")

        if submit_button:
            input_data = [age, sex, cp, trtbps, chol, fbs, rest_ecg, thalach, exang, oldpeak, slp, caa, thall]
            prediction = make_prediction(input_data)
            if prediction == 1:
                st.error("You are likely to have a heart attack")
            else:
                st.success("You are unlikely to have a heart attack")



if __name__ == "__main__":
    main()
