from selenium import webdriver
import matplotlib.pyplot as plt
import numpy as np
import dictionary
import time

lang = "hello"
while lang != "0" and lang != "1":
    lang = input("0 for Turkish chart, 1 for English chart ")


path = "*"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://seyler.eksisozluk.com/")
time.sleep(2)
categories = driver.find_elements_by_class_name("meta-category")

index = 0
topics = {}
for a in categories:
    if index < 25:
        index += 1
        try:
            topics[a.text.upper()] += 1
        except:
            topics[a.text.upper()] = 1
    else:
        break

if lang == "0":
    title = "İstatistikler"
    x_label = "Konular"
    y_label = "Konuların Sayıları"
    x = [b.capitalize() for b in topics.keys()]

elif lang == "1":
    title = "Statistics"
    x_label = "Topics"
    y_label = "Number of Topics"
    x = []
    keys = dictionary.translations.keys()
    for c in topics.keys():
        if c in keys:
            x.append(dictionary.translations[c])
        else:
            x.append(c)

y = topics.values()
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')
positions = np.arange(len(x))
plt.xticks(positions, x)
plt.tick_params(labelsize=8)
plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)

rng = range(0, max(y) + 1)
plt.yticks(list(rng))

plt.bar(positions, y)
plt.show()

driver.close()
