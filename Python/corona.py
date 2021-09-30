# 모듈을 읽어 들입니다.
from urllib import request
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():

    link = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?"
    link += "serviceKey=zj%2BgF2pIXe8aXZgjKd53WlpzGACyXfz%2FXJTaZl057ITgPIiZ9Ty44jXS%2BuyIjjWsWrpzL3OpvCI21krPM3IiJw%3D%3D"
    link += "&pageNo=1&numOfRows=10&startCreateDt=20210726&endCreateDt=20210726"
    target = request.urlopen(link)
    # BeautifulSoup을 사용해 웹 페이지를 분석합니다.
    soup = BeautifulSoup(target, "html.parser")

    output = "<table border=´1´><tr><td>도시</td><td>총확진자</td><td>오늘 확진자</td></tr>"

    for item in soup.select("item"):
        output +="<tr>"
        output += "<td>{}</td>".format(item.select_one("gubun").string)
        output += "<td>{}</td>".format(item.select_one("defCnt").string)
        output += "<td>{}</td>".format(item.select_one("localOccCnt").string)
        output += "</tr>"
        output += "</table>"
    return output
