for i in range(1,6):
    a = int(input('请输入年份 '))
    if (a%4 == 0) and (a%100 != 0):
        print('%d 今年是润年' % a)
    elif a%400 == 0:
        print('%d 今年是润年' % a)
    else:
        print('%d 今年是平年' % a)

