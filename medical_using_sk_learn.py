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
