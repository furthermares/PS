# [Silver III] Dividing apples - 29911 

[문제 링크](https://www.acmicpc.net/problem/29911) 

### 성능 요약

메모리: 78928 KB, 시간: 760 ms

### 분류

누적 합

### 제출 일자

2024년 1월 16일 16:17:30

### 문제 설명

<p>$N$ baskets are lined up, numbered $1 \ldots N$ from left to right. The basket number $i$ contains $K_i$ apples. John and Mary want to draw a line between two baskets, and then John would get all the baskets to the left of the line and Mary all the baskets to the right of the line. Help them draw the line to divide the apples as equally as possible!</p>

### 입력 

 <p>The first line of input contains $N$, the number of baskets ($2 \le N \le 1\,000\,000$). Each of the following $N$ lines contains an integer $K_i$: the number of apples in basket number $i$ ($1 \le i \le N$, $0 \le K_i \le 10\,000$).</p>

### 출력 

 <p>The only line of output should contain a single integer: the number of the basket to the right of which the line should be drawn, so that the absolute value of the difference between the number of apples John gets, and the number of apples Mary gets, would be as small as possible. If there are multiple possible answers, output any one of them.</p>

