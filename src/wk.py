class Account:
    def __init__(self, aid, abl):
        self.aid = aid
        self.abl = abl
    def __iadd__(self, m):
        self.abl += m
    def __isub__(self, m):
        self.abl -= m
    def __str__(self):
        return "self.aid, self.abl"

names = ['James', 'Ann', 'Tom']

anct_J = Account('James01', 100)
acnt_A = Account('Ann01', 100)
acnt_T = Account('Tom01', 100)

def main():
    
    
    while True:
        
        name = input("성함 : ")
        print("----------메뉴------------")
        print("1. 입금")
        print("2. 송금")
        print("3. 잔액 확인")
        print("4. 계좌 생성")
        print("5. 전체 사용자 잔액 출력")
        print("0. 종료")

        menu = int(input("메뉴를 선택하세요"))
        if menu == 1 :
            money = input("얼마를 입금하시겠습니까? ")
            if name == "James":
                acnt_J += money
            elif name == "Ann":
                acnt_A += money
            elif name == "Tom":
                acnt_T += money
            else:
                print("잘못된 입력입니다,")
        if menu == 2:
            to = input("누구에서 송금하시겠습니까? ")
            money = input("금액 : ")
            if name == "James":
                if to == "Ann":
                    acnt_A += money
                elif to == "Tom":
                    acnt_T += money
                else:
                    print("잘못된 입력입니다.")
                acnt_J -= money
                    
            elif name == "Ann":
                if to == "James":
                    acnt_J += money
                elif to == "Tom":
                    acnt_T += money
                else:
                    print("잘못된 입력입니다.")
                acnt_A -= money
            
            elif name == "Tom":
                if to == "Ann":
                    acnt_A += money
                elif to == "James":
                    acnt_J += money
                else:
                    print("잘못된 입력입니다.")
                acnt_T -= money

        elif menu == 0:
            break
