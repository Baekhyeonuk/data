

# 모듈을 읽어 들입니다.
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버를 생성합니다.
app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # BeautifulSoup을 사용해 웹 페이지를 분석합니다.
    soup = BeautifulSoup(target, "html.parser")

    # location 태그를 찾습니다.
    outout =""
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
        outout += "<h2>{}</h2>".format(location.select_one("city").string)
        outout += "날씨: {}<br/>".format(location.select_one("wf").string)
        outout += "<h5>최저/최고 기온: {}/{}</h5>"\
                  .format(\
                      location.select_one("tmn").string,\
                      location.select_one("tmx").string\
                      )
                
        outout += "<hr/>"
    return outout
