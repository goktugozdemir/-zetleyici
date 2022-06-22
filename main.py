
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = """Prices are continuing to rise at their fastest rate for 40 years with food costs, particularly for bread, cereal and meat, climbing.

UK inflation, the rate at which prices rise, edged up to 9.1% in the 12 months to May, from 9% in April, the Office for National Statistics (ONS) said.

Fuel and energy prices are the biggest drivers of inflation, but the ONS said food costs had pushed it up further.

Workers and unions are pushing for pay rises to cope with higher prices.

But the government has warned against employers handing out big increases in salaries over fears of a 1970s style "inflationary spiral" where firms hike wages and then pass the cost on to customers through higher prices.

Currently, inflation is at the highest level since March 1982, when it also stood at 9.1% and the Bank of England has warned it will reach 11% this year.

Inflation is the pace at which prices are rising. For example, if a bottle of milk costs £1 and that rises by 5p compared with a year earlier, then milk inflation is 5%.

"""

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)


sıklıktablosu = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in sıklıktablosu:
        sıklıktablosu[word] += 1
    else:
        sıklıktablosu[word] = 1

cümleler = sent_tokenize(text)
deger = dict()

for sentence in cümleler:
    for word, freq in sıklıktablosu.items():
        if word in sentence.lower():
            if sentence in deger:
                deger[sentence] += freq
            else:
                deger[sentence] = freq

toplam = 0
for sentence in deger:
    toplam += deger[sentence]


ortalama = int(toplam / len(deger))

summary = ''
for sentence in cümleler:
    if (sentence in deger) and (deger[sentence] > (1.2 * ortalama)):
        summary += " " + sentence

print(summary)
