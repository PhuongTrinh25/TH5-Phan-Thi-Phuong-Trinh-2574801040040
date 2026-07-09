Câu 5 (Ứng dụng Hàng đợi - Queue)
Cho mảng A = [4, 2, 12, 11, -5, 8, 1, 5, 6] và kích thước cửa sổ trượt k = 3. Thay vì tìm giá trị lớn nhất, hãy mô tả quá trình sử dụng cấu trúc Deque (Hàng đợi hai đầu) để tìm giá trị nhỏ nhất trong mỗi cửa sổ trượt. Trình bày trạng thái của Deque ở 3 bước dịch chuyển đầu tiên và đưa ra mảng kết quả.

dùng Deque để lưu vị trí (chỉ số) của các phần tử trong cửa sổ
khi có phần tử mới nếu phần tử ở cuối Deque lớn hơn nó thì xóa phần tử đó, nếu phần tử ở đầu không còn nằm trong cửa sổ thì cũng xóa
-> phần tử ở đầu Deque luôn là giá trị nhỏ nhất

3 bước dịch chuyển đầu tiên:
[4, 2, 12]: Deque = [2, 12] ->  = 2
[2, 12, 11]: Deque = [2, 11] ->  = 2
[12, 11, -5]: Deque = [-5] -> = -5
Thực hiện cho các cửa sổ còn lại -> được mảng kết quả: [2, 2, −5, −5, −5, 1, 1]
