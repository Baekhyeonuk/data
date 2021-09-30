

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
    
    def score(self):
        if self.std_avg()>=90 :
            return "A학점"
        elif self.std_avg()>=80 and self.std_avg()<90:
            return "B학점"
        elif self.std_avg()>=70 and self.std_avg()<80:
            return "C학점"
        elif self.std_avg()>=60 and self.std_avg()<70:
            return "D학점"
        else:
            return "F학점"
        
stu = [
    ]

try:       
    for i in range(3):
        name = input("이름을 입력하세요 : ")
        kor = int(input("국어 점수 입력 : "))
        mat = int(input("수학 점수 입력 : "))
        eng = int(input("영어 점수 입력 : "))
        stu.append(Student(name,kor,mat,eng))
            
except:
    print(" *점수란에 숫자를 입력하세요* --프로그램 종료--")
        

for std in stu:
    
    print("{}의 성적 합계는 {}이고 평균은 {}이고 학점은 {}입니다.".format(std.name, std.std_hap(), std.std_avg(),std.score()))
