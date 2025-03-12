import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../data/scatterplot_data.xlsx')
data = df.head()
# print(data)

plt.style.use('fivethirtyeight')
"""
Temayı değiştirebiliriz.
Tema değiştiği için lejantı, eksenlere ait etiketleri ve başlığı küçültebilir; 
"""

kategori_renkleri = {
    'Durmuş Yılmaz': 'orange',  ## Kategori'da isme karşılık Renk
    'Erdem Başçı': 'blue',      ## Kategori'da isme karşılık Renk
    'Murat Çetinkaya': 'green', ## Kategori'da isme karşılık Renk
    'Murat Uysal': 'yellow',    ## Kategori'da isme karşılık Renk
    'Naci Ağbal': 'purple',     ## Kategori'da isme karşılık Renk
    'Şahap Kavcıoğlu': 'red'    ## Kategori'da isme karşılık Renk
}


plt.figure(figsize=(11,6))


for kategori, renk in kategori_renkleri.items():
    kategoriler = df[df['TCMB_BASKAN'] == kategori]
    marker = 'o'
    if kategori == 'Şahap Kavcıoğlu':
        marker = '^'
    plt.scatter(
        kategoriler['USDTRY'],
        kategoriler['ENFLASYON'],
        color=renk,
        alpha=0.7,
        label=kategori,
        marker=marker  # Şekiller
    )

"""
for kategori, renk in kategori_renkleri.items():
    
    kategoriler = df[df['TCMB_BASKAN'] == kategori]   
    plt.scatter(
         
        kategoriler['USDTRY'],
        kategoriler['ENFLASYON'],
        color=renk, #bunu kaldırırsam rastgele renk atar yine de çalışır
        alpha=0.7, # Saydamlık
        label=kategori # legend
    )
"""
"""
plt.figure(figsize=(12, 7))
plt.scatter(        # Başlangıç, sadece noktalar var. x, y  başlık ismi renkler yok. Tamamen default hali.
    'USDTRY',       # Başlangıç, sadece noktalar var. x, y  başlık ismi renkler yok. Tamamen default hali.
    'ENFLASYON',    # Başlangıç, sadece noktalar var. x, y  başlık ismi renkler yok. Tamamen default hali.
    data=df,        # Başlangıç, sadece noktalar var. x, y  başlık ismi renkler yok. Tamamen default hali.
    color = 'red'   # Noktalar kırmızı renk olur. Noktaların rengi değişiyor,

)
"""
plt.xlabel('USDTRY (%)')    # X etiketi
plt.ylabel('ENFLASYON')     # Y etiketi
plt.title('USDTRY ve ENFLASYON - TÜRKİYE')  # Başlık Adı
plt.figtext(0.75, 0.07, 'Veriler TCMB/EVDS\'den alınmıştır.', ha='center', va='center', fontsize='8', fontstyle='italic')
# Al tarafa bilgilendirme
plt.figtext(0.75, 0.04, 'USDTRY: Aylık alış kuru yüzde değişimler', ha='center', va='center', fontsize='8', fontstyle='italic')
# Al tarafa bilgilendirme
plt.figtext(0.75, 0.01, 'Enflasyon: Bir önceki yılın aynı ayına göre',ha='center', va='center', fontsize='8', fontstyle='italic')
# Al tarafa bilgilendirme
plt.rcParams['legend.fontsize'] = 'xx-small'
plt.legend()
plt.show()  





