# ---------------------------------
# if 파트

a = "soontae"

if a == "soontae":
  # if 이후의 조건이 참(True)이라면 아래의 코드가 실행된다
  print("True!")

# ---------------------------------
# else and elif 파트

# if
password_correct = False

if password_correct:
  # if의 조건이 참이 아니라면 아래의 else를 실행한다
  print("Here is your money")
else:
  # else는 반드시 사용 할 필요는 없다
  print("Wrong password")

# elif
winner = 20

if winner > 10:
  # False
  print("Winner is greater than 10")
elif winner < 10:
  # False | elif는 조건문에 추가의 조건이나 대안을 추가할수 있다
  print("Winner is less than 10")
else:
  print("Winner is 10")

# 조건문의 위에서 부터 순차적으로 참,거짓을 판단하여 참이 나오면 코드를 종료함

# ---------------------------------
# 조건문 복습

winner = 50

if winner <= 10:
  # != 는 다름 not을 표현하는 부호
  print("If")
elif winner <= 25:
  print("elif")
elif winner == 0:
  print("elif 2")
elif winner == 50:
  print("elif 3")
else:
  print("Else")

# 파이선의 조건문은 순차적으로 참,거짓을 판단하여 참일경우 아래의 조건을 확인하지않고 코드를 종료시키므로 구조를 고려해서 만들어야함

# ---------------------------------
# And, Or 복습

# 유저의 답변을 데이터로 저장하는 방법
age = input("How old are you?")

print("User answer ", age)
# type() 값의 타입을 알려주는 함수
# print(type(age)) || input의 값은 str 타입

# int() 문자열을 정수로 변환해주는 함수
age = int(age)

if age < 18:
  print("You can't drink.")
elif 18 <= age and age <= 35:
  # and 는 두개의 조건을 동시에 만족하는 경우 참
  print("You drink beer!")
elif age == 60 or age == 70:
  # or 는 하나의 조건만 참이더라도 참
  print("Birthday party!")
else:
  print("Go ahead!")

True and True == True
True and False == False
False and True == False
False and False == False

True or True == True
True or False == True
False or True == True
False or False == False
  