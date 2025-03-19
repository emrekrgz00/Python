import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('../data/stackedbargraph_data.xlsx')
data = df.head()
# print(data)
plt.style.use('fivethirtyeight')
plt.figure(figsize=(12,7))
yillar = df['TARIH'].astype(str) 
df.drop('TARIH', axis=1, inplace=True) # Tarihleri aldım
df.drop('TOPLAM_YURTICI', axis=1, inplace=True)
df_yuzde = df.div(df.sum(axis=1), axis=0) * 100

bankalar = df.columns.tolist()

yatay_eksen = np.arange(len(yillar))
bar_genislik = 0.7
bar_ara_mesafe = 0

taban = np.zeros(len(yillar))
viridis_renk_paleti = plt.cm.viridis(np.linspace(0, 1, len(bankalar)))

for i, banka in enumerate(bankalar):
    veriler = df_yuzde[banka]
    plt.bar(
        yatay_eksen,
        veriler,
        width=bar_genislik,
        bottom=taban,
        color=viridis_renk_paleti[i],
        # label=banka
        label=banka.replace('_',' ')

    )
    taban += veriler

plt.xticks(yatay_eksen, yillar)
# plt.yticks([0, 25, 50, 75, 100]) #  Y ekseni 25'lik artar
plt.yticks(np.linspace(0,100,5)) # Y ekseni 25'lik artar
plt.ylabel('Kredi Hacmi Payı (%)')
plt.title('Yurt İçi Kredi Hacmi Dağılımı')
plt.figtext(0.8, 0.02, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='left', fontsize='8', fontstyle='italic')
# plt.legend()
# plt.legend(loc='upper center', ncol=len(bankalar), bbox_to_anchor=(0.5, -0.06)) # Legend konum değişikliği
plt.legend(loc='upper center', ncol=len(bankalar), bbox_to_anchor=(0.5, -0.06), frameon=False)  # Legend konum değişikliği, çerceve silme
plt.show() 
