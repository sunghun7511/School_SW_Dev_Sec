# SW Development Secuirty Day 007 Class of python

## 클래스가 무엇인가

### 클래스는 일종의 템플릿이다.

* C언어의 구조체와 유사하다
* 차이점은 구조체는 변수만 담을 수 있지만, 클래스는 함수까지 담을 수 있다.
* 즉, 클래스 = 변수 U 함수

### 형식

```python
class ClassName():
    varname = value
    def functionName(self, args...., ...):
        val = value
```

### self

클래스의 변수에 접근하기 위해 파이썬이 제공하는 변수

클래스 내에서 함수를 정의할 때 잊지 말고 꼭 쓰자

### 생성자

클래스 변수가 생성될 때 자동으로 호출되는 함수

클래스 내부에 정의된 변수 등을 초기화 할 때 사용
