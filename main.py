# 파일이름 :
# 작 성 자 :

#보유 미보유 리스트
owned = []
not_owned = ['목각 인형', '돌무덤', '물부리', '추억의 펜던트', '어느 날의 기억', '경외심', '상처붙이', '작고 나쁠 인형', '억류된 찬송', '밀라르카', '사원증', '순찰용 손전등', '휴대용 전지 소켓', '무정전 전원장치', '미니어처 전봇대']

#합성 목록
consums = ['추억', '치성', '인슐레이터']
consumed = []

#돈 가치
money = 0
value = 0

# 사용할 키워드 '출혈' '호흡' '충전'

# 시작 팩
start_breath = ['목각 인형', '돌무덤', '물부리']
start_bleed = ['경외심', '상처붙이', '작고 나쁠 인형']
start_charge = ['사원증', '순찰용 손전등', '휴대용 전지 소켓']



for i1 in range(999):
    print(f'보유중 {owned}')
    print(f'미보유 {not_owned}')
    print(f'-'*20)

    print(f'실행할 항목을 선택')
    print(f'1. 시작 아이템 팩 선택')
    print(f'2. 아이템 등록')
    print(f'3. 아이템 판매')
    print(f'4. 아이템 합성')
    print(f'5. 아이템 목록')
    print(f'6. 프로그램 종료')
    menu = int(input(f'번호 입력 : '))

    if menu == 1:
        print(f'시작 아이템 팩을 선택')
        start_pack = input(f"호흡 출혈 충전 중 입력 : ")

        if start_pack == '호흡':
            owned = list(start_breath)
            for item in start_breath:
                not_owned.remove(item)
            value += 150    
        elif start_pack == '출혈':
            owned = list(start_bleed)
            for item in start_bleed:
                not_owned.remove(item)
            value += 150    
        elif start_pack == '충전':
            owned = list(start_charge)
            for item in start_charge:
                not_owned.remove(item)
            value += 150    
        else :    
            print(f'잘못된 입력입니다.')
        continue  
    

    elif menu == 2:
        for i2 in range(3):
            add_item = input(f'등록할 아이템 이름 {i2 + 1} : ')
            if add_item in not_owned:
                value += float(input(f'아이템 가격 : '))
                not_owned.remove(add_item)
                owned.append(add_item)
            else:
                print(f'보유중이거나 존재하지 않는 아이템 입니다.')

    elif menu == 3:
        sell_item = input(f'판매할 아이템 이름 : ')
        if sell_item in owned:
            price = float(input(f'아이템 가격 : '))
            value -= price
            money += price
            owned.remove(sell_item)
            not_owned.append(sell_item)
        else:
            print(f'미보유이거나 존재하지 않는 아이템 입니다.')

    elif menu == 4:
        consum_item = input(f'합성할 이이템 이름 : ')
        if consum_item == '추억':
            if '추억의 펜던트'


    elif menu == 6:
        print(f'프로그램을 종료합니다.')
        break

    else:
        print(f'잘못된 입력입니다.')
        continue