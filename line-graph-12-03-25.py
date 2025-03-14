import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../data/linegraph_data.xlsx')
# df['TARIH'] = pd.to_datetime(df['TARIH'], format='%Y-%m-%d')
df['TARIH'] = pd.to_datetime(df['TARIH'] + '-01' ,format='%Y-%m-%d', errors='coerce')
# Tarih formatı 2023-01 gibiydi buna '-01' eklyerek, istediğim formata döndüm
data = df.head()
# print(data)
plt.style.use('fivethirtyeight')
plt.figure(figsize=(11,6))
"""
plt.plot(
    
    'TARIH',
    'TUFE_REDK',
    data=df,
    color = 'red' ## Renk ekledim
)
plt.ylabel('REDK')  # Y - ekseni etiketi
plt.title('TÜFE Bazlı Reel Efektif Döviz Kuru (2003=100), Türkiye') # Başlık
plt.figtext(0.8, 0.03, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='left', fontsize='8', fontstyle='italic')
# Alt tarafa eklenti, açıklama, etiket
plt.axhline(y=100, color='black', linestyle='--') # 100 değerine yatay çizgi eklendi
plt.show()
"""
###Çoklu çizgi grafik yapabiliriz.
# target_date = pd.to_datetime('2016-01-01') # Y ekseni boyunca çizgi için tarih atadım
plt.plot(
    'TARIH',
    'TUFE_REDK',
    data=df,
    color='black'
)
plt.plot(
    'TARIH',
    'TUFE_REDK_GELISMEKTE',
    data=df,
    color='blue'
)
plt.plot(
    'TARIH',
    'TUFE_REDK_GELISMIS',
    data=df,
    color='orange'
)
plt.ylabel('REDK')
plt.title('TÜFE Bazlı Reel Efektif Döviz Kuru (2003=100), Türkiye')
plt.figtext(0.6, -0.03, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='left', fontsize='8', fontstyle='italic')
plt.axhline(y=100, color='red', linestyle='--')  # Belirtme çizgisi kırmızı x ekseni boyunca y = 100'de düz
# plt.axvline(x=target_date, color='b', linestyle='-.') # Belirtme çizgisi kırmızı y ekseni boyunca x = target_date ne olursa
# plt.legend() 
plt.legend(fontsize='xx-small') # -- Legend küçültür,
plt.legend(fontsize='xx-small', loc='lower left') # Legend sağ üst köşeye gider
plt.show()
