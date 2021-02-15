# 读取文件，留意strip() append()用法

data = []
with open('food.txt', 'r') as f :
    for line in f :
        data.append(line)
        print(line.strip())
    print(data)
    print(len(data))