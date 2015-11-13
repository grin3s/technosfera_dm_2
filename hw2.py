import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar_counts(data):
    fig = plt.figure(figsize=(20,10))
    plt.yticks(fontsize=8)
    plt.xticks(rotation=90)
    sns.barplot(x=grouped_agency_count.keys().values,y=grouped_agency_count.values)
    plt.xlabel('')
    plt.ylabel('Number of jobs',fontsize=10)

dataset = pd.read_csv('NYC_Jobs.csv')
grouped_agency = dataset.groupby('Agency')
grouped_agency_count = grouped_agency.size().sort_values(ascending=False)
plot_bar_counts(grouped_agency_count)

