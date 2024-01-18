# [Silver V] Monkeying Around - 29901 

[문제 링크](https://www.acmicpc.net/problem/29901) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 1월 18일 14:08:06

### 문제 설명

<p>$N$ baby monkeys are playing in treetops. They all start from the same height, and each of them finishes where it started from. Each monkey makes $M$ jumps, denoted by integers that show how many centimeters higher or lower the monkey moved with that jump. For each monkey, the height of one of the jumps in unknown and represented as zero in the input data. Find the monkey who was on the highest level on average (assuming the jumps take place after equal time intervals).</p>

### 입력 

 <p>The first line contains $N$ ($1 \le N \le 100$), the number of monkeys, and $M$ ($1 \le M \le 100$), the number of jumps. Each of the following $N$ lines contains $M$ space-separated integers $A_i$ ($-200 \le A_i \le 200$) showing how many centimeters higher the corresponding monkey moved with the corresponding jump (negative values indicate moving lower). There is exactly one $0$ on each line, indicating that we do not know how much higher or lower the monkey moved with that jump.</p>

### 출력 

 <p>Output exactly one integer, the index of the monkey who was on the highest level on average. The monkeys are indexed $1, \ldots, N$ in the order in which their data are given in the input. When computing the average, the common final height after the last jump is included, but the initial height before the first jump is excluded. If there are several monkeys with the maximal average level, output the index of any of them.</p>

