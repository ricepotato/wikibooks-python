# 변수와 자료형

## 변수

변수란 python 에서 어떠한 데이터를 임시로 저장하기 위해 사용하는 그릇 입니다. 변수는 아래와 같은 형식으로 생성할 수 있습니다.

```python
변수명 = 값
```

왼쪽에는 변수 이름을 쓴 다음 '=' 기호를 넣고 해당 변수에 저장할 값을 오른쪽에 적습니다.

그러면 실제 코드를 한번 살펴 보겠습니다. 아래와 같이 python 코드를 작성해 보세요.

```python
>>> age = 10
>>> name = "potato"
```

위 코드에서 'age' 와 'name' 은 변수 이름 입니다. python 인터프리터가 위 코드를 실행하면 컴퓨터의 메모리 어딘가에 10 이라는 숫자값과 "potato" 라는 문자열을 저장합니다.

변수를 어떤 데이터를 담는 그릇이라고 생각하면 이해하기 편합니다. 각 그릇에 이름을 정할 수 있고 각각의 그릇에 담긴 변수는 나중에 꺼내 사용할 수 있습니다. 아래와 같이 코드를 작성해 보세요.

```python
>>> name = "potato"
>>> text = "제 이름은 %s 입니다." % name
>>> print(text)
제 이름은 potato 입니다.
```

위 예제 코드에서는 'name' 변수에 값을 담은 다음 맨 아랫줄 print() 함수 내에서 저장한 값을 불러와 사용 했습니다.

위 예제와 같이 print() 함수 안에 %s 와 % 를 사용하면 변수에 있는 값을 가져와 합쳐서 출력할 수 있습니다.

변수에서 값을 가져와 합쳐서 문자열을 만드는 예제를 하나 더 살펴보겠습니다. 아래와 같이 입력해 보세요

```python
>>> age = 15
>>> print("제 나이는 %s세 입니다." % age)
제 나이는 15세 입니다.
```

변수 내의 값은 임시로 저장되는 값이기 때문에 언제든 값을 변경할 수 있습니다. 아래와 같이 코드를 작성해 보세요.

```python
>>> age = 15
>>> print("제 나이는 %s세 입니다." % age)
제 나이는 15세 입니다.
>>> age = 20
>>> print("제 나이는 %s세 입니다." % age)
제 나이는 20세 입니다.
```

처음에 'age' 변수에 값 15를 저장한 다음 print() 함수에서 age 값을 불러와 사용했습니다. 이후에 'age' 변수에 새로운 값 20을 저장한 다음 print() 함수를 사용해서 age 의 값 20을 불러와 사용했습니다.

위와 같이 변수에는 값을 여러번 할당할 수 있으며 **새로운 값을 저장하면 기존의 값은 삭제**됩니다.

❕ 마지막으로 저장한 값만 유효하다는 것에 유의하세요!

변수의 이름은 여러분 마음대로 정할 수 있지만, 아래와 같은 약간의 제약사항이 있습니다.

- 영문자 또는 \_(언더바) 로 시작해야 합니다.
- \_(언더바) 를 제외한 특수문자를 사용할 수 없습니다.
- 숫자로 시작할 수 없습니다.
- 예약된 키워드를 사용할 수 없습니다.
- 공백을 넣을 수 없습니다.

아래의 예제들은 잘못된 변수 이름을 설정했을때 python 인터프리터가 발생시키는 오류입니다.

```python
>>> my-age = 10
  File "<stdin>", line 1
    my-age = 10
    ^
SyntaxError: cannot assign to operator
```

'-' (hyphen) 은 python 이 뺄셈 연산자로 인식하기 때문에 변수이름에 들어갈 수 없습니다.

```python
>>> myage! = 10
  File "<stdin>", line 1
    myage! = 10
         ^
SyntaxError: invalid syntax
```

'myage!' 는 느낌표 특수문자 부분에서 SyntaxError 가 발생 합니다.

```python

>>> 3_times = 3
  File "<stdin>", line 1
    3_times = 3
     ^
SyntaxError: invalid decimal literal
```

'3_times' 는 변수 이름이 숫자로 시작하기 때문에 SytaxError 가 발생했습니다.

```python
>>> if = 33
  File "<stdin>", line 1
    if = 33
       ^
SyntaxError: invalid syntax

>>> a v = 50
  File "<stdin>", line 1
    a v = 50
      ^
SyntaxError: invalid syntax
```

위 SyntaxError 오류는 키워드(if) 를 변수이름으로 사용하거나, 변수이름에 공백이 있는 경우 발생합니다.

```python
>>> Yourname = "tomato"
>>> print(yourname)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'yourname' is not defined
```

위 오류는 프로그램 어디에서도 'yourname' 이라는 변수에 값을 설정한 적이 없는데, 값을 가져오려고 했기 때문에 NameError 가 발생 했습니다. 변수는 어떤 값을 가질때에만 유효합니다.

위 예제의 첫번째 줄에서 사용한 변수 이름은 'Yourname'(첫번째 문자가 대문자) 입니다. python 의 변수이름은 대소문자를 엄격하게 구분하기 때문에 대소문자를 섞어서 사용하는 경우 주의가 필요합니다.

만약 위와같이 NameError 가 발생 했다면 변수 이름에 오타가 없는지 확인해 보세요. 😅

## 자료형

### 숫자형

파이썬에서 다룰 수 있는 숫자에는 몇가지 종류가 있습니다. 아래 예제를 살펴보겠습니다.

```python
>>> integer_value = 20 # 정수 (interger)
>>> float_value = 3.1 # 실수 (float)
```

가장 윗줄의 'integer_number' 변수에 담긴 값은 20 이고 이 값은 정수 입니다. 정수는 소수점이 없는 값이고 대부분의 프로그래밍 언어에서는 이러한 종류의 값을 'integer' 라고 부릅니다.

두번째 줄의 'float_value' 변수에 담긴 값은 3.1 이고 이 값은 실수 입니다. 실수는 소수점이 있는 값이고 python 에서는 이 값의 타입을 'float' 이라고 부릅니다.

### bool

bool 은 참 또는 거짓을 나타내는 값입니다. 아래의 코드와 같이 'is_alive' 변수에 bool 값을 저장할 수 있습니다.

```python
>>> is_alive = True
>>> is_dead = False
>>> print(is_alive)
True
>>> print(is_dead)
False
```

위 코드에서 True 와 False 는 python 의 bool 값 예약어 입니다. 각각 가장 앞 문자가 대문자임에 유의하세요 !

```python
>>> is_run = true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
```

위 코드와 같이 가장 앞 문자가 대문자가 아닌 true 를 변수에 저장하려고 하면 오류가 발생합니다.

대문자가 아닌 true 는 는 python 인터프리터가 변수 식별자로 인식하기 때문에 NameError 가 발생합니다.

### 문자열(str) 형

아래의 코드는 변수에 문자열을 담는 코드입니다.

```python
>>> string_value = '문자열1' # 문자열 (str)
>>> string_value2 = "문자열2"
>>> string_value3 = """문자열3"""
```

문자열은 '(single qoute), "(double qoute), """(triple qoute) 를 사용해서 문자열을 생성할 수 있습니다. 위 예제에서와 같이 문자열로 만들고 싶은 텍스트를 " " 로 감싸서 문자열을 만듭니다.

아래 예제 살펴보겠습니다.

```python
>>> my_str = """I
am
potato.
"""

>>> print(my_str)
I
am
potato.

>>> my_str2 = '안녕!
파이썬!'
>>> my_str = '안녕!
  File "<stdin>", line 1
    my_str = '안녕!
                 ^
SyntaxError: EOL while scanning string literal
```

보통은 ' 와 " 를 주로 사용하지만 """ 는 문자열 안에 개행이 들어가거나 python 코드 내에 주석문을 입력할때 사용합니다.
위 예제와 같이 ' 내에 엔터를 입력해서 개행하면 SytaxError 가 발생합니다.

문자열 내에 " 를 포함시켜야 하는 경우 ' 를 사용합니다. 반대의 경우에 "" 를 사용합니다. 아래 예제를 참고하세요.

```python
>>> text = '밤하늘에 반짝이는 별들을 보면서 "나는 아무 걱정도 없이 가을 속의 별들을 다 헬듯합니다." 라는 시구를 떠올렸다.'
>>> print(text)
밤하늘에 반짝이는 별들을 보면서 "나는 아무 걱정도 없이 가을 속의 별들을 다 헬듯합니다." 라는 시구를 떠올렸다.

>>> text = "나는 '일이 다 틀렸나 보군.' 하고 생각하였다."
>>> print(text)
나는 '일이 다 틀렸나 보군.' 하고 생각하였다.
```

#### 문자열 다루기

문자열을 다루는 간단한 방법을 살펴보겠습니다. 앞서 print() 함수를 사용할 때 변수의 값을 가져와 문자열 안에 포함시키는 방법을 배웠습니다. 이번에는 여러 변수의 값을 문자열에 포함시키는 다른 방법 몇가지를 알아보겠습니다. 아래와 같이 작성하면 문자열에 변수를 포함시킬 수 있습니다.

```python
>>> age = 12
>>> name = "tomato"
>>> text = "저의 이름은 " + name + " 이고, 나이는 %s세 입니다." % age
>>> print(text)
저의 이름은 tomato 이고, 나이는 12세 입니다.
```

문자열 과 'name' 변수 사이에 + 연산자를 사용 했습니다. + 연산자는 문자열 사이에 들어가게 되면 두 문자열을 합친 새로운 문자열을 만들어 냅니다.

그런데 'age' 변수의 값을 문자열과 합칠 때는 + 연산자를 사용해서는 안됩니다. 'age' 변수에 들어있는 값은 'int' 형태이기 때문에 문자열과 + 연산자를 사용해서 합칠 수 없습니다. 아래 예제를 참고하세요.

```python
>>> age = 12
>>> name = "potato"
>>> print(name + age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

'age' 와 'name' 을 합치려고 + 연산자를 사용했지만 TypeError 가 발생 했습니다. str 과 str 만 합칠 수 있다는 오류 메시지가 출력됩니다. 따라서 + 연산자를 사용할 때는 합치려는 두 값이 문자열 일때만 사용할 수 있습니다.

반면 아래 코드는 오류가 발생하지 않습니다.

```python
>>> text1 = "ABCD"
>>> text2 = "EFGH"
>>> print(text1 + text2)
ABCDEFGH
```

그렇다면 문자열인 값과 숫자인 값을 + 연산자를 사용해서 합치려면 어떻게 해야 할까요?

아래 코드를 보고 문자열 값과 숫자 값의 타입을 확인해 봅시다.

```python
>>> age_str_value = "17"
>>> age_int_value = 17

>>> print(age_str_value) # 문자열 값 출력
17
>>> print(age_int_value) # 숫자 값 출력
17

>>> age_str_value + age_int_value # 덧셈 연산자 사용. 오류 발생.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

>>> age_str_value # 문자열 변수를 그대로 입력
'17'
>>> age_int_value # 숫자 변수를 그대로 입력
17

>>> type(age_str_value)
<class 'str'>
>>> type(age_int_value)
<class 'int'>
```

위 코드는 int 값과 str 값의 차이를 보여줍니다. print() 함수를 사용해서 두 값을 출력해 보면 같아 보이지만, python 인터프리터에 해당 변수값을 그냥 입력한 경우에는 다르게 출력됩니다. 그리고 타입이 다르기 때문에 + 연산자를 사용해서 합치려고 하면 TypeError 가 발생합니다.

type() 함수는 입력받은 값의 type 출력합니다. age_str_value 는 'str' 타입임을 확인할 수 있습니다.

그러면 이번에는 문자열 값을 숫자로, 숫자 값을 문자로 변환하는 방법을 알아보겠습니다. 아래 코드를 살펴보세요.

```python
>>> age_str_value + str(age_int_value) # str() 함수를 이용해서 'int' -> 'str' 타입 변환
'1717'
>>> int(age_str_value) + age_int_value # int() 함수를 이용해서 'str' -> 'int' 타입 변환
34
```

앞서 두 문자열 사이에 + 연산자를 사용하면 두 문자열을 합친 새로운 문자열을 생성한다고 설명 했습니다.

'age_int_value' 변수에 저장되어있는 'int' 타입의 숫자값을 str() 함수를 사용해서 변환한 다음 + 연산자를 사용하면 오류 없이 두 문자열이 합쳐져서 '1717' 이라는 문자열이 생성됩니다. python 인터프리터에 표현식을 직접 입력했기 때문에 바로 아래줄에 문자열이 출력되었습니다.

두번째 줄은 'age_str_value' 변수에 저장되어있는 'str' 타입의 문자값을 int() 함수를 사용해서 변환한 다음 + 연산자를 사용했습니다. 결과적으로 17 + 17 표현식의 결과값인 34 가 출력되는 것을 확인할 수 있습니다.

이제 + 연산자를 사용해서 문자열과 숫자를 합쳐서 새로운 문자열을 만들 수 있게 됐습니다. 아래 코드와 같이 작성하면 됩니다. 😄

```python
>>> age = 12
>>> name = "tomato"
>>> text = "저의 이름은 " + name + " 이고, 나이는 " + str(age) + "세 입니다."
>>> print(text)
저의 이름은 tomato 이고, 나이는 12세 입니다.
```

아래 코드는 위 코드와 같은 기능을 하는 또 다른 방법 입니다. 아래에 소개되는 방법을 사용하면 문자와 숫자를 구분하지 않아도 됩니다.

아래 코드를 따라서 작성해 보세요.

```python
>>> age = 12
>>> name = "tomato"
>>> text = "저의 이름은 '{}' 이고 나이는 {}세 입니다.".format(name, age)
>>> print(text)
저의 이름은 'tomato' 이고 나이는 12세 입니다.
```

위 코드는 문자열 '메소드'인 format() 을 사용하는 방법 입니다. '메소드' 에 대해서는 나중에 자세히 다루겠습니다. 여기서는 문자열을 합쳐주는 기능을 하는 것 이라는 것 정도만 알고 넘어가면 됩니다.

문자열 내에 {}(braces) 를 포함시킨 다음 뒤에 .format() 을 입력해서 해당 위치에 들어갈 값을 넣어주면 됩니다.

```python
>>> age = 12
>>> name = "tomato"
>>> text = f"저의 이름은 '{name}' 이고 나이는 {age}세 입니다."
>>> print(text)
저의 이름은 'tomato' 이고 나이는 12세 입니다.
```

두번째 방법은 f-string 입니다. 문자열의 시작을 나타내는 " 앞에 f 를 붙인다음 {} 내에 출력하고 싶은 변수를 넣으면 됩니다.

지금까지 소개된 방법 중 어떤 것을 사용해도 좋습니다. 😀

#### 연산자

여러가지 자료형을 알아봤으니 이번에는 python 에서 사용할 수 있는 몇가지 연산자를 알아보겠습니다. 연산자는 연산자의 오른쪽 왼쪽에 있는 값의 type 이 무엇이냐에 따라 다르게 동작하고 오류가 발생할 수 있다는 것을 배웠습니다.

아래 예제들을 보면서 여러 연산자 사용해 보겠습니다.

+, - 연산자는 잘 알다시피 덧셈, 뺄셈 연산자 입니다. + 연산자는 문자열, list 사이에 들어가는 경우 똑같이 동작합니다.

```python
>>> integer_value = 20
>>> integer_value + float_value
23.1
>>> "hello" + "python"
'hellopython'
>>> [1, 2, 3, 4] + [5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
```

python 에는 += 라는 연산자도 있습니다. 이 연산자는 연산자의 왼쪽에 있는 변수에 오른쪽에 있는 값을 더해서 왼쪽 변수에 저장합니다. 이 연산자는 문자열, list 타입의 변수에도 똑같이 동작합니다.

아래 예제를 입력해 보세요.

```python
>>> a = 3
>>> a += 4 # a = a + 4
>>> print(a)
7

>>> firstname = "rice"
>>> firstname += "potato" # firstname = firstname + "potato"
>>> firstname
'ricepotato'

>>> number_list = [1, 2, 3, 4]
>>> number_list += [5, 6, 7] # number_list = number_list + [5, 6, 7]
>>> number_list
[1, 2, 3, 4, 5, 6, 7]
```

python 인터프리터에 표현식을 입력하면 해당 값이 평가되어 그대로 출력되어 마치 계산기처럼 결과값을 확인할 수 있습니다.

파이썬에서의 곱셈과 나눗셈은 \*, / 연산자를 사용합니다.

```python
>>> 13 / 5
2.6
>>> 2 * 3
6
>>> 10 / 2 # 나눈 값은 float type 이 됨
5.0
>>> 3.0 * 3
9.0
```

앞서 문자열 합치기에 사용했던 % 연산자는 숫자와 숫자 사이에 사용될 경우 나머지 연산자가 됩니다.
하지만 % 왼쪽에 문자열을 사용하는 경우에는 문자열과 오른쪽에 있는 값을 합쳐 새로운 문자열을 만드는 기능을 합니다.

```python
>>> 10 % 4 # 숫자 사이에 % 연산자를 사용하면 나머지 값이 출력됨
2
>>> 10 % 3
1

>>> "hello %s" % "python" # 문자열과 문자열 사이에 % 연산자를 사용하면 문자열을 합침
'hello python'
```

### 리스트 (list)

## 연습문제

아래 예제는 input() 함수 예제입니다. input() 함수는 입력받은 문자열을 변수에 담는 기능을 가지고 있습니다. input() 함수가 호출되면 프로그램이 실행을 잠시 멈추고 사용자의 입력을 기다리는 상태가 됩니다.

이 상태에서 값을 입력하면 input() 함수는 입력받은 값을 변수에 저장해 줍니다.

아래 프로그램을 작성해 보세요.

exam1.py

```python
name = input("이름을 입력하세요 : ")
print(f"당신의 이름은 {name} 입니다.")
```

위 프로그램을 실행하면 아래와 같이 출력됩니다.

결과화면

```bash
이름을 입력하세요 : potato
당신의 이름은 potato 입니다.
```

위 결과화면에서 'potato' 는 사용자가 입력한 값입니다. 사용자가 입력한 값이 name 변수에 저장되어 출력된 것입니다.

### 연습문제1

이름과 전화번호를 입력받고 정보를 출력하는 프로그램을 아래 예제를 참고해서 작성해 보세요.

아래의 결과 화면과 같이 동작하는 exam2.py 를 직접 작성해 보세요.

결과 화면

```bash
이름을 입력하세요 : melon
전화번호를 입력하세요 : 010-2222-3333
melon님의 전화번호는 [010-2222-3333] 입니다.
```

정답

exam2.py

```python
name = input("이름을 입력하세요 : ")
phone_number = input("전화번호를 입력하세요 : ")
print(f"{name}님의 전화번호는 [{phone_number}] 입니다.")
```

### 연습문제2

생년월일을 입력받고 올해 나이가 몇살인지, 그리고 50세가 되는 해는 몇년인지를 출력하는 프로그램을 작성해 보세요.

아래 결과 화면과 같이 동작하는 exam3.py 를 직접 작성해 보세요.

```bash
생년월일을 입력하세요 : 2020
올해 당신의 나이는 1세 입니다.
50세가 되는 해는 2069년 입니다.
```

정답

exam3.py

```python
this_year = 2021
birth_year = input("생년월일을 입력하세요 : ")
birth_year_int = int(birth_year) # input() 함수는 항상 문자열을 반환하므로 'int' 형태로 형변환 필요
age = this_year - birth_year_int
print(f"올해 당신의 나이는 {age}세 입니다.")
print(f"50세가 되는 해는 {this_year + 49 - age}년 입니다.")
```
