class Atm:
    def __init__(self, name):
        self.account = {}
        self.count = 1000
        self.name = name
    def makeAccount(self):
        self.acount[self.count] = 0
        self.count += 1
        
    def deposit(self, account, money):
        if self.checkAccount(account):
            self.account[account] += money
            return True
        self.message = "계좌정보가 없습니다."
        return False
        
    def withdraw(self, account, money):
        if not self.checkAccount(account):
            self.message = "계좌정보가 없습니다."
            return False
        if self.account[account] >= money:
            self.account[account] -= money
            return True
        return False
    
    def checkAccount(self, account):
        if account in self.account.keys():
            return True
        return False
    
    def infoAccount(self, account):
        print(f"계좌번호: {account}")
        print(f"잔액: {self.account[account]} 원")
        
    def remittance(self, recipient, senderAccountNumber, recipientAccountNumber, money):
        if not checkPeople(recipient):
            self.message = f"{recipient}님은 없습니다."
            return False
        if not self.checkAccount(senderAccountNumber):
            self.message = f"{self.name}님의 {senderAccountNumber} 번호인 계좌는 없습니다."
            return False
        self.infoAccount(senderAccountNumber)
        if self.account[senderAccountNumber] < money:
            self.message = "잔액이 부족합니다."
            return False
        self.withdraw(senderAccountNumber, money)
        recipient.deposit(recipientAccountNumber, money)
        self.message = f"{recipient.name}님께 {money}원을 정상적으로 송금하였습니다."
        return True


james = Atm("James")
ann = Atm("Ann")
tom = Atm("Tom")
users = [james, ann, tom]

def checkPeople(name):
    for i in users:
        if i.name == name:
            return True
    return False

def checkPeopleInstance(name):
    for i in users:
        if i.name == name:
            return i

def allAccountBalance():
    for i in users:
        print(f"이름: {i.name}")
        for j in i.account.keys():
            i.infoAccount(j)

def main():
    check = 0
    while (check != 6):
        print("1. 입금")
        print("2. 출금")
        print("3. 송금")
        print("4. 개인 별 잔액조회")
        print("5. 전체 잔액조회")
        print("6. 종료")
        check = int(input("입력하세요: "))
        if check == 1:
            name = input("사용자를 입력해주세요: ")
            money = input("입금할 금액을 입력해주세요: ")
            name = checkPeopleInstance(name)