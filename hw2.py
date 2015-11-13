import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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

dataset = pd.read_csv('NYC_Jobs.csv')
grouped_agency = dataset.groupby('Agency')
grouped_agency_count = grouped_agency.size().sort_values(ascending=False)
dataset['AvgSalary'] = (dataset['Salary Range From'] + dataset['Salary Range To']) / 2
plot_bar_counts(grouped_agency_count)

violin_plot_cat(dataset[dataset['Salary Frequency']=="Annual"],'Agency','AvgSalary',grouped_agency_count.keys().values)