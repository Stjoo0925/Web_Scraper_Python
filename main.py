print("Hello World!")

# ---------------------------------
# 변수 파트

a = 2
b = 3
c = a + b

print(c)
# 파이선은 위에서 아래로 코드를 읽는다

my_age = 88
""" 
* 파이선의 변수 관행은 _(언더스코어)
* 변수의 앞부분은 숫자, 특수문자가 될 수 없음
"""

# ---------------------------------
# 타입 파트

# 숫자
a_number = 654

# 문자열 - "" or '' 로 작성가능
name_string = "soontae"

# 불린 - True or False , 첫 글자는 반드시 대문자
boolean = True

print(a_number, name_string, boolean)

# ---------------------------------
# 복습

my_name = "soontae"
age = 32
dead = False

print("Hello my name is", my_name)
print("and I'm", age, "years old")

# ---------------------------------
# 함수 파트

print(True)
print("Hello")
print(12)
# 예시로 print 함수는 콘솔창에 출력하기 위한 재사용 가능한 함수이다

# 함수를 정의하기 위한 방법
def say_hello():
  # 함수명 선언 방식은 변수 선언 방식과 동일하다
  print("Hello how r u?")

# 함수를 호출하는 방법
say_hello()
