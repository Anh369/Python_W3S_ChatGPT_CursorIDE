# Thụt lề trong Python (Indentation)

## Khái niệm
- Thụt lề là khoảng trống ở đầu một dòng mã
- Được sử dụng để định nghĩa các khối mã (code blocks)
- Là một phần quan trọng trong cú pháp của Python

## Quy tắc thụt lề

### 1. Số lượng khoảng trắng
- Thông thường sử dụng 4 khoảng trắng (1 tab)
- Tối thiểu phải có 1 khoảng trắng
- Phải nhất quán trong cùng một khối mã

### 2. Ví dụ cú pháp đúng
```python
if 5 > 2:
    print("Five is greater than two!")
else:
    print("Five is not greater than two!")
```

### 3. Ví dụ cú pháp sai
```python
# Thiếu thụt lề
if 5 > 2:
print("Five is greater than two!")
else:
print("Five is not greater than two!")

# Thụt lề không nhất quán
if 8 < 9:
    print("Eight is not greater than Nine!")
     print("Eight is less than nine!")  # Thụt lề 5 khoảng trắng - sai
```

## Lưu ý quan trọng
- Python sẽ báo lỗi nếu không sử dụng thụt lề
- Trong cùng một khối mã, phải giữ số lượng khoảng trắng thụt lề giống nhau
- Có thể sử dụng 1 khoảng trắng nhưng khuyến nghị dùng 4 khoảng trắng
- Thụt lề không đúng sẽ dẫn đến lỗi cú pháp (IndentationError)
