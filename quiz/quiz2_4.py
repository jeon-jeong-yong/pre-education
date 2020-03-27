'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''


class 할인 :
    def discount(self, 금액, 장소):
        if 장소 == "영화관":
            할인금액 = 금액 * 0.8
            if 할인금액 <= self.잔액 :
                self.잔액 -= 할인금액
                print("영화관에서 {}원을 사용했습니다.".format(할인금액))
            else :
                print("잔액이 부족합니다.")
        elif 장소 == "마트" :
            할인금액 = 금액 * 0.9
            if 할인금액 <= self.잔액 :
                self.잔액 -= 할인금액
                print("마트에서 {}원을 사용했습니다.".format(할인금액))
            else :
                print("잔액이 부족합니다.")
        elif 장소 == "교통" :
            할인금액 = 금액 * 0.9
            if 할인금액 <= self.잔액 :
                self.잔액 -= 할인금액
                print("교통에서 {}원을 사용했습니다.".format(할인금액))
            else :
                print("잔액이 부족합니다.")

class Multi_card(할인) :
    print("카드가 발급되었습니다.")
    def __init__(self) :
        self.잔액 = 0

    def charge(self, 충전) :
        print("{}이 충전되었습니다.".format(충전))
        self.잔액 += 충전
        return self.잔액

    def consume(self, 금액, 장소) :
        super().discount(금액, 장소)
        return self.잔액

    def print(self):
        print("잔액이 {}원 입니다.".format(self.잔액))

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()