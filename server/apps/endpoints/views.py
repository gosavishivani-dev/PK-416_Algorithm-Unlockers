from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.shortcuts import render
#import pylab
import pandas as pd
from datetime import datetime
import warnings
import csv
import json


# Create your views here.
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)

@api_view(["POST"])
def predict_cropArrival(request):
    try:
        commodity = request.data.get('commodity',None)
        data = pd.read_csv("research/Arrival.csv", index_col ="Commodity")
        s=data.loc[[commodity]]
        s.to_csv("Arrival_1.csv", sep=',')
        data1 = pd.read_csv("Arrival_1.csv")
        
        pd.options.mode.chained_assignment = None
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        output =[]
        with open("Arrival_1.csv",'r') as f:
            reader = csv.DictReader(f)
            for records in reader:
                output.append(records)
        with open("RecordsJson.json",'w')as outfile:
            json.dump(output,outfile,sort_keys=True, indent=4)
        with open("RecordsJson.json",'r')as infile:
            indata = json.load(infile)
        
        fields = [commodity]
        if not None in fields:
            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : indata
        }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'
        }
    except Exception as e:
        predictions = {
        'error' : '2',
            "message": str(e)
        }
    
    return Response(predictions)


#@api_view(["POST"])
@api_view(['GET'])
def predict_pricePredict(request):
    try:
        market='Bengaluru'
        commodity='Onion'
        data = pd.read_csv("price_predict_1.csv", index_col ="Market")
        s=data.loc[[market]]
        s.to_csv("Modal_23.csv", sep=',')
        data1 = pd.read_csv("Modal_23.csv", index_col ="Commodity")
        t=data1.loc[[commodity]]
        t.to_csv("Modal_234.csv", sep=',')
        data2 = pd.read_csv("Modal_234.csv")
        data2 = data2.drop(data2.columns.difference(["Date","Commodity","Modal","Market"]), axis=1)
        print(data2)
        data2.to_csv("Modal_1_1.csv",sep=',')
        pd.options.mode.chained_assignment = None
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        output =[]
        with open("Modal_1_1.csv",'r') as f:
                    reader = csv.DictReader(f)
                    for records in reader:
                        output.append(records)
        with open("RecordsJsonModal.json",'w')as outfile:
            json.dump(output,outfile,sort_keys=True, indent=4)
        with open("RecordsJsonModal.json",'r')as infile:
            indata = json.load(infile)
        
        
        fields = [commodity]
        if not None in fields:
            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : indata
        }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'
    }
    except Exception as e:
        predictions = {
        'error' : '2',
            "message": str(e)
    }
    #print(predictions)
    return Response(predictions)

@api_view(["POST"])
def predict_psfPredict(request):
    try:
        commodity = request.data.get('commodity',None)
        data = pd.read_csv("research/Price_Final.csv", index_col ="Commodity")
        s=data.loc[[commodity]]
        s.to_csv("Price_Final_2.csv", sep=',')
        data1 = pd.read_csv("Price_Final_2.csv")
        
        pd.options.mode.chained_assignment = None
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        output =[]
        with open("Price_Final_2.csv",'r') as f:
            reader = csv.DictReader(f)
            for records in reader:
                output.append(records)
        with open("RecordsJsonModal3.json",'w')as outfile:
            json.dump(output,outfile,sort_keys=True, indent=4)
        with open("RecordsJsonModal3.json",'r')as infile:
            indata = json.load(infile)
        
        fields = [commodity]
        if not None in fields:
            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : indata
        }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'
    }
    except Exception as e:
        predictions = {
        'error' : '2',
            "message": str(e)
    }
    
    return Response(predictions)
