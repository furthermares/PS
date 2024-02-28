# [Bronze I] Koncertas - 30064 

[문제 링크](https://www.acmicpc.net/problem/30064) 

### 성능 요약

메모리: 42036 KB, 시간: 84 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 2월 28일 12:08:37

### 문제 설명

<p>Muzikos mylėtojai renkasi į koncertą. Iš viso koncertų salėje yra $N$ sėdimų vietų ir jos visos išpirktos. Kiekvienas klausytojas turi po bilietą su pažymėta vieta. Laikysime, kad klausytojo numeris yra $X$, jeigu jis turi bilietą su pažymėta vieta $X$. Taigi pirmasis klausytojas turėtų sėdėti vietoje $1$, antrasis – vietoje $2$, ir taip toliau.</p>

<p>Tačiau atėję į koncertų salę klausytojai susėdo nežiūrėdami į paskirtas vietas.</p>

<p>Paskutinysis vėluodamas atbėgo pats didžiausias muzikos mylėtojas nr. $1$, kuris turėjo sėdėti vietoje $1$. Kadangi tai pati geriausia vieta, jeigu ji bus užimta, jis paprašys ten sėdinčio klausytojo ją atlaisvinti. Tokiu atveju, šis klausytojas susigėdęs eis į sau paskirtą vietą (klausytojas $X$ eis į vietą $X$), o jeigu ji bus užimta – paprašys ją atlaisvinti. Šitaip persėdimas tęsis tol, kol galų gale visi klausytojai vėl susės.</p>

<p>Jums žinoma, kur yra atsisėdęs kiekvienas muzikos mylėtojas bei kuri viena vieta yra laisva prieš pasirodant klausytojui nr. $14, Raskite, kiek iš viso klausytojų turės persėsti.</p>

### 입력 

 <p>Pirmoje eilutėje įrašytas skaičius $N$. Antroje eilutėje įrašyta $N$ skaičių, atskirtų tarpais: tai numeriai klausytojų atsisėdusių vietose $1, 2, \dots , N$. Lygiai vienas iš šių skaičių bus lygus $0$, kuris žymi jog ši viena vieta yra laisva.</p>

### 출력 

 <p>Išveskite vieną skaičių – kiek klausytojų iš viso turės persėsti, klausytojui nr. $1$ pareikalavus savo vietos.</p>

