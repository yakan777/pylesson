userinfo =input('名前と血液型をカンマ区切りで入力>')
[name,blood]=userinfo.split(',')
blood=blood.upper().strip()
print('{}さんは{}型なので大吉です'.format(name,blood))

result='bamama'.replace('a','o')
print(result)

aCount='banana'.count('a')
print(aCount)

def add(x,y):
    return x+y

print(type(add))
newadd=add
print(newadd(4,5))
