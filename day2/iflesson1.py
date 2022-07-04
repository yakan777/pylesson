name=input('あなたの名前を教えてください')
print('{}さん、こんにちは'.format(name))
food=input('{}さんの好きな食べ物を教えてください>'.format(name))
if 'カレー' in food:
#if 'カレー' not in food:　←カレー以外
    print('素敵です')
else:
    print('私も{}が好きですよ'.format(food))
