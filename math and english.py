score1 = int(input("輸入數學分數")) 

score2 = int(input("輸入英文分數"))

if (score1 >=0 and score1<=100) and (score2 >=0 and score2 <=100):
    
    if score1 >=90 and score2 >=90:
        print("恭喜得到獎品")
    elif score1 >=60 or score2 >=60:
        print("再加油")
    else:
        print("恭喜接受懲罰")
else:
    print("輸入錯誤")