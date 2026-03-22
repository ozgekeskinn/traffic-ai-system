import matplotlib.pyplot as plt
from src.data_loader import dataLoader
import pandas as pd
from src.feature_engineering import featureEngineering

def visualization(df):
    grouped = df.groupby("hour")["Total"].mean()  
    plt.plot(grouped.index, grouped.values, marker = 'o')
    plt.title("Traffic vs. Hour")
    plt.xlabel("Hour")
    plt.ylabel("Average Traffic Volume")
    plt.show()

    groupedDay = df.groupby("Day of the week")["Total"].sum()  
    order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    groupedDay = groupedDay.reindex(order)
    plt.bar(groupedDay.index , groupedDay.values)
    plt.title("Traffic for Days")
    plt.xlabel("Days")
    plt.ylabel("Average Traffic Volume")
    plt.show()

    trafficCount = df["Traffic Situation"].value_counts()
    order2 = ["low","normal","high","heavy"]
    trafficCount = trafficCount.reindex(order2)
    plt.bar(trafficCount.index, trafficCount.values)
    plt.title("Traffic Distribution")
    plt.xlabel("Traffic Situation")
    plt.ylabel("Counts")
    plt.show()
