# 변수와 자료형

## 변수

변수란 python 에서 어떠한 데이터를 임시로 저장하기 위해 사용하는 그릇 입니다. 변수는 아래와 같은 형식으로 생성할 수 있습니다.

```python
변수명 = 값
```

왼쪽에는 변수 이름을 쓴 다음 '=' 기호를 넣고 해당 변수에 저장할 값을 오른쪽에 적습니다.

그러면 실제 코드를 한번 살펴 보겠습니다. 아래와 같이 python 코드를 작성해 보세요.

```python
age = 10
name = "potato"
```

위 코드에서 'age' 와 'name' 은 변수 이름 입니다. python 인터프리터가 위 코드를 실행하면 컴퓨터의 메모리 어딘가에 10 이라는 숫자값과 "potato" 라는 문자열을 저장합니다.

변수를 어떤 데이터를 담는 그릇이라고 생각하면 이해하기 편합니다. 각 그릇에 이름을 정할 수 있고 각각의 그릇에 담긴 변수는 나중에 꺼내 사용할 수 있습니다. 아래와 같이 코드를 작성해 보세요.

```python
>>> name = "potato"
>>> print("제 이름은 %s 입니다." % name)
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

변수 이름은 여러분 마음대로 정할 수 있지만 아래와 같은 약간의 제약사항이 있습니다.

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

'-'(hyphen) 은 python 이 뺄셈 연산자로 인식하기 때문에 변수이름에 들어갈 수 없습니다.

```python
>>> myage! = 10
  File "<stdin>", line 1
    myage! = 10
         ^
SyntaxError: invalid syntax
```

'myage!' 는 느낌표 특수문자 부분에서 SyntaxError 가 발생한 것을 알 수 있습니다.

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
myname = "tomato"
>>> print(yourname)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'yourname' is not defined
```

위 오류는 프로그램 어디에서도 'yourname' 이라는 변수에 값을 설정한 적이 없는데 가져다 쓰려고 했기 때문에 NameError 가 발생 했습니다. 변수는 어떤 값을 가질때에만 유효합니다.

만약 NameError 가 발생 했다면 변수 이름에 오타가 없는지 확인해 보세요 😅

## 숫자

## 문자열

## bool

```python
True
```
