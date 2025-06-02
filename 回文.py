def isHuiwen():
    s = input("请输入一个字符串：")
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            print("不是回文")
            return
    print("是回文")
    