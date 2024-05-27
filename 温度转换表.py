
tempstr =input ("温度值：")
if tempstr [-1] in ['F','f']:
    C = (eval (tempstr[0:-1])-32)/1.8
    print("转换后的温度{:.2f}C".format(C))
elif tempstr[-1] in ['C','c']:
    F = 1.8*eval(tempstr[0:-1])+32
    print("转换后的温度{:.2f}F".format(F))
else:
    print("shurucuowu")
