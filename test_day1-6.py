motor_status = "OK"

angle_input = "185"

angle = int(angle_input)

print(type(angle))

if angle > 180:
    print("角度異常，馬達停止")
else:
    print("角度正常，繼續運作")

count = 1

while count <= 5:
    print("第" + str(count) + "次檢查")
   
    if count % 2 == 0:
        
        print("這是偶數次檢查")
    count = count + 1