import pandas as pd

def featureEngineering(df):
    df["Time"] = pd.to_datetime(df["Time"], format = "%I:%M:%S %p")
    df["hour"] = df["Time"].dt.hour

    # | Parça | Anlam           |
    # | ----- | --------------- |
    # | `%I`  | 12 saatlik saat |
    # | `%M`  | dakika          |
    # | `%S`  | saniye          |
    # | `%p`  | AM / PM         |
    day_map = {
        "Monday" : 0,
        "Tuesday" : 1,
        "Wednesday" : 2,
        "Thursday" : 3,
        "Friday" : 4,
        "Saturday" : 5,
        "Sunday" : 6
    }  
    df["day_of_week"] = df["Day of the week"].map(day_map)
    
    trafficSituation_map = {
        "low" : 0,
        "normal" : 1,
        "high" : 2,
        "heavy" : 3
    }

    df["traffic_situation"] = df["Traffic Situation"].map(trafficSituation_map)
    df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)  # haftasonu ise 1, haftaiçi ise 0 olur
    return df