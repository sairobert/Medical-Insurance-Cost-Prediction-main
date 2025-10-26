import streamlit as st
import pickle


pickle_in=open("xg_bicp.pkl","rb")
c=pickle.load(pickle_in)

def predict_output(age,sex,bmi,children,smoker,region):
    age = float(age)
    sex = float(sex)  
    bmi = float(bmi)
    children = float(children)
    smoker = float(smoker)  
    region = float(region) 
    res = c.predict([[age,sex,bmi,children,smoker,region]])
    return res

def main():
    st.title("Medical Insurance Cost Prediction")
    html="""
    <div style="background-color:blue">
    </div>"""
    st.markdown(html,unsafe_allow_html=True)
    age=st.text_input("AGE","Type Here")
    sex=st.text_input("SEX[Male=1,Female=0]","Type Here")
    bmi=st.text_input("BMI","Type Here")
    children=st.text_input("Number of childrens","Type Here")
    smoker=st.text_input("Smoker[Yes=1,No=0]","Type Here")
    region=st.text_input("Region[northeast=0,southeast=1,northwest=2,southwest=3]","Type Here")
    result=""
    if st.button("Predict Charges"):
        result=predict_output(age,sex,bmi,children,smoker,region)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()