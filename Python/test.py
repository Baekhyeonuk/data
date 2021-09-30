## 상속

## 부모 클래스
class Cars:
    def __init__(self, name, color, price, speed):
        self.name = name
        self.color = color
        self.price = price
        self.speed = speed

    def speed_up(self, sp):
        return self.speed+sp

## 자식 클래스
class Suv(Cars):
    def __init__(self, name, color, price, speed, person):
        #Cars.__init__(self,name, color, price, speed)
        super().__init__(name, color, price, speed)
        self.person = person

    def speed_up2(self):
        return self.speed+100

car1 = Cars("벤틀리", "green", 2000, 100)
car2 = Suv("BMW", "blue", 3000, 200, 6)

print(car2.person)
print(car2.speed_up(50))
print(car2.speed_up2())
