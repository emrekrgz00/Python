import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('../data/multisetbarchart_data.xlsx')
data = df.head()
# print(data)

plt.style.use('fivethirtyeight')
yillar = df['TARIH'].astype(str)
teknolojiler = df.columns.tolist()
teknolojiler.remove('TARIH')


yatay_eksen = np.arange(len(yillar))
bar_genislik = 0.15
bar_ara_mesafe = 0

viridis_renk_paleti = plt.cm.viridis(np.linspace(0, 1, len(teknolojiler))) # Renk paleti ekledim.

for i, teknoloji in enumerate(teknolojiler):
    veriler = df[teknoloji]
    plt.bar(
        yatay_eksen + (bar_genislik + bar_ara_mesafe) * i,
        veriler,
        width=bar_genislik,
        color=viridis_renk_paleti[i], # Renk ekledim.
        # label=teknoloji,   # label ekledim
        label=teknoloji.replace('_',' ') # etiketete bulunan '_' değişirdim ' ' yaptım
    )

plt.xticks(yatay_eksen, yillar) # X eksen
plt.ylabel('Endeks')  # Y eksen
# plt.title('Yıllara Göre Sanayi Üretim Teknoloji Endeksleri') # Başlık
# plt.figtext(0.6, 0.02, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='left', fontsize='8', fontstyle='italic') # Alt açıklama
plt.title('Yıllara Göre Sanayi Üretim Teknoloji Endeksleri', fontsize='12') # Başlık küçüldü
plt.figtext(0.6, 0.01, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='left', fontsize='8', fontstyle='italic')
# plt.legend() # legend ekledim
plt.legend(fontsize='x-small') # Legend küçülttüm
plt.show()