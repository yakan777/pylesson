name=input('性別を入力>')
age=int(input('年齢を入力>'))
if (name == '男' and age>=18) or (name=='女' and age>=16):
    print('結婚出来ます')
else:
    print('結婚出来ません')
