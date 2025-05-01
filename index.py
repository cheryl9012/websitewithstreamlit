import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title = " Student Data Generator" , layout= "wide")

st.title("Student Data Generator")

names= ["Jennifer", "Aster" , "Anum" , "Tahira" , "Anosha" , "Genesis" ," Gillian", "Aliza", "Hadia", "Areej", "Zarka","Kinza"]

students=[]
for i in range(1,10):
    student = {
        "ID" : i,
        "Name" : random.choice(names),
        "Age" : random.randint(15, 25),
        "Grade" : random.choice(["A", "B", "C", "D", "E","F"])
    }
    students.append(student)

df = pd.DataFrame(students)
st.subheader("Generated Student Data")
st.dataframe(df)
csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button(label = "Download CSV" , data = df.to_csv(index=False) , file_name = "student_data.csv" , mime = "text/csv")
st.success("Students Record Generated Successfully")