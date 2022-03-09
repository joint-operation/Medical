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