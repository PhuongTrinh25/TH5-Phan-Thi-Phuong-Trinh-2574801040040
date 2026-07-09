Câu 3 (Đồ thị & Thuật toán Dijkstra)
Tại sao thuật toán Dijkstra lại cho kết quả sai khi đồ thị có chứa cạnh trọng số âm? Hãy tự thiết kế một đồ thị có hướng nhỏ (gồm 3 đỉnh) làm phản ví dụ chứng minh sự sai lệch của bước "chốt đỉnh". Đề xuất một thuật toán khác có thể thay thế Dijkstra trong trường hợp này.

Thuật toán Dijkstra cho kết quả sai khi đồ thị có chứa cạnh trọng số âm vì: 
Dijkstra có bước "chốt đỉnh", là khi một đỉnh đã được chốt thì khoảng cách đến đỉnh đó đã là ngắn nhất. Nếu có cạnh trọng số âm, sau này nếu xuất hiện một đường đi ngắn hơn thì kết quả sẽ sai
Đồ thị: Có 3 đỉnh: A, B, C
A -> B = 4
A -> C = 2
B -> C = -3
Bắt đầu từ A
d(A) = 0
d(B) = 4
d(C) = 2
-> chốt C trước vì 2 < 4
A -> C -> B = 5 + (-4) = 1
Xét B sau: A → B → C = 4 + (-3) = 1
Đường đi mới đến C là 1, ngắn hơn 2, nhưng C đã được chốt nên không cập nhật được
=> trả về kết quả 2 thay vì 1, nên kết quả sai

Thuật toán thay thế: có thể dùng Bellman-Ford, vì thuật toán này vẫn tìm đúng đường đi ngắn nhất khi đồ thị có cạnh trọng số âm (nếu không có chu trình âm)
