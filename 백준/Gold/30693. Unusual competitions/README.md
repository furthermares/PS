# [Gold IV] Unusual competitions - 30693 

[문제 링크](https://www.acmicpc.net/problem/30693) 

### 성능 요약

메모리: 33076 KB, 시간: 288 ms

### 분류

그리디 알고리즘

### 제출 일자

2023년 11월 25일 14:21:52

### 문제 설명

<p>The teacher gave Dmitry's class a very strange task --- she asked every student to come up with a sequence of arbitrary length, consisting only of opening and closing brackets. After that all the students took turns naming the sequences they had invented. When the Dima's turn come, he suddenly realized that all his classmates got the right bracketed sequence, and whether he got the right bracketed sequence, he did not know.</p>

<p>Dima suspects now that he simply missed the word "right" in the task statement, so now he wants to save the situation by modifying his sequence slightly. More precisely, he can arbitrary amount of times (possibly zero) perform the <em>reorder</em> operation. The reorder operation consists of choosing an arbitrary subsegment of the sequence and then reordering all the characters in it in an arbitrary way. Such operation takes $l$ nanoseconds, where $l$ is the length of the subsegment being reordered. It's easy to see that reorder operation doesn't affect the number of opening and closing brackets doesn't change.</p>

<p>Since Dima will soon have to answer, he wants to make his sequence right as fast as possible. Help him to do this, or determine that it's impossible.</p>

### 입력 

 <p>The first line contains a single integer $n$ ($1 \le n \le 10^6$) --- the length of Dima's sequence.</p>

<p>The second line contains string of length $n$, consisting of characters "<code>(</code>" and "<code>)</code>" only.</p>

### 출력 

 <p>Print a single integer --- the minimum number of nanoseconds to make the sequence right or "<code>-1</code>" if it is impossible to do so.</p>

