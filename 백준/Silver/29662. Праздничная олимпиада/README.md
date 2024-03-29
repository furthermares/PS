# [Silver II] Праздничная олимпиада - 29662 

[문제 링크](https://www.acmicpc.net/problem/29662) 

### 성능 요약

메모리: 37336 KB, 시간: 76 ms

### 분류

자료 구조, 그리디 알고리즘, 우선순위 큐, 정렬

### 제출 일자

2024년 1월 20일 12:31:46

### 문제 설명

<p>У мальчика Вити скоро день рождения, который он хочет провести с друзьями. Какой же праздник без праздничной олимпиады? Для своих друзей Витя подготовил олимпиаду по программированию.</p>

<p>Когда все гости собрались, именинник распределил их по $m$ командам. Витя очень старался сбалансировать силы команд, и у него это получилось. Каждую из предложенных $n$ задач олимпиады любая команда решает ровно за $a_i$ минут и всегда с первой попытки. Ребята не любят распыляться, поэтому если команда берется писать задачу $i$, то все ее участники непрерывно решают задачу в течении $a_i$ минут. При этом команда может начинать решать следующую задачу сразу после того, как решила предыдущую.</p>

<p>Однако, Витя не хотел поссорить своих друзей, поэтому исключил элемент борьбы между командами --- команды не соперничают, а помогают друг другу. Целью команд на олимпиаде является решение всех задач. Таким образом каждую задачу решает только одна команда. При этом друзьям засчитывается штрафное время, равное числу минут, прошедших от начала олимпиады до момента сдачи задачи. Единственная цель, которую преследуют друзья --- сдать все задачи с наименьшим суммарным штрафным временем.</p>

<p>Например, пусть участвуют две команды, которым предложено в олимпиаде три задачи с временами решения 5, 10 и 15 минут. Пусть первая команда решает сначала вторую, а потом первую задачу. Таким образом за решение второй задачи друзья получат 10 штрафных минут, а за решение первой 15. Вторая команда с начала олимпиады решает только третью задачу, за которую друзья получат 15 штрафных минут. В сумме друзья Вити получат 40 штрафных минут.</p>

<p>В то время, когда друзья будут решать задачи, Витя будет управлять порядком, в котором команды будут их решать. Помогите Вите --- напишите программу, которая вычислит наименьшее суммарное штрафное время, требуемое для сдачи всех задач.</p>

### 입력 

 <p>В первой строке входного файла содержатся два числа $n$ и $m$ --- число задач и команд, соответственно ($0 \le n \le 50000$, $1 \le m \le 10000$). Во второй строке содержится $n$ целых чисел $a_i$ --- количество времени, необходимое для решения задачи $i$ любой из команд ($0 \le a_i \le 30$).</p>

### 출력 

 <p>Выведите в выходной файл наименьшее суммарное штрафное время, которое могут получить друзья Вити за решение всех задач.</p>

