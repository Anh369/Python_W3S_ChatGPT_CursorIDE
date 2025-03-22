# Python là ngôn ngữ có cú pháp đơn giản và dễ hiểu
# Thụt lề trong Python
# Thụt lề là khoảng trống ở đầu 1 dòng mã
# Trong Python, thụt lề được sử dụng để định nghĩa khối mã, vậy

#   Ví dụ: 
##  Đúng
if 5 > 2:
    print("Five is greater than two !") 
else:
    print("Five is not greater than two!")
    
#   Nếu không sử dụng thụt lề, Python sẽ báo lỗi
##  Sai:

# if 5 > 2:
# print("Five is greater than two !") 
# else:
# print("Five is not greater than two !")

# Cách sử dụng phổ biến nhất là bốn khoảng trắng, nhưng tối thiểu phải có một khoảng trắng.

if 6 > 3:
    print("Six is greater than three !")
#   4 khoảng trắng = 1 tab
if 6 > 3:
 print("Six is greater than three !")
#   1 khoảng trắng 
    

#   Phải sử dụng cùng số lượng khoảng trắng trong cùng một khối mã, nếu không Python sẽ báo lỗi:

##  Ví dụ Sai:
# if 8 < 9:
#     print("Eight is not greater than Nine !")
#      print("Eight is less than nine !")
     #  Sai vì trong 1 khối mã, 1 dòng là 4 khoảng trắng, 1 dòng lại là 5 khoảng trắng

##  Ví dụ đúng
if 7 < 9:
    print("Seven is not greater than Nine \n")
    print("Seven is less than Nine")




