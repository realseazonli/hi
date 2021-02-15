kg = input('请输入体重kg：')
cm = input('请输入身高cm：')
kg = float(kg)
cm = float(cm)
m = cm/100
bmi = kg/m/m
bmi = round(bmi, 2)
print(bmi)
if bmi >= 35:
    print('重度肥胖')
elif bmi >= 30:
    print('中度肥胖')
elif bmi >= 27:
    print('轻度肥胖')
elif bmi >= 24:
    print('过胖')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')