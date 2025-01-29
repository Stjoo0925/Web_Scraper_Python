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