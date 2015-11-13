import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
import pickle

GOOGLE_API_KEY = "AIzaSyDd8Ybx4xStlfY927OC6DcCzhYnkTWlwxw"
GOOGLE_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address="{0}"&key={1}'

LOAD_FROM_FILE = True


def plot_bar_counts(data):
    fig = plt.figure(figsize=(20,10))
    plt.yticks(fontsize=8)
    plt.xticks(rotation=90)
    sns.barplot(x=data.keys().values,y=data.values)
    plt.xlabel('')
    plt.ylabel('Number of jobs',fontsize=10)


def violin_plot_cat(data, cat, val, order):
    fig = plt.figure(figsize=(20,10))
    sns.boxplot(x=val, y=cat, data=data, order=order)
    sns.stripplot(x=val, y=cat, data=data, jitter=True, size=4, order=order);


def fetch_location(location):
    full_url = GOOGLE_API_URL.format(location, GOOGLE_API_KEY);
    answer = requests.get(full_url).json()
    results = answer['results']
    if len(results) > 0:
        position = results[0]['geometry']['location']
        return position['lat'], position['lng']
    else:
        return None


def get_all_locations(data):
    res = dict()
    all_locations = data.groupby('Work Location').groups.keys()
    for idx, location in enumerate(all_locations):
        print "{0} out of {1}".format(idx, len(all_locations))
        pos = fetch_location(location)
        res[location] = pos

    return res

dataset = pd.read_csv('NYC_Jobs.csv')
grouped_agency = dataset.groupby('Agency')
grouped_agency_count = grouped_agency.size().sort_values(ascending=False)
dataset['AvgSalary'] = (dataset['Salary Range From'] + dataset['Salary Range To']) / 2
locations = get_all_locations(dataset)
#plot_bar_counts(grouped_agency_count)

#violin_plot_cat(dataset[dataset['Salary Frequency']=="Annual"],'Agency','AvgSalary',grouped_agency_count.keys().values)