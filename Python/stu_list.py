
## class 클래스명(첫문자는 대문자)
## def__init__(self,매개변수들)
## def 함수명(self.매개변수,기타 변수)

## 부모 클래스
class Student:
    def __init__(self,name,kor,mat,eng):
        self.name=name
        self.kor=kor
        self.mat=mat
        self.eng=eng
        
    def hap(self):
        return self.kor+self.mat+self.eng
    def avg(self):
        return round(self.hap()/3,2)

## 자식 클래스
class Col(Student):
    
    def __init__(self,name,kor,mat,eng,dept):
        Student.__init__(self,name,kor,mat,eng)
        self.dept=dept

    def score(self):
        ## 평균값으로 학점 계산
        if self.avg() >=90:
            return "A학점"
        elif self.avg()>=80 and self.avg()<90:
            return "B학점"
        elif self.avg()>=70 and self.avg()<80:
            return "C학점"
        elif self.avg()>=60 and self.avg()<70:
            return "D학점"
        else:
            return "F학점"
        

##std1 = Col("홍길동",100,90,80,"체육학과")

##print(std1.name)
##print(std1.score())
    
        

stu = [
    Col("신유빈",100,90,80,"체육학과"),
    Col("황선우",90,90,80,"체육학과"),
    Col("김제덕",100,90,60,"체육학과")
    ]

##stu = []
##stu.append(Student("홍길동",100,50,90))

for std in stu:
  #  hap = std["kor"]+std["mat"]+std["eng"]
  #  avg = hap/3
    print("{}의 합계는 {}이고 평균은 {}이고 학점은 {}입니다.".format(std.name, std.hap(),std.avg(),std.score()))
