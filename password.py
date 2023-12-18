password = "6324aaron"
count = 0
max = 3

while count < max:
    ans = input("請輸入密碼: ")
    if ans == password:
        print("恭喜答對")
        break
    elif ans != password:
        count = count + 1
        print("答錯!剩下", max - count, "次機會")
        if max - count == 0:
            print("帳號已上鎖!!!")
