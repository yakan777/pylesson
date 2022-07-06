try:
    price=int(input('料金を入力>'))
    number=int(input('人数を入力>'))
    print(f'一人あたり{(price/number)}円です')
except ValueError:
    print('正しい値を入力してください')
print('プログラムを終了します')
