Câu 2 (Thuật toán Sắp xếp)
Cho mảng A = [5, 2, 4, 6, 1, 3]. Hãy tính tổng số lần dịch chuyển (shift) phần tử khi áp dụng thuật toán Insertion Sort để sắp xếp mảng theo thứ tự tăng dần. Đại lượng tính được này có mối liên hệ đặc biệt nào với khái niệm "số nghịch thế" (inversions) của mảng ban đầu?


Thực hiện Insertion Sort:
chèn 2 vào trước 5 -> dịch 1 phần tử
chèn 4 -> dịch 1 phần tử (dịch 5)
chèn 6 -> không dịch
chèn 1 -> dịch 4 phần tử (6, 5, 4, 2)
chèn 3 -> dịch 3 phần tử (6, 5, 4)
Tổng: 1 + 1 + 0 + 4 + 3 = 9	​

Mối liên hệ: 
Trong Insertion Sort, tổng số lần dịch chuyển phần tử luôn bằng số nghịch thế của mảng ban đầu.
Với mảng [5, 2, 4, 6, 1, 3], số nghịch thế cũng bằng 9