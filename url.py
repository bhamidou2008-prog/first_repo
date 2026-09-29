from collections import Counter
import requests
import re
# url= 'http://www.gutenberg.org/files/1112/1112.txt'
# response= requests.get(url)
# texte = response.text
# sub= re.sub(r'[^a-zA-Z]', ' ', texte)
# spl= sub.split()
# number= Counter(spl)

# common= number.most_common(10)
# print(common)

# cats_api = 'https://api.thecatapi.com/v1/breeds'
# cats_response = requests.get(cats_api)
# js=  cats_response.json()
# for cat in js:
#     max_weight, min_weight = cat['weight']['metric'].split(' - ')
#     #print(f"{cat['name']}: Max weight - {max_weight}, Min weight - {min_weight}")
#     median= (float(max_weight) + float(min_weight)) / 2
#     print(f"{cat['name']}: Median weight - {median}")


