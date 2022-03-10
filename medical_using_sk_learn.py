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
    #inputs2 = new_df.drop('Disease',axis='columns')
    #target2["Disease"] = new_df['Disease']
    
    from sklearn.preprocessing import LabelEncoder
    le_disease = LabelEncoder()
    
    new_df["Diseases"] = le_disease.fit_transform(new_df['Disease'])
    
    inputs2 = new_df.drop('Disease',axis='columns')
    
    target2 = new_df['Diseases']
    
    inputs2 = inputs2.drop('Diseases',axis=1)
    
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(inputs2,target2,test_size=0.3)
    
    print("Test and Train data created")

    from sklearn import tree
    model = tree.DecisionTreeClassifier()
    model.fit(X_train,y_train)
    model.score(X_test,y_test)
    print("Model fitted ")
    print("Acurracy is ",model.score(X_test,y_test))
    desc = pd.read_csv("symptom_description.csv")
    desc.head()
    
    sev = pd.read_csv("symptom_severity.csv")
    sev.head()
    
    prec = pd.read_csv( "symptom_precaution.csv")
    prec.head()

    for ind,smp in enumerate(symptoms):

        try:
            symptoms[ind] = smp.strip(" ")
            
        except:
            pass
    return symptoms,    model, desc, sev, prec, col_names, le_disease

def predict(symptoms, model, desc, sev, prec, col_names, le_disease):
    print(len(symptoms))
    prd = [0]*(len(symptoms) - 1)
    