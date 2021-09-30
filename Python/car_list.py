

##클래스명 : Cars
##이름,색상,가격,스피드
##speed_up 함수 스피를 받아서 +100을 리턴

class Cars:
    def __init__(self,name,color,price,speed):
        self.name=name
        self.color=color
        self.price=price
        self.speed=speed

    def speed_up(self,sp):
        return self.speed+sp

car = [
    Cars("페라리","blue",1000,200),
    Cars("테슬라","red",500,180),
    Cars("벤틀리","white",2000,250)
    ]

for cars in car:
    print("내가 사고싶은 자동차는 {}이고 가격은 {}입니다.".format(cars.name,cars.price))
    print("{}의 속도를 올리면 {}가 됩니다".format(cars.name,cars.speed_up(70)))


##print("내가 사고싶은 자동차는 {}이고 가격은 {}입니다.".format(car1.name,car1.price))
##print("{}의 속도를 올리면 {}가 됩니다".format(car1.name,car1.speed_up(70)))


##1.자동차 객체를 여러개 생성해서 리스트의 요소 만들기
##2.모듈 생성
##
##합계와 평균 구하기
##
##모듈을 import 사용하기
##
##3. 확인문제 1번
##
##4. 코로나 출력에서 자동으로 오늘 날짜 불러오기.
