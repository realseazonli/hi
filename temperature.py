#输入摄氏温度，程序转成华氏温度输出
temp_c = input('请输入摄氏温度：')
temp_h = int(temp_c)*9/5+32
if temp_c :
    print('您输入的摄氏温度是：', int(temp_c), '°C，换算成华氏温度是：', temp_h, '℉')