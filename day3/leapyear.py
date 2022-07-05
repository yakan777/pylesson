def is_leapyear(year):
    return(year%400==0 or (year % 4==0 and year % 100 !=0) )
now_year=int(input('今年は何年?>'))
if is_leapyear(now_year):
    print(f'{now_year}はうるう年です')
else:
    print(f'{now_year}はうるう年ではありません')
    

