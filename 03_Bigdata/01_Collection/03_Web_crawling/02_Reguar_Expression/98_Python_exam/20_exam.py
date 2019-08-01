import re
data = ['park@naver.com', 'kim@daum.net', 'lee@myhome.co.kr']
p = re.compile(".*[@].*[.](?=com|net)...")

for file_name in data:
    print(p.search(file_name))
