import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('../data/günlükdelhiiklimeğitim.csv')
# print(data.head()) # ilk 5 sair
# print(data.describe()) # istatistik bilgiler
# print(data.info()) # Sütunlara ait Bİlgiler

## Yillar boyunca Delhi ortalama sicaklik
figure = px.line(data, x="date", 
                 y="meantemp", 
                 title='Delhi Yillar Boyunca Ortalama Sicakliği ')
# figure.show()

## Yillar boyunca Delhi ortalama nem orani
figure = px.line(data, x="date", 
                 y="humidity", 
                 title='Delhi Yillar Boyunca Nem orani')
# figure.show()

## Yillar boyunca Delhi Rüzgar hzhi
figure = px.line(data, x="date", 
                 y="wind_speed", 
                 title='Delhi Yillar Boyunca Rüzgar Hizi')
# figure.show()

"""
2015'e kadar, rüzgar hizi musonlar (Ağustos ve Eylül) ve geri çekilen musonlar (Aralik ve Ocak) sirasinda daha yüksekti. 
2015'ten sonra, musonlar sirasinda rüzgar hizinda herhangi bir anormallik olmadi. 
"""

figure = px.scatter(data_frame = data, x="humidity",
                    y="meantemp", size="meantemp", 
                    trendline="ols",  # ols, en küçük kareler yöntemi - Ordinary Least Square
                    title = "Sicaklik ve Nem arasindaki ilişki")
# figure.show()


"""
İşte tarih sütunundan veri türünü nasil değiştirebileceğimiz ve yil ve ay verilerini nasil
"""


data["date"] = pd.to_datetime(data["date"], format = '%Y-%m-%d')
data['year'] = data['date'].dt.year
data["month"] = data["date"].dt.month
# print(data.head())

"""
Delhi'deki sicaklik değişiminin yillara göre nasil değiştiğine bir
"""

plt.style.use('fivethirtyeight')
plt.figure(figsize=(15, 10))
plt.title("Delhi'nin yillara Göre Sicaklik Değişimi")
sns.lineplot(data = data, x='month', y='meantemp', hue='year')
# plt.show()

forecast_data = data.rename(columns = {"date": "ds", 
                                       "meantemp": "y"})
# print(forecast_data)

from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

model = Prophet()
model.fit(forecast_data)
forecasts = model.make_future_dataframe(periods=365)
predictions = model.predict(forecasts)
fig = plot_plotly(model, predictions)
fig.show()

"""
Hava tahmini, belirli bir konum ve zaman için hava koşullarini tahmin etme görevidir. 
Hava durumu verileri ve algoritmalari kullanilarak, önümüzdeki n gün sayisi için hava koşullarini tahmin etmek mümkündür
"""