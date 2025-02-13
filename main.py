# ---------------------------------
# methods 파트

# 파이선의 데이터 구조는 list, tuple, dictionary
# data structure(자료 구조)는 데이터를 구조화 하고 싶을 때 사용한다

# mon = "Mon"
# tue = "Tue"
# wed = "Wed"
# thu = "Thu"
# fri = "Fri"

# list(배열)
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# print(days_of_week)

# name = "soontae"

# # upper()같은 변수와 연결되어 있는 함수들이 있다 이때 이런 함수들을 methods라고 한다
# methods는 데이터와 함수가 연결되어 있는 상태
# # upper 는 문자열을 대문자로 바꿔주는 메서드 이다
# print(name.upper())
# print(name.startswith("s"))
# print(name.replace("o", "!"))

# ---------------------------------
# lists 파트

# 특정 데이터 개수 세기
# print(days_of_week.count("Wed"))

# 데이터 추가하기
days_of_week.append("Sat")
days_of_week.append("Sun")

# 특정 데이터 삭제하기
days_of_week.remove("Fri")

# print(days_of_week)

# 특정 인덱스의 값 가져오기

# print(days_of_week[3])

# ---------------------------------
# tuples 파트

# tuple은 [] 대신 ()를 사용한다
# tuple은 변경이 불가능하다 | 불변성

day = ("Mon", "Tue", "Wed", "Thu", "Fri")

# print(day.count("Mon"))

# ---------------------------------
# Dicts 파트

player = {
    'name' : 'soontae',
    'age' : 20,
    'alive' : True,
    'fav_food' : ['pizza', 'burger']
}
# 딕셔너리는 많은 속성(타입)들을 가지고 있는 데이터를 만들 때 사용된다

# print(player.get('age'))

# print(player.get('fav_food'))
# print(player['fav_food']) | 위와 동일하게 작동함

# 딕셔너리에 데이터 삭제하기
# print(player)
# print(player.pop('age'))
# print(player)


# 딕셔너리에 데이터 추가하기
# print(player)
# player['xp'] = 1500
# print(player)

# 딕셔너리 리스트에 데이터를 추가하는 방법
player['fav_food'].append("noodle")
print(player.get('fav_food'))
