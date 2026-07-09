Thuật toán Floyd, nếu Rùa và Thỏ gặp nhau thì là danh sách liên kết có chu trình
rồi đưa một con trỏ về Head, con trỏ còn lại giữ nguyên tại điểm gặp nhau, cho cả hai cùng di chuyển mỗi lần 1 bước

trong toán học, khoảng cách từ Head đến nút bắt đầu chu trình bằng khoảng cách từ điểm gặp nhau đến nút bắt đầu chu trình theo số bước trong chu trình
nên khi cả hai cùng di chuyển cùng tốc độ, chúng sẽ gặp nhau đúng tại nút bắt đầu của chu trình

-> giai đoạn 2 của thuật toán Floyd dựa trên mối quan hệ về khoảng cách trong chu trình giúp xác định chính xác nút bắt đầu chu trình trong danh sách liên kết.