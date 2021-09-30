
import score as Student
## score 모듈에서 Student 생성자 함수를 이용해 std객체를 생성합니다.
std = Student("홍길동",100,90,50)

print(std.name)
print("{} 학생의 합계는 {}이고 평균은 {}입니다.".format(std.name,std.std_hap(),std.std_avg()))
