from src.data_loader import dataLoader
from src.feature_engineering import featureEngineering
from src.visualization import visualization
from src.traffic_model import trafficModel
from src.risk_analyzer import riskAnalyzer

df = dataLoader()
df = featureEngineering(df)
visualization(df)
trained_model,history,X_test,y_test = trafficModel(df)

sample = X_test.iloc[[0]] 
prediction = trained_model.predict(sample)
predicted_traffic = float(prediction[0][0])
hour = int(sample["hour"].iloc[0])
result = riskAnalyzer(predicted_traffic, hour)
trained_model.save("models/traffic_model.h5")

day_num = int(sample["day_of_week"].iloc[0])

day_map_reverse = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

day_name = day_map_reverse[day_num]
print("AI Prediction")
print(f"Saat: {hour}")
print(f"Gün: {day_name}")
print("\nAI tahmin:")
print(f"Traffic Volume -> {predicted_traffic:.2f}")
print(f"\nRisk : {result}")
