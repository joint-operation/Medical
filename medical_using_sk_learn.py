from pywebio.input import input, FLOAT, NUMBER, TEXT
from pywebio.output import put_text, put_markdown, put_loading, put_collapse, put_table, toast
import pandas as pd
import pywebio

x_symptoms = []

def symp_check(x):
    if x not in x_symptoms:
        return 'Try again !!'
def check_age(age):
    if age > 100:
        return 'Too old'
    elif age < 5:
        return 'Too young'
def count_check(c):
    if c > 17:
        return "Too many symptoms"
def modelling():
    
    df = pd.read_csv("dataset.csv")
    inputs = df.drop('Disease',axis='columns')
    target = df['Disease']   

    col_names = []
    for col in inputs.columns:
        col_names.append(col)
        
    symptoms = []
    for col in col_names:
        new = df.drop_duplicates(subset = [col])
        for ind in new.index:
            symptom = new[col][ind]
            if symptom not in symptoms and str(symptom) != "nan": #
                symptoms.append(symptom) 
    
    print("Please wait !!")
    print("Loading.....")
    symptoms.append("Disease")

    new_df = pd.DataFrame(columns = symptoms)
    
    for ind in df.index:
        smp = [0]*(len(symptoms)-1)
        for symp in col_names:
            val = df[symp][ind]
            if str(val) == "nan": #
                continue
            idx = symptoms.index(val)
            smp[idx] = 1
            
        smp.append(df["Disease"][ind])
        #print(len(smp),smp)
        new_df.loc[ind] = smp
    print("Dataset loaded...")