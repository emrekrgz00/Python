import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('../data/histogram_data.xlsx')
data = df.head()
# print(data)

### Tek değişkenli
"""
plt.hist(
    'BIST100',
    data=df,
    color='red',  # Renk değiştir
    # bins = 20 ,    # histogram sayısı
    bins = 'auto'    #Histogram sayısı otomatik ayarlanır
)

plt.xlabel('Getiri (%)')  # X ekseni
plt.ylabel('Frekans')     # Y eskseni
plt.title('BIST100 Aylık Getirileri (01/2003-06/2023)')  # başlık
plt.figtext(0.6, 0.04, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='left', fontsize='8', fontstyle='italic') # Bilgi
plt.yticks([]) # Histogram tipi olduğu için Y tipini kaldırdım
plt.axvline(x=0, color='black', linestyle='--')  #Sıfır noktasına çizgi
plt.show()
"""

### Çok değişkenli
plt.style.use('fivethirtyeight')

medyan_bist100 = np.median(df['BIST100'])  # MEdian hesaplama
medyan_usdtry = np.median(df['USDTRY'])

plt.hist(
    'BIST100',
    data=df,
    color='red',
    bins='auto',
    alpha=0.7,  #Saydamlık
    label='BIST100'
)
plt.hist(
    'USDTRY',
    data=df,
    color='orange',
    bins='auto',
    alpha=0.7,  #Saydamlık
    label='USDTRY'
)
plt.xlabel('Getiri (%)')  # X ekseni
plt.ylabel('Frekans')     # Y eskseni
plt.title('BIST100 Aylık Getirileri (01/2003-06/2023)')  # başlık
plt.figtext(0.6, 0.04, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='left', fontsize='8', fontstyle='italic') # Bilgi
plt.yticks([]) # Histogram tipi olduğu için Y tipini kaldırdım
# plt.axvline(x=0, color='black', linestyle='--')  #Sıfır noktasına çizgi
plt.axvline(x=medyan_bist100, color='red', linestyle='--', linewidth='3', label='BIST100 Medyan')
# Dikey çizgiti medyan'dan çekicez 
plt.axvline(x=medyan_usdtry, color='orange', linestyle='--', linewidth='3', label='USDTRY Medyan')
plt.rcParams['legend.fontsize'] = 'x-small'  # legant küçültme 
plt.legend()  # Veri seti açıklama -- Label koymazsan legend işe yaramaz boş küçük figure açar
plt.show()
