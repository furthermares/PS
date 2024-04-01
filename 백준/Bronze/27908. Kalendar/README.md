# [Bronze II] Kalendar - 27908 

[문제 링크](https://www.acmicpc.net/problem/27908) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

구현, 문자열

### 제출 일자

2024년 4월 1일 12:33:41

### 문제 설명

<p>Magdalena likes calendars, and she makes her own calendar for each month.</p>

<p>Each day of the month is represented with exactly three characters:</p>

<ul>
	<li>If the day number is single-digit, then it is represented as '<code>..X</code>'. For example, the number $7$ is represented as '<code>..7</code>'</li>
	<li>If the day number is double-digit, then it is represented as '<code>.XY</code>'. For example, the number $17$ is represented as '<code>.17</code>'.</li>
</ul>

<p>Each row of the calendar represents a week, and each week consists of $7$ days. If the week doesn’t have all the $7$ days (because the month doesn’t start on Monday, or it doesn’t end on Sunday), then the missing days are replaced with '<code>...</code>'.</p>

<p>Magdalena also wants her calendar to be pretty. She will decorate it in the following way: she will fill the upper and lower sides with '<code>-</code>' (ASCII 45), the left and right sides with '<code>|</code>' (ASCII 124), and the corners with '<code>+</code>' (ASCII 43).</p>

<p>For example, the format of Magdalena’s calendar, when the month has 31 days and starts on Wednesday, is the following:</p>

<pre style="text-align: center;">+–––––––––––––––––––––+
|........1..2..3..4..5|
|..6..7..8..9.10.11.12|
|.13.14.15.16.17.18.19|
|.20.21.22.23.24.25.26|
|.27.28.29.30.31......|
+–––––––––––––––––––––+</pre>

<p>Your task is to determine the format of Magdalena’s calendar if it has $n$ days, and the first day of the month is the $x$-th day of the week. For example, if $x = 1$, the month starts on Monday, and if $x = 5$, it starts on Friday.</p>

<p>Note: We assume the first day of the week is Monday.</p>

### 입력 

 <p>The first and only line contains integers $n$ and $d$ ($1 ≤ n ≤ 99$, $1 ≤ d ≤ 7$), the number of days in the month, and the day it starts with.</p>

### 출력 

 <p>Print Magdalena’s calendar.</p>

