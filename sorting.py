from bs4 import BeautifulSoup
import requests

url = input("Введите адрес html страницы")

response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')

print(bs.get_text())



mylist = [word.lower().strip() for word in bs.get_text().split() if len(word) > 2]
print(mylist)


for i in range(len(mylist)):
    if mylist[i][-1] in ".,-/:;()?!<>[]{}'":
        mylist[i] = mylist[i][:-1]
    if mylist[i].isdigit(): mylist[i] = ''

reslist =[]
for word in mylist:
    if word.isalpha(): reslist.append(word)
mylist_clear = list(set(reslist))

mydict = {}
for i in mylist_clear:
    count = 0
    for j in mylist:
        if i == j: count += 1
    mydict[i] = count


sort_tuple = sorted(mydict.items(), reverse=1, key=lambda item: item[1])

count = 0
res_list = [value + '\n' for value, key in sort_tuple]
with open('/home/arkadiy/py/first_repo/text.txt', 'w') as f:
    for v, k in sort_tuple:
        if k < 5: break
        print(count, k, v)
        count += 1
        v = v + '\n'
        f.writelines(v)

print(res_list)