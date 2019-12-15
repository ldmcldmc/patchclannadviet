# patchclannadviet
Hướng dẫn đàn em patch được cái game từ cái thủa mà t mới biết có máy tính :))))

B1: Cài python 32bit

B2: Cài Rldev theo hướng dẫn https://www.baka-tsuki.org/project/index.php?title=OCamlInstall (Lưu ý thay bước tải TortoiseSVN bằng bước dùng bản này https://github.com/theappleman/rldev)
Index.php?title=OCamlInstall
Đây chỉ là patch text nên chỉ build đc kprl và rlc, để patch cg thì sang hỏi anh Hwan :slight_smile:
B2 có thể thay thế bằng folder này https://drive.google.com/open?id=1oUq5j858INKCINdFD0Jn1QrlTi5vlalV

B3 (quan trọng):
Để thư mục theo đúng đường dẫn :)
!!! - Ném hết file dịch vào folder seenviet
__- Liệt kê tất cả từ dangopedia bị dịch (ko dữ nguyên bản gốc) vào dangoword.txt
___- các file .txt lưu dưới dạng UTF-16 LE with BOM
Link công cụ: https://drive.google.com/open?id=1vfLUmZsUoT7_D0wPfUf3CGDX91oivC1o

B4: mở Cygwin, gõ lần lượt các lệnh:
cd z:
cd CLANNAD
kprl -d -v -f 1.5 -o  seens -e utf8 Seen.txt

B5: vào thư mục seens, copy và paste tất cả file ngay tại đó để tạo " - Copy"

B6: chạy file "patch text.py" (nếu cài pip và pyperclip trước thì các lệnh đã có ở trong clipboard)

B7 copy các lệnh hiển thị trên màn hình và paste vào cygwin :slight_smile:

Một số lỗi thường găp:

Lỗi lệch line do dangopedia, size to nhỏ, wait... --> gặp đâu thì vá đấy :slight_smile:
Lỗi cygwin ko nhận các ký tự lạ ---> thêm ký tự lạ vào bangma.txt và dùng \size{} \mvx{} mvy{} để tạo các ký tự lạ đó hoặc bỏ đi mà làm người
Lỗi cygwin ko thích \g :slight_smile: ---> kệ nó đi, cygwin bị chảnh đấy
các lỗi còn lại thì chịu khó search google + stackoverflow + tham khảo các tài liệu: https://www.google.com/search?client=firefox-b-d&q=rldev
