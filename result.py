import random

decorate_main = ('어디로 튈지 모르고' ,'개성 있고', '자유분방하며', '편안하며', '꾸밈없고', '자연스러우면서', '패션 감각 있고', '트렌디하고', '품격있고', '우아하고', '멋쟁이이면서', '스타일리쉬하고', '디자이너가 꿈이며', '존경스럽고')
decorate_sub = ('부끄러운', '조용한', '내성적인', '순수한', '따뜻한', '친절한', '유머러스한', '긍정적인', '열정적인', '도전적인', '독특한', '개성 있는')
decorate_dep = ('독수리', '코끼리', '호랑이', '사자', '토끼', '거북이', '고슴도치')

clothlist_outer = [('롱패딩', '후드 집업'), ('재킷', '트러커 재킷'), ('숏패딩',), ('코트',)]
clothlist_inner = [('후드',), ('맨투맨', '니트'), ('화이트 셔츠', '니트'), ('화이트 셔츠', '목폴라')]
clothlist_under = [('데님 팬츠', '슈트 팬츠'), ('데님 팬츠', '조거 팬츠'), ('데님 팬츠', '코튼 팬츠'), ('데님 팬츠',)]

def calc_total(operations):
    total_main = 0
    total_sub = 0
    dep = 0

    for val in operations:
        if val[-1] == '+':
            increase = 1
        else:
            increase = -1

        if val[0] == 'm':
            total_main += increase
        elif val[0] == 's':
            total_sub += increase
        else:
            dep += 1

    return total_main, total_sub, dep

def combination_process(clothes, num):
    if len(clothes[num]) > 1:
        index = random.randint(0, len(clothes[num]) - 1)
        element = clothes[num][index]

        return element
    else:
        return clothes[num][0]

def get_recommendations(type, type_num):
    global clothlist_outer, clothlist_inner, clothlist_under

    result = []

    # 옷 별로 수식어 추가?
    # 함수 내 함수로 코드 축소??
    if type[0] == 'n':
        result.append(combination_process(clothlist_outer, type_num))
        result.append(combination_process(clothlist_inner, type_num))
        result.append(combination_process(clothlist_under, type_num))
    else:
        if type_num > 1 and type_num < 4:
            outer = random.randint(type_num - 1, type_num + 1)
            inner = random.randint(type_num - 1, type_num + 1)
            under = random.randint(type_num - 1, type_num + 1)
        elif type_num == 1:
            outer = random.randint(type_num, type_num + 1)
            inner = random.randint(type_num, type_num + 1)
            under = random.randint(type_num, type_num + 1)
        else:
            outer = random.randint(type_num - 1, type_num)
            inner = random.randint(type_num - 1, type_num)
            under = random.randint(type_num - 1, type_num)

        result.append(combination_process(clothlist_outer, outer))
        result.append(combination_process(clothlist_inner, inner))
        result.append(combination_process(clothlist_under, under))

    return result

def get_result(operations):
    total_main, total_sub, dep = calc_total(operations)

    if total_main > -7 and total_main <= -3:
        typenum = 0
    elif total_main > -3 and total_main < 0:
        typenum = 1
    elif total_main >= 0 and total_main < 4:
        typenum = 2
    else:
        typenum = 3

    if total_sub > 0:
        user_adv = 'go_type'
    else:
        user_adv = 'no_type'

    result = {
        'keywords': {
            'main': decorate_main[total_main + 7],
            'sub': decorate_sub[total_sub + 5],
            'dep': decorate_dep[dep]
        },
        'recs': get_recommendations(user_adv, typenum)
    }

    return result