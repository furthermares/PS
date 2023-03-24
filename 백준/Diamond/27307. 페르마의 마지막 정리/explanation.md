# 27307. 페르마의 마지막 정리

(이 문제는 [에디토리얼](https://upload.acmicpc.net/f44e8e2c-c01a-4472-9536-370b41bd2b4a/)이 있습니다. 67쪽입니다.)

**이 문제는 Lifting-The-Exponent Lemma 문제로, 그 식 구현과 Pollard Rho 소인수분해만 하면 끝납니다.**


## 문제 요약

z는 |x|,|y|와 서로소이지만 |x+y|와는 아님. 그 z중에서 |x<sup>n</sup>+y<sup>n</sup>|이 z<sup>m</sup>의 배수일 때는? (n은 홀수)


## 풀이

LTE lemma에 따르면 식 하나로 표현된다. 그렇게 해서 소인수분해 한 식에서 z<sup>m</sup>이 몇 번 들어갈 수 있나 보자.


### 1. 소인수분해: |x<sup>n</sup>+y<sup>n</sup>|를 z<sup>m</sup> · k = p<sub>t</sub><sup>e<sub>t</sub>m</sup> · k 형태로 나타내기.

식을 z<sup>m</sup>을 사용하는 꼴로 나타내자.

1. |x+y| 소인수분해: ℙ(|x+y|)

  z는 x,y 와는 서로소이다. 소인수분해 해서 빼주자.

2. X 소인수분해: ℙ(X). (X = |x|)

3. Y 소인수분해: ℙ(Y). (Y = |y|)

4. (1)에서 (2)와 (3) 뺴기. ℙ = ℙ(|x+y|) - ℙ(X) - ℙ(Y)

5. 중복 요소 제거 → 모두 e<sup>t</sup>로 처리됨.

6. (X, Y 대소관계 무상관.)

z 소인수분해 꼴이 z = p<sub>1</sub><sup>e<sub>1</sub></sup> p<sub>2</sub><sup>e<sub>2</sub></sup> ··· p<sub>t</sub><sup>e<sub>t</sub></sup> 

m 제곱하면 z<sup>m</sup> = p<sub>1</sub><sup>e<sub>1</sub>m</sup> p<sub>2</sub><sup>e<sub>2</sub>m</sup> ··· p<sub>t</sub><sup>e<sub>t</sub>m</sup>

|x<sup>n</sup>+y<sup>n</sup>|이 z<sup>m</sup>의 배수일 때를 찾는 것이니...

|x<sup>n</sup>+y<sup>n</sup>| = z<sup>m</sup> · k = p<sub>1</sub><sup>e<sub>1</sub>m</sup> p<sub>2</sub><sup>e<sub>2</sub>m</sup> ··· p<sub>t</sub><sup>e<sub>t</sub>m</sup> · k

여기서 k는 z<sup>m</sup>에 x,y 와의 서로소 조건으로 잘린 소인수와 m제곱 때문에 작아서 못들어가는 찌꺼기.

### 2. [Lifting-The-Exponent Lemma](https://brilliant.org/wiki/lifting-the-exponent/): |x<sup>n</sup>+y<sup>n</sup>|을 p<sub>t</sub><sup>f<sub>t</sub></sup> · l 형태로 나타내기.

이제 식을 LTE로 제대로 소인수분해 해보자.

𝜈<sub>p</sub>(n) = (n에 p가 몇제곱 있나). 𝜈<sub>2</sub>(12) = 𝜈<sub>2</sub>(2<sup>2</sup>3<sup>1</sup>) = 2, 𝜈<sub>3</sub>(12) = 𝜈<sub>3</sub>(2<sup>2</sup>3<sup>1</sup>) = 1

LTE: 이 문제에서와 같이 n이 홀수이고 p|(x+y) 이면, 𝜈<sub>p</sub>(x<sup>n</sup>+y<sup>n</sup>) = 𝜈<sub>p</sub>(x + y) + 𝜈<sub>p</sub>(n) 이 성립합니다.

1. 케이스 1: xy ≥ 1 (부호가 같을 때)

   f<sub>i</sub> = 𝜈<sub>p<sub>i</sub></sub>(|X<sup>n</sup>+Y<sup>n</sup>|) = 𝜈<sub>p<sub>i</sub></sub>(X<sup>n</sup>+Y<sup>n</sup>) = 𝜈<sub>p<sub>i</sub></sub>(X + Y) + 𝜈<sub>p<sub>i</sub></sub>(n)

2. 케이스 2: xy ≤ 1 (부호가 다를 때)

   f<sub>i</sub> = 𝜈<sub>p<sub>i</sub></sub>(|X<sup>n</sup>+Y<sup>n</sup>|) = 𝜈<sub>p<sub>i</sub></sub>(X<sup>n</sup>-Y<sup>n</sup>) = 𝜈<sub>p<sub>i</sub></sub>(X - Y) + 𝜈<sub>p<sub>i</sub></sub>(n)

3. "사실 생각해보면 굳이 경우를 나눌 필요가 없긴 하다." (p = 2 일때도 그렇다고 함)

   두 경우 다: 𝜈<sub>p<sub>i</sub></sub>(x + y) + 𝜈<sub>p<sub>i</sub></sub>(n) 이다. 이렇게 처리. (x = x, X = |x|)

지금 구한게 |X<sup>n</sup>+Y<sup>n</sup>|에 소인수 p가 몇제곱이나 있는가를 LTE로 구한 것.

|x<sup>n</sup>+y<sup>n</sup>| = p<sub>1</sub><sup>f<sub>1</sub></sup> p<sub>2</sub><sup>f<sub>2</sub></sup> ··· p<sub>t</sub><sup>f<sub>t</sub></sup> · l

여기서 l은 모든 p와 서로소이며 찌꺼기 없이 소인수분해 됐다.

### 3. 그래서 얻은 게 |x<sup>n</sup>+y<sup>n</sup>| = z<sup>m</sup> · k = p<sub>1</sub><sup>e<sub>1</sub>m</sup> p<sub>2</sub><sup>e<sub>2</sub>m</sup> ··· p<sub>t</sub><sup>e<sub>t</sub>m</sup> · k = p<sub>1</sub><sup>f<sub>1</sub></sup> p<sub>2</sub><sup>f<sub>2</sub></sup> ··· p<sub>t</sub><sup>f<sub>t</sub></sup> · l

문제가 요구하는 것은 이렇게 정리된다: p<sub>t</sub><sup>f<sub>t</sub></sup> 안에 꾸겨 넣을 수 있는 p<sub>t</sub><sup>e<sub>t</sub>m</sup>수는?

2<sup>4</sup>3<sup>2</sup> 안에 2<sup>2</sup>3<sup>1</sup>가 몇 번 들어가나? m=1일 때 2<sup>2</sup>를 한 번씩 넣어준다. 그러면 2 두번, 3 한번. 그러니 개수가 (1+2)(1+1) = 6 개. 합은 그 밑(base)에 따라서 계산.

m=2이면 두 개를 한꺼번에 넣는 것. 2 한번 밖에 안들어간다.

2가 몇 번 들어가는지를 g로 두자.

 1. g<sub>i</sub> = f<sub>i</sub>//m (e<sub>i</sub>의 값 자체는 답을 구하는데 필요 없다.)

 2. 개수 세기와 합은 수식대로 계산.

### 4. 출력. 끝.

## 비고

- 𝜈(1)=0 처리
  - |x+y| = 1, 즉 ℙ = {0} 이면 그 안에 들어갈 수 있는 z<sup>m</sup>는 1 밖에 없다. → print(1,1); exit(0);
  - 그렇지만 따로 처리 없어도 빈 리스트로 놔두면 iterate 되지 않고 초깃값인 1,1로 출력되어 상관없다.
- mod 처리된 식을 빼고 나눌 때 핸들링
  - mod 처리된 값을 추가로 연산할 때 빼거나 나눌 때 주의해야 하는 게 음수가 되거나 0이 될 수 있다는 점이다.
  - 이 케이스에서는 나눠야 하는데 이를 -1제곱으로 곱셈으로 바꿔서 처리하는 게 좋다.
    - (본인은 꼼수로 단순히 MOD 값을 충분히 높였다. 계산에 사용되는 값이 그거보다 훨씬 높은지라 3제곱도 역부족이다.)
