Câu 4 (Ứng dụng Ngăn xếp - Stack)
Cho mảng biểu diễn nhiệt độ trong các ngày liên tiếp T = [73, 74, 75, 71, 69, 72, 76, 73]. Trình bày cách sử dụng Ngăn xếp đơn điệu (Monotonic Stack) để đếm số ngày ít nhất phải chờ để có một ngày ấm hơn (nhiệt độ cao hơn) cho mỗi ngày. Nếu không có ngày nào trong tương lai thỏa mãn, trả về 0. Cung cấp mảng kết quả cuối cùng.

Ngăn xếp đơn điệu: để lưu chỉ số của các ngày chưa tìm được ngày có nhiệt độ cao hơn, duyệt từ trái sang phải, nếu nhiệt độ hiện tại lớn hơn nhiệt độ ở đỉnh stack thì lấy chỉ số đó ra và tính

Số ngày chờ = chỉ số hiện tại - chỉ số đã lấy ra
rồi đưa chỉ số hiện tại vào stack
khi duyệt hết mảng, các ngày còn lại trong stack sẽ có kết quả bằng 0 vì không có ngày nào trong tương lai có nhiệt độ cao hơn
Kết quả thu được: 
ngày 0: chờ 1 ngày
ngày 1: chờ 1 ngày
ngày 2: chờ 4 ngày
ngày 3: chờ 2 ngày
ngày 4: chờ 1 ngày
ngày 5: chờ 1 ngày
ngày 6: 0 ngày
ngày 7: 0 ngày
-> mảng kết quả cuối cùng là: [1, 1, 4, 2, 1, 1, 0, 0]