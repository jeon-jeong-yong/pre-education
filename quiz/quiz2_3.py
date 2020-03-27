'''
3.
Card 클래스를 생성해 카드에 충전기능, 소비기능, 잔액을 알려주는 기능을 넣으시오.
-충전기능 (charge)
-소비기능 (consume)
-영화관에서 카드를 사용하면 20% 할인율 적용
print 기능(print) # 잔액이 ( ) 원 입니다.

테스트코드
<입력>
card = Card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()

<출력>
잔액이 20000원 입니다.
마트에서 3000원 사용했습니다.
영화관에서 8000원 사용했습니다.
잔액이 부족합니다
잔액이 9000원 입니다.
'''

class Card :
    def __init__(self):
        self.잔액 = 0

    def charge(self,x):
        print("잔액이 {}원 입니다.".format(x))
        self.잔액 += x
        return self.잔액

    def consume(self,지출,장소):
        if 장소 == "영화관" :
            할인금액 = int(지출 * 0.8)
            if 할인금액 <= self.잔액 :
                print("{}에서 {}원 사용했습니다.".format(장소, 할인금액))
                self.잔액 -= 할인금액
                return self.잔액
            else :
                print("잔액이 부족합니다.")
        else :
            if 지출 <= self.잔액 :
                print("{}에서 {}원 사용했습니다.".format(장소, 지출))
                self.잔액 -= 지출
                return self.잔액
            else :
                print("잔액이 부족합니다.")

    def print(self):
        print("잔액이 {}원 입니다.".format(self.잔액))


#입력될 부분
card = Card()
card.charge(20000)
card.consume(3000,'마트')
card.consume(10000,'영화관')
card.consume(13000,'마트')
card.print()