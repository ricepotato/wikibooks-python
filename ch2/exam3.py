this_year = 2021
birth_year = input("생년월일을 입력하세요 : ")
birth_year_int = int(birth_year) # input() 함수는 항상 문자열을 반환하므로 'int' 형태로 형변환 필요
age = this_year - birth_year_int
print(f"올해 당신의 나이는 {age}세 입니다.")
print(f"50세가 되는 해는 {this_year + 49 - age}년 입니다.")
