Câu 1 (Chia mảng - Ứng dụng Tìm kiếm Nhị phân)
Một công ty vận tải cần giao các kiện hàng có khối lượng lần lượt là W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Công ty chỉ có K = 5 xe tải, và mỗi xe chỉ được chở các kiện hàng xếp liên tiếp nhau trong danh sách. Hãy dùng thuật toán tìm kiếm nhị phân để xác định tải trọng tối thiểu của một chiếc xe sao cho có thể chở hết tất cả kiện hàng trong một lượt. Giải thích cách chia kiện hàng cho 5 xe với tải trọng tìm được.

B1: Xác định khoảng tìm kiếm
W=[1,2,3,4,5,6,7,8,9,10]
K=5
max(w)= 10 -> left=10
tổng(w)= 55 -> right=55
-> khoảng tìm kiếm là: [10,55]
B2: Kiểm tra các giá trị
mid = 32 -> chở được trong 2 xe -> giảm xuống
mid = 20 -> chở được trong 4 xe -> giảm xuống
mid = 15 -> chở được đúng 5 xe  -> giảm xuống 
mid = 12, 13, 14 -> đều cần 6 xe -> không đủ
-> tải trọng nhỏ nhất là 15

Chia hàng cho 5 xe:
Xe 1: 1 + 2 + 3 + 4 + 5 = 15
Xe 2: 6 + 7 = 13
Xe 3: 8 = 8
Xe 4: 9 = 9
Xe 5: 10 = 10