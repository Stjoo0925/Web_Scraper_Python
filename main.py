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
  # 함수를 작성할때 공백이 중요하다 | Tap or space bar * 2
  print("Hello how r u?")

# 함수를 호출하는 방법
say_hello()

# 함수에 파라미터(Parameter)를 넣는 방법
def say_hello_with_name(name):
  # 파라미터는 변수명과 같이 입력해준다, 파라미터의 변수명은 함수 내에서만 사용가능하다
  print("hello " + name + " how r u?")

# 함수에 인자를 넣어서 호출하는 방법
# 이떄 "soontae"는 인자(Argument)이다
say_hello_with_name("soontae")

# 멀티 파라미터 사용 방법
def say_hello_with_name_and_age(name, age):
  # 파라미터를 ,로 구분하여 여려개 사용할수 있다
  print(f"Hello {name} how r u? I'm {age} years old")

# 함수에 여러개의 인자를 넣어서 호출하는 방법
# 마찬가지로 ,로 구분하여 각각의 파라미터에 인자를 넣을수 있다 | 인자를 넣는 순서에 주의해야 한다
say_hello_with_name_and_age("soontae", 32)

# ---------------------------------
# 복습

def tax_calculator(money):
  print(money * 0.35)

tax_calculator(15000000)

# ---------------------------------
# 파라미터에 기본값 주기

def say_hello_default(name="anonymous"):
# "=" 이후에 기본값을 설정해줘서 인자가 없더라도 함수에 오류를 발생시키지 않는다
  print("hello " + name)

say_hello_default("soontae")
say_hello_default()

# ---------------------------------
# 계산기 만들기

def plus(a, b):
  print(a + b)

def minus(a, b):
  print(a - b)

def multiply(a, b):
  print(a * b)

def divide(a, b):
  print(a / b)

def power(a, b):
  print(a ** b)

def culcurator(symbols="", a=0, b=0):
  if symbols == "+":
    plus(a, b)
  elif symbols == "-":
    minus(a, b)
  elif symbols == "*":
    multiply(a, b)
  elif symbols == "/":
    divide(a, b)
  elif symbols == "**":
    power(a, b)
  else:
    print("잘못된 기호를 입력하셨습니다.")

culcurator("+", 1, 2)
culcurator("-", 1, 2)
culcurator("*", 1, 2)
culcurator("/", 1, 2)
culcurator("**", 1, 2)
culcurator("", 1, 2)
culcurator()

# ---------------------------------
# 리턴 파트

def tax_calc(money):
  # return 을 사용해서 함수의 값을 받아낼 수 있다
  return money * 0.35

def pay_tax(tax):
  print("thank you for paying", tax)

# 복잡한 변수 선언 없이 표현하는 방법
pay_tax(tax_calc(15000000))

# ---------------------------------
# 리턴 복습

my_name = "soontae"
my_age = 32
my_color_eyes = "brown"

# f-string | 문자열 포메팅 방법
print (f"Hello I,m {my_name} I have {my_age} years in the earth, {my_color_eyes} is my eye color")

# 쥬스 기계 만들기
def make_juice(fruit):
  return f"{fruit}+🍹"

def add_ice(juice):
  return f"{juice}+🧊"

def add_suger(iced_juice):
  return f"{iced_juice}+🍬"

# juice = make_juice("🍎")
# cold_juice = add_ice(juice)
# perfect_juice = add_suger(cold_juice)

# 체이닝을 사용한 코드 활용법 | 실행시간 및 메모리 효율증대
perfect_juice = add_suger(add_ice(make_juice("🍎")))

print(perfect_juice)

# return은 함수를 끝내버린다 즉 리턴이후의 함수내의 코드는 실행되지 않는다