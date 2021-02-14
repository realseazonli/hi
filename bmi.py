# 要求输入身高和体重，程序算出bmi数据，并判断bmi状况

height = float(input('请输入身高cm：'))
height = height/100
weight = float(input('请输入体重kg：'))
bmi = weight/height/height
print('您的BMI值是：', bmi)
if bmi < 18.5 :
    print('体重过轻')
elif bmi >=18.5 and bmi <24 :
    print('体重正常')
elif bmi >= 24 and bmi < 27 :
    print('过重')
elif bmi >=27 and bmi <30 :
    print('轻度肥胖')
elif bmi >=30 and bmi < 35 :
    print('中度肥胖')
else :
    print('重度肥胖')