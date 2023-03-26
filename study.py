with open('/home/arkadiy/py/first_repo/massive', 'r+') as mssv:
    temp_var = mssv.read()

list_of_words = [word.lower().strip() for word in temp_var.split() if len(word) > 2]
words_by_one = set(list_of_words)
voc = {}

for word in words_by_one:
    count = 0
    for wrd in list_of_words:
        if wrd == word:
            count += 1
    if word.isalpha():
        voc[word] = count

sorted_list = sorted(voc.items(), reverse = 1, key = lambda item: item[1])
with open('/home/arkadiy/py/first_repo/text.txt', 'a') as massive:
    for word, key in sorted_list:
        one_line = f'{key}, {word}\n'
        massive.writelines(one_line)
        print(key, word)
