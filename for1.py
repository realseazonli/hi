# for loop

names = ['Tom', 'Simon', 'Seazonli', 'Mike']
count = 0
print('这个小组有', len(names), '位同学，他们是：')
for name in names :
    count = count + 1
    print('第', count, '位：', name)