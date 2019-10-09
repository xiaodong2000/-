x = input("请输入一段字符")
a=b=c=d=0
for i in x:
    if ord('a')<=ord(i)<=ord('z') or ord('A')<=ord(i)<=ord('Z'):
        a=a+1
    elif ord('1')<=ord(i)<=ord('9'):
        b=b+1
    elif ord(i)==ord(' '):
        c=c+1
    else:
        d=d+1
print("字母数量:{},数字数量:{},空格数量:{},其他:{}。".format(a,b,c,d))
 
