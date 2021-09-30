

#from datetime import datetime, timedelta

#x = datetime.now()

#print(x+timedelta(hours=2, weeks=3))
#print(x)
#print("오늘은 {}년{}월{}일 입니다.".format(x.year,x.month,x.day))
#print(x.strftime("%a"))

#x = datetime(2021,8,15)-datetime.now()

#print(x.days)

# 모듈을 읽어 들입니다.
#from urllib import request
#from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
#target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup을 사용해 웹 페이지를 분석합니다.
#soup = BeautifulSoup(target, "html.parser")

# location 태그를 찾습니다.
#for location in soup.select("location"):
# 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
   # print("도시:", location.select_one("city").string)
   # print("날씨:", location.select_one("wf").string)
   # print("최저기온:", location.select_one("tmn").string)
   # print("최고기온:", location.select_one("tmx").string)
  #  print()

import json

# a Python object (dict):
x = {
"name": "John",
"age": 30,
"city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(type(y))
