from bs4 import BeautifulSoup
import requests

url = 'https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup'

response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')

print(bs.get_text())



mylist = [x.lower() for x in bs.get_text()]
print(mylist)

for i in range(len(mylist)):
    if mylist[i][-1] in ".,-/:;()?!'":
        mylist[i] = mylist[i][:-1]

mylist_clear = list(set(mylist))
mydict = {}
for i in mylist_clear:
    count = 0
    for j in mylist:
        if i == j: count += 1
    mydict[i] = count

sort_tuple = sorted(mydict.items(), reverse=1, key=lambda item: item[1])

sort_dict = {k: v for k, v in sort_tuple}
for k, v in mydict.items():
    print(v, k)

print(sort_dict)