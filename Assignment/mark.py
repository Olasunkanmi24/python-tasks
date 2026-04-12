mark = int(input('Enter your mark: '))
if mark < 0:
    print('Your mark must be greater than 0')
elif mark > 100:
    print('Your mark must be less than 100')
else:
    if mark >= 90 and mark <=100:
        print('A')
    elif mark >=80 and mark <= 89:
        print('B')
    elif mark >=70 and mark <= 79:
        print('C')
    elif mark >=60 and mark <= 69:
        print('D')
    else:
        print('F')


