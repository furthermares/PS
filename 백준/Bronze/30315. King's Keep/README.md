# [Bronze II] King's Keep - 30315 

[문제 링크](https://www.acmicpc.net/problem/30315) 

### 성능 요약

메모리: 33376 KB, 시간: 356 ms

### 분류

브루트포스 알고리즘, 기하학, 수학

### 문제 설명

<p>King Carl's kingdom contains $k$ keeps (commonly called castles).</p>

<p>Coordinates of keeps are known, and King Carl considers himself convinced that it could be convenient to choose a central keep as King Carl's residence.</p>

<p>Critically, King Carl considers that the average cost to carry commands from King Carl's residence to King Carl's other keeps should be small.</p>

<p>Compute the minimal average Euclidean distance<sup>1</sup> from his residence keep to the other keeps if King Carl chooses his residence optimally.</p>

<hr>
<p><sup>1</sup>The Euclidean distance between two points is the length of a straight line segment between these points.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with an integer $k$ ($2\leq k\leq 1000$), the number of keeps.</li>
	<li>$k$ lines, each with two integers $x$ and $y$ ($|x|, |y| \leq 1000$), the coordinates of the keeps.</li>
</ul>

<p>It is guaranteed that all keeps are at distinct locations.</p>

### 출력 

 <p>Output the minimal possible average distance from the keep that is chosen as the king's residence to all other keeps.</p>

<p>Your answer should have an absolute or relative error of at most $10^{-6}$.</p>

