# [Silver V] Maksimaalne tõus - 29970 

[문제 링크](https://www.acmicpc.net/problem/29970) 

### 성능 요약

메모리: 32576 KB, 시간: 76 ms

### 분류

구현

### 제출 일자

2023년 12월 31일 14:29:38

### 문제 설명

<p>Nii suusa- kui jooksu- kui rattamaratonide üks tähtsamaid iseloomustajaid on raja kõrgusprofiil ja eriti selle maksimaalne tõus.</p>

<p>Raja kõrgusprofiil annab $N$ rajapunkti kõrgused $H_1$, $H_2$, $\dots$, $H_N$. Tõusuks nimetatakse sellist järjestikuste punktide jada, kus iga järgmine punkt on eelmisest rangelt kõrgemal. Tõusu kõrguseks nimetatakse selle alguse ja lõpu kõrguste vahet.</p>

<p>Kirjutada programm, mis leiab antud rajaprofiilis maksimaalse tõusu kõrguse.</p>

### 입력 

 <p>Tekstifaili esimesel real on rajaprofiili punktide arv $N$ ($1 \le N \le 50\,000$) ja järgmisel $N$ real punktide täisarvulised kõrgused $H_i$ ($0 \le H_i \le 1\,000\,000$) järjestatuna stardist finiši suunas.</p>

### 출력 

 <p>Tekstifaili ainsale reale väljastada üks täisarv: maksimaalne tõusu kõrgus sisendis antud rajaprofiilis, see tähendab maksimaalne kõrguste vahe $H_i - H_j$, kus $j \le i$ ja $H_j < H_{j+1} < \dots < H_{i-1} < H_i$. Kui rajal pole ühtki tõusu (haha :), siis väljastada vastusena 0.</p>

