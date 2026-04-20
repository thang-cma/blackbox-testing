# Black-box Testing Assignment

## Nội dung
Gồm 8 bài toán:
- HCN (chu vi, diện tích)
- Phương trình bậc 2
- Số ngày trong tháng
- Số nguyên tố
- Tổng luân phiên
- UCLN
- Tổng giai thừa

## Phương pháp kiểm thử
Áp dụng kiểm thử hộp đen:
- Phân lớp tương đương
- Giá trị biên
- Dữ liệu hợp lệ & không hợp lệ

## Cấu trúc
- src/: mã nguồn
- tests/: test case

## Ghi chú
Mỗi bài đều có:
- kiểm tra input
- xử lý ngoại lệ
## Cách chạy chương trình

```bash
python3 run_tests.py
## Black-box Testing Description

Trong bài này, em áp dụng kiểm thử hộp đen cho từng bài toán dựa trên các kỹ thuật sau:

### 1. Phân lớp tương đương (Equivalence Partitioning)
Chia dữ liệu đầu vào thành các nhóm:
- Dữ liệu hợp lệ (valid): thỏa mãn điều kiện của bài toán  
- Dữ liệu không hợp lệ (invalid): vi phạm điều kiện (số âm, sai kiểu dữ liệu, giá trị không hợp lệ)

Ví dụ:
- Bài hình chữ nhật:  
  - valid: a > 0, b > 0  
  - invalid: a ≤ 0 hoặc b ≤ 0, hoặc kiểu dữ liệu không phải số  

---

### 2. Giá trị biên (Boundary Value Analysis)
Chọn các giá trị tại ranh giới của miền dữ liệu để kiểm thử:

Ví dụ:
- Bài số nguyên tố:
  - n = 1 (biên dưới, không phải số nguyên tố)
  - n = 2 (biên, là số nguyên tố)
- Bài tháng:
  - tháng = 1 và 12 (biên hợp lệ)
  - tháng = 0 và 13 (không hợp lệ)

---

### 3. Kiểm thử dữ liệu hợp lệ và không hợp lệ
Với mỗi bài toán, em đều xây dựng:
- Test case đúng → kiểm tra kết quả chính xác
- Test case sai → kiểm tra xử lý lỗi của chương trình

---

### 4. Áp dụng vào bài toán
Mỗi bài đều được:
- Xác định input/output
- Xây dựng test case theo các kỹ thuật trên
- Chạy test và lưu kết quả trong thư mục `results/`
