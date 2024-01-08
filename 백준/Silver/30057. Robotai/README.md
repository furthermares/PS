# [Silver IV] Robotai - 30057 

[문제 링크](https://www.acmicpc.net/problem/30057) 

### 성능 요약

메모리: 168592 KB, 시간: 644 ms

### 분류

브루트포스 알고리즘, 수학

### 제출 일자

2024년 1월 8일 13:46:56

### 문제 설명

<p>Iškasta tiesi $L$ ilgio vaga, kurioje reikia pasodinti $M$ medelių. Medelius sodins robotai, todėl visi atstumai vagoje matuojami <em>robopėdomis</em>.</p>

<p>Duota pozicijų (t. y. atstumų nuo vagos pradžios) seka $P_1, P_2, \dots , P_M$. Kiekvienoje šių pozicijų turi būti pasodintas vienas medelis.</p>

<p>Darbą turi atlikti $2$ robotai. Kiekvienas robotas per $1$ laiko vienetą nuvažiuoja $1$ robopėdą, o per $S$ laiko vienetų pasodina vieną medelį.</p>

<p>Per kiek mažiausiai laiko galima pasodinti visus medelius, jeigu dirbs abu robotai? Pirmojo roboto pradinė pozicija yra $0$, o antrojo – $L$. Abu robotai darbą pradeda tuo pačiu laiko momentu $0$.</p>

<p>Duotas medelių skaičius $M$, vagos ilgis $L$, bei laikas, per kurį robotas pasodina vieną medelį $S$. Taip pat duotas pozicijų, surikiuotų didėjimo tvarka, sąrašas $P_1, P_2, \dots , P_M$.</p>

<p>Parašykite programą, kuri apskaičiuotų trumpiausią sodinimo laiką T, per kurį robotai gali pasodinti visus medelius.</p>

### 입력 

 <p>Pirmojoje eilutėje pateikti trys sveikieji skaičiai: $M$ – pozicijų skaičius, $L$ – vagos ilgis, $S$ – vieno medelio sodinimo laikas.</p>

<p>Likusiose $M$ eilučių pateiktos medelių sodinimo pozicijos $P_1, P_2, \dots , P_M$ – po vieną sveikąjį skaičių kiekvienoje eilutėje.</p>

### 출력 

 <p>Pirmojoje (ir vienintelėje) eilutėje išveskite trumpiausią sodinimo laiką T.</p>

