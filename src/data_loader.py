import pandas as pd
import os

def dataLoader():
    basePath = os.path.dirname(os.path.dirname(__file__))
    dataPath = os.path.join(basePath,"data","Traffic.csv")

    df = pd.read_csv(dataPath)
    return df