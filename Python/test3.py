

#stu = [
 #   {"name": "이순신", "kor":100 , "mat":90, "eng":80},
  #  {"name": "홍길동", "kor":90 , "mat":70, "eng":80},
   # {"name": "강감찬", "kor":80 , "mat":90, "eng":100}
    #]

## class 클래스명(첫문자는 대문자)
## def__init__(self,매개변수들)
## def 함수명(self.매개변수,기타 변수)

class Student:
    def __init__(self,name,kor,mat,eng):
        self.name=name
        self.kor=kor
        self.mat=mat
        self.eng=eng
        
    def std_hap(self):
        return self.kor+self.mat+self.eng

    def std_avg(self):
        return round(self.std_hap()/3,2)

##stu = [
##    Student("홍길동",100,50,90),
##    Student("이순신",90,70,80),
##    Student("강감찬",80,90,100)
##    ]

stu = []
stu.append(Student("홍길동",100,50,90))

for std in stu:
  #  hap = std["kor"]+std["mat"]+std["eng"]
  #  avg = hap/3

    print("{}의 합계는 {}이고 평균은 {}입니다.".format(std.name, std.std_hap(),std.std_avg()))
