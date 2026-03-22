from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from src.preprocessing import preprocessing

def trafficModel(df):
    model = Sequential()
    model.add(Dense(64,activation="relu"))
    model.add(Dense(32,activation="relu"))
    model.add(Dense(1))

    model.compile(
        optimizer = "adam",
        loss = "mse",
        metrics = ["mae"] 
    )
    X_train,X_test,y_train,y_test = preprocessing(df)
    history = model.fit(
        X_train,
        y_train,
        epochs = 10,
        batch_size = 32,
        validation_data = (X_test,y_test)
    )
    return model,history,X_test,y_test
