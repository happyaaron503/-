password = "6324aaron"
count = 0
max = 3

while count < max:
    ans = input("請輸入密碼: ")
    count = count + 1
    if ans == password:
        print("登入成功")
        break
    elif ans != password and max - count != 0:
        print("答錯!剩下", max - count, "次機會")
    elif ans != password and max - count == 0:
        if max - count == 0:
            print("答錯!帳號已上鎖!!!")
