# [Bronze II] Palindroom - 29835 

[문제 링크](https://www.acmicpc.net/problem/29835) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

그리디 알고리즘, 구현, 문자열

### 제출 일자

2024년 5월 1일 10:58:09

### 문제 설명

<p>Kevin sai informaatikaolümpiaadi eelvooru palindroomiülesande eest maksimumpunktid. Seda nähes andis õpetaja talle natuke raskema ülesande, milles uuritakse mitmesuguse pikkusega tekstilisi palindroome.</p>

<p>Sarnaselt arvujada juhtumiga nimetatakse teksti palindroomiks, kui see on sama eest tahapoole ja tagant ettepoole lugedes. Näiteks <code>ABBA</code> on palindroom (sest see on ka tagurpidi lugedes <code>ABBA</code>), aga <code>ABCD</code> ei ole (sest see on tagurpidi lugedes <code>DCBA</code>).</p>

<p>Kirjutada programm, mis leiab vähima võimaliku arvu täheasendustega viisi antud tekst palindroomiks muuta.</p>

### 입력 

 <p>Sisendi esimesel real on täisarv $N$ ($1 \le N \le 300$).</p>

<p>Teisel real on $N$ suurest ladina tähest (<code>A</code> $\ldots$ <code>Z</code>) koosnev tekst.</p>

### 출력 

 <p>Väljundi esimesele reale väljastada täisarv $K$, mis näitab, mitu tähte on minimaalselt vaja asendada, et sisendis antud tekstist saaks palindroom.</p>

<p>Teisele reale väljastada saadud palindroom. Kui minimaalse täheasenduste arvuga palindroome on mitu, väljastada neist (ladina tähestiku järgi) tähestikulises järjekorras esimene.</p>

