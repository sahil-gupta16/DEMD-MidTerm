from copyreg import pickle
from os import lseek
from flask import Flask, request
import streamlit as st
import pickle
from sklearn.linear_model import LogisticRegression

pickled_model_file = open("pickle_wine_model.pkl", "rb")
classifier = pickle.load(pickled_model_file)

def predict_wine():

    try :
        st.title("Model Deployment")
        f1 = st.text_input("Feature 1 :")
        f2 = st.text_input("Feature 2 :")
        f3 = st.text_input("Feature 3 :")
        f4 = st.text_input("Feature 4 :")
        f5 = st.text_input("Feature 5 :")
        f6 = st.text_input("Feature 6 :")
        f7 = st.text_input("Feature 7 :")
        f8 = st.text_input("Feature 8 :")
        f9 = st.text_input("Feature 9 :")
        f10 = st.text_input("Feature 10 :")
        f11 = st.text_input("Feature 11 :")
        f12 = st.text_input("Feature 12 :")
        f13 = st.text_input("Feature 13 :")

        


        result = classifier.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]])

        if st.button("Print output"):
            st.success(result)
    except Exception as e :
        return f" Error occured with message : {e}"

if __name__=="__main__":
    predict_wine()