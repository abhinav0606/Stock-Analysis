from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib,base64
from .Prediction import prediction
def home(requst):
    data=prediction("RELIANCE.NS")
    return render(requst,"index.html",data)