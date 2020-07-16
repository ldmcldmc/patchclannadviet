# patchclannadviet
> Hướng dẫn đàn em patch được cái game từ cái thủa mà t mới biết có máy tính :))))

> Video hướng dẫn : https://www.youtube.com/watch?v=hoNChLgenfg&feature=youtu.be

> Các bước tiến hành:

**Bước 1:**
- Cài python 32bit
- cài pip install pyperclip

**Bước 2:**
- Tải folder này https://drive.google.com/open?id=1oUq5j858INKCINdFD0Jn1QrlTi5vlalV
- Thêm máy ảo vào Oracle VM VirtualBox
- Chỉnh lại một số thiết đặt.
- (Hoặc Cài Rldev theo hướng dẫn https://www.baka-tsuki.org/project/index.php?title=OCamlInstall (Lưu ý thay bước tải TortoiseSVN bằng bước dùng bản này https://github.com/theappleman/rldev). Đây chỉ chỉ build kprl và rlc nên chỉ có thể patch text, để patch cg thì sang hỏi anh Hwan :slight_smile:)

**Bước 3 (quan trọng):**
- Để thư mục theo đúng đường dẫn (D:\CLANNAD)
- Đặt gói công cụ hỗ trợ theo đúng đường dẫn
- Liệt kê tất cả các từ dangopedia bị dịch vào dangoword.txt
- các file .txt lưu dưới dạng UTF-16 LE with BOM

**Bước 4:** 
- mở Cygwin, gõ lần lượt các lệnh:
```cygwin
cd z:
cd CLANNAD
kprl -d -v -f 1.5 -o  seens -e utf8 Seen.txt
```
**Bước 5:**
- Vào thư mục seens, copy và paste tất cả file ngay tại đó để tạo " - Copy"

**Bước 6:** 
- chạy file "patch text.py" (nếu cài pip và pyperclip trước thì các lệnh đã có ở trong clipboard)

**Bước 7:** 
- Copy các lệnh hiển thị trên màn hình và paste vào cygwin :slight_smile:

> Tổng hợp 1 số lỗi thường gặp:

- Lỗi lệch line do dangopedia, size to nhỏ, wait... --> gặp đâu thì vá đấy :slight_smile:
- Lỗi cygwin ko nhận các ký tự lạ ---> thêm ký tự lạ vào bangma.txt và dùng \size{} \mvx{} mvy{} để tạo các ký tự lạ đó hoặc bỏ đi mà làm người
- Lỗi cygwin ko thích \g :slight_smile: ---> kệ nó đi, cygwin bị chảnh đấy
- các lỗi còn lại thì chịu khó search google + stackoverflow + tham khảo các tài liệu: https://www.google.com/search?client=firefox-b-d&q=rldev
