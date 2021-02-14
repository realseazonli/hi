driving = input('请问你有开过车吗？')
if driving != '有' and driving != '没有' :
    print('只能输入 有/没有')
    raise SystemExit
age = int(input('请问你的年龄？'))
if driving == '有' :
    if age >= 18 :
        print('你确实可以开车')
    else :
        print('你还没有到能开车的年龄')
elif driving == '没有':
    if age >=18 :
        print('你已经可以学开车了')
    else :
        print('等你到18岁就可以学开车了')
