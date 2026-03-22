import matplotlib.pyplot as plt
from src.data_loader import dataLoader
import pandas as pd
from src.feature_engineering import featureEngineering

def visualization(df):
    grouped = df.groupby("hour")["Total"].mean()  # aynı saatleri gruplar, her saat için trafik değerini alır ve bunların ortalamasını alır
    plt.plot(grouped.index, grouped.values, marker = 'o')
    plt.title("Traffic vs. Hour")
    plt.xlabel("Hour")
    plt.ylabel("Average Traffic Volume")
    plt.show()

    groupedDay = df.groupby("Day of the week")["Total"].sum()  # gün sütununa göre gruplandırıp her gün için total ortalamayı al
    order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    groupedDay = groupedDay.reindex(order) # sıralamak için
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

 # test için
# df = dataLoader()
# sonDF = featureEngineering(df)
# visualization(sonDF)

# ===================== VISUALIZATION ANALYSIS =====================
# Bu bölümde trafik verisi farklı açılardan analiz edilmiştir.
# Amaç, model kurmadan önce verinin davranışını anlamaktır.

# 1. Traffic vs Hour (Saatlik Trafik Analizi)
# - Trafik gün içinde belirgin şekilde değişmektedir.
# - Sabah saatlerinde (özellikle 6-9 arası) ve akşam saatlerinde (16-18 arası) pik yapmaktadır.
# - Gece saatlerinde trafik oldukça düşüktür.
# -> Bu gösterir ki trafik yoğunluğu büyük ölçüde saate bağlıdır.
# -> Model için en önemli feature'lardan biri "hour" olacaktır.

# 2. Traffic for Days (Günlük Trafik Analizi)
# - Haftanın günleri arasında trafik ortalamaları birbirine oldukça yakındır.
# - Belirgin bir gün bazlı fark gözlenmemektedir.
# -> Bu, trafikte gün etkisinin zayıf olduğunu gösterir.
# -> Model açısından "day_of_week" daha az etkili bir feature olabilir.

# 3. Traffic Situation Distribution (Sınıf Dağılımı)
# - Veri seti dengesizdir (imbalanced dataset).
# - "normal" sınıfı diğer sınıflara göre çok daha fazladır.
# - "low" ve "high" sınıfları daha az temsil edilmektedir.
# -> Bu durum modelin majority class'a (normal) bias geliştirmesine neden olabilir.
# -> Model performansı değerlendirilirken bu durum dikkate alınmalıdır.

# GENEL SONUÇ:
# - Trafik yoğunluğu zaman (saat) bazlı değişmektedir.
# - Gün bazlı değişim zayıftır.
# - Veri setinde sınıf dengesizliği bulunmaktadır.
# ================================================================