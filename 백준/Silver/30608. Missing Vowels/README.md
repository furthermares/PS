# [Silver IV] Missing Vowels - 30608 

[문제 링크](https://www.acmicpc.net/problem/30608) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

그리디 알고리즘, 문자열

### 제출 일자

2023년 11월 30일 13:28:51

### 문제 설명

<p>There are many ways to write a word on paper. For example, some writing systems, like Arabic and Hebrew, omit most vowels, although they write some of them.</p>

<p>In this problem, we will only consider strings consisting of English letters and hyphens. Letters '<code>a</code>', '<code>e</code>', '<code>i</code>', '<code>o</code>', '<code>u</code>', and '<code>y</code>' are considered to be vowels, while hyphens and all other letters are considered to be consonants. All comparisons are case-insensitive: uppercase and lowercase versions of the same letter are considered equal.</p>

<p>You are given two strings $s$ and $f$, called the <em>short</em> name and the <em>full</em> name, respectively. Your task is to check whether the short name $s$ can be obtained from the full name $f$ by omitting some vowels (possibly none).</p>

### 입력 

 <p>The first line contains a single string $s$, denoting the short name.</p>

<p>The second line contains a single string $f$, denoting the full name.</p>

<p>Each string is non-empty and consists of at most $1000$ English letters and hyphens.</p>

### 출력 

 <p>Print "<code>Same</code>" if the short name $s$ can be obtained from the long name $f$ by omitting some vowels, and "<code>Different</code>" otherwise.</p>

