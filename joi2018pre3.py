n = int(input())
s = input()

xo = "XO"
ox = "OX"

count_x = s.count("X")
#print(count_xo)
dst = s.replace("X", "")
o_length = len(s)
# Oの数
x_length = n - o_length

count_o = s.count("O")
#print(count_ox)
dst = s.replace("O","")


if count_xo == 0:
    print(1)
    count = 0
elif count_ox == 0:
    print(2)
    count = 0
elif count_ox == count_xo:
    print(3)
    count = count_ox
else:
    print(4)
    count = count_ox + count_xo

print(count)



#if count_o == 0:
#    count = 0
#elif count_x == 0:
#    count = 0
#elif count_o == count_x:
#    count = count_o
#elif count_o > count_x:
#    count = count_x
#else:
#    count = count_o

#dst = s.replace("OX", "",1)
#ans = len(dst)
#
## 文字列に検索したい文字列が含まれているか
#for ox in s:
#    count = s.count(ox)
#    dst = s.replace(ox,"-",count)
#    for xo in s:
#        dst = s.replace("XO", "-",1)
#        count = count + 1
