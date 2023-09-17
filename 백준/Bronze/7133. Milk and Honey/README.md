# [Bronze II] Milk and Honey - 7133

[문제 링크](https://www.acmicpc.net/problem/7133) 

### 성능 요약

메모리: 31256 KB, 시간: 56 ms

### 분류

\-

### 문제 설명

<p>In the country of milk and honey, Juku is in charge of cows and bees. Since bees will sting cows and make them unhappy and cows will eat all the flowers bees use to make honey, cows and bees need to be kept on separate fields. Each field can support a limited number of animals. Cows and bees are free to obtain, so as many will be put on any field as can be supported there.

Each cow produces one unit of milk and each bee produces one unit of honey. Milk and honey produce different levels of happiness when consumed. Additionally, customers place higher value on "rare" goods. So, when the first unit of milk from a given field produces $M$ units of happiness, the second one only produces $M - D_M$ units, the third one $M - 2 \cdot D_M$, and so on (though the values never go below zero). Similar pattern also holds for the value of honey.

Juku's task is to choose how to place cows and bees in the milk and honey land to maximize happiness. Juku needs your help to do this since the calculations are too many to be done on a piece of paper.</p>

### 입력 

<p>The first line of the text file contains two integers: $M$ ($0 \le M \le 1000$), the amount of happiness of first unit of milk, and $D_M$ ($0 \le D_M \le M$), the incremental decrease of happiness value for each following unit of milk produced on one field. The second line contains two integers: $H$ and $D_H$ ($0 \le D_H \le H \le 1000$), giving the same information for honey.

The third line contains $N$ ($1 \le N \le 1000$), the number of fields. The following $N$ lines describe the fields. Each line contains $C$ ($0 \le C \le 100$) and $B$ ($0 \le B \le 100$), the the number of cows and the number bees the fields can support.</p>

### 출력 

<p>The only line of output should contain a single number, the maximum amount of happiness achievable.</p>
