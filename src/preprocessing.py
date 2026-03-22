import pandas as pd
from sklearn.model_selection import train_test_split
from src.feature_engineering import featureEngineering

def preprocessing(df):
    newDF = featureEngineering(df)
    
    X = newDF[["hour","day_of_week","is_weekend","CarCount","BikeCount","BusCount","TruckCount"]]
    y = newDF["Total"]

    X_train , X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)
    return X_train,X_test,y_train,y_test

# stratify=y kullanmamızın sebebi, train ve test veri setlerinde sınıf dağılımını korumaktır.
# Yani target (traffic_situation) içindeki low, normal, high, heavy sınıflarının oranı
# hem train hem test setinde aynı kalır.
# Eğer stratify kullanılmazsa, bazı sınıflar test setinde hiç bulunmayabilir veya
# dengesiz dağılabilir. Bu da modelin performansını yanlış değerlendirmemize neden olur.