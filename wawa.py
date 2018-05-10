for i in range(o,5):
    a = int(input("请输入抓娃娃需要多少秒（1～60秒）"))
    if  a > 30:
        print ("时间到啦，机器自动给你抓")
        continue
    print ("你本次用了%d秒 %"a)
