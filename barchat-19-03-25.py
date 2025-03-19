import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_excel('../data/barchart_data.xlsx')
data = df.head()
# print(data)
plt.style.use('fivethirtyeight')
plt.figure(figsize=(12,7))
"""
df['TARIH'] = df['TARIH'].astype(str)  # X -ekseni yıllara göre böldüm.



plt.bar(
    'TARIH',
    'TOPLAM',
    data=df,
    color='red'  # Bar renkleri değiştir.


)
formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x/1000000) + 'M' if x != 0 else '') # y eksenini milyon cinsinden yazalım  
plt.gca().yaxis.set_major_formatter(formatter) # y eksenini milyon cinsinden yazalım  
plt.ylabel('Ziyaretçi Sayısı') # y ekseni
plt.title('Yıllara Göre Türkiye\'ye Gelen Toplam Ziyaretçi Sayısı') # Başlık
plt.figtext(0.6, 0.04, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='left', fontsize='8', fontstyle='italic') # Alt açıklama
plt.show()
"""
# KAtegori şeklinde
df['TARIH'] = df['TARIH'].astype(str)

df2 = pd.melt(
    df,
    id_vars='TARIH', value_vars=['AVRUPA', 'BDT', 'AMERIKA', 'AFRIKA', 'ASYA'],
    var_name='GRUP',
    value_name='SAYI'
)
# df2 = df2[df2['TARIH'] == '2020'] 
# df_sirala = df2.sort_values('SAYI', ascending=False) # katgeori sıraladım 
df_sirala = df2.sort_values('SAYI', ascending=True) # katgeori sıraladım ters çevirdim

# plt.bar(
#     'GRUP',
#     'SAYI',
#     # data=df2,
#     data=df_sirala,
#     color='red'
# )

plt.barh(   # Grafik yan döndü, bar h oldu
    'GRUP',
    'SAYI',
    # data=df2,
    data=df_sirala,
    color='red'
)
formatter = ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x/1000000) + 'M' if x != 0 else '')
# plt.gca().yaxis.set_major_formatter(formatter)
plt.gca().xaxis.set_major_formatter(formatter)
plt.ylabel('Ziyaretçi Sayısı')
plt.title('Ülke Gruplarına Göre Türkiye\'ye Gelen Toplam Ziyaretçi Sayısı, 2020')
plt.figtext(0.6, -0.05, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='left', fontsize='10', fontstyle='italic')
plt.show()
