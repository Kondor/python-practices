dict_main = {}
with open('file.txt', 'r', encoding='utf-8') as file:
    for line in file:
        key, *value = line.split(':')
        dict_main[key] = value
        # print(key, ':', ' '.join(str(x) for x in dict_main[key]))

dict_tmp = {}
for _ in range(int(input())):
    country = input().strip()
    dict_tmp[country] = dict_main[country]

for line in dict_tmp:
    # print(str(dict_tmp.get(line)).strip("[ |] |' |*''\n|"))
    print(''.join(str(x) for x in dict_tmp[line]).strip(' '), end='')
