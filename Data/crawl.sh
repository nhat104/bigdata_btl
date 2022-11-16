py crawl_data.py 1 10
py crawl_data.py 11 20
py crawl_data.py 21 30
py crawl_data.py 31 40
py crawl_data.py 41 50
py crawl_data.py 51 60
py crawl_data.py 61 70
py crawl_data.py 71 80
py crawl_data.py 81 90
py crawl_data.py 91 100
py crawl_data.py 101 110
py crawl_data.py 111 120
py crawl_data.py 121 130
py crawl_data.py 131 140
py crawl_data.py 141 150
py crawl_data.py 151 160
py crawl_data.py 161 170



Dữ liệu của hệ thống là dữ liệu tuyển dụng liên quan đến lĩnh vực phần mềm, có thể thu thập được tại website TopCV. Tại thời điểm dữ liệu được thu thập, trên TopCV có tất cả 170 trang, file html của mỗi trang có chứa link đến đơn tuyển dụng của từng công ty. Hệ thống sẽ truy cập vào từng link và thu thập thông tin theo các thẻ. Mỗi đơn tuyển dụng sẽ được lưu thành một đối tượng json (một bản ghi), trong đó tên của các thẻ trong html và nội dung của các thẻ tương ứng sẽ tạo thành các cặp key-value. Một bản ghi sẽ bao gồm các trường sau:
- name (tên công ty tuyển dụng)
- Mô tả công việc
- Yêu cầu ứng viên
- Quyền lợi
- Cách thức ứng tuyển

Chương trình thu thập dữ liệu của hệ thống được lưu ở file crawl_data.py, sử dụng thư viện BeautifulSoup để parse các văn bản html. Để tăng tốc độ thực thi, hệ thống sử dụng một bash script để chạy song song 44 luồng cùng lúc, mỗi luồng thu thập dữ liệu trên 10 trang liên tiếp. Dữ liệu trả về được lưu ở 17 file json, tương ứng với kết quả chạy đồng thời của 44 luồng, mỗi file json sẽ bao gồm 25x10 = 250 bản ghi từ 10 trang đã thu thập
