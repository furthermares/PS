# [Gold III] Syntax Included - 4557 

[문제 링크](https://www.acmicpc.net/problem/4557) 

### 성능 요약

메모리: 34856 KB, 시간: 120 ms

### 분류

자료 구조, 파싱, 정규 표현식, 스택, 문자열

### 문제 설명

<p>You are writing your first website and seem to be making your fair share of simple HTML syntax errors. You have decided to write an HTML parser to help you determine if your HTML code is syntactically correct based on the following condensed HTML definition:</p>

<table class="table table-bordered table-center-60">
	<tbody>
		<tr>
			<td><b>HTML CODE</b></td>
			<td><HTML><i><b>BODY</b></i></HTML></td>
		</tr>
		<tr>
			<td><b>BODY</b></td>
			<td><BODY><i><b>TEXT</b></i></BODY></td>
		</tr>
		<tr>
			<td><b>TEXT</b></td>
			<td><i><b>STRING</b></i> | <i><b>STRING TEXT</b></i> | <i><b>TAG</b></i> | <i><b>TAG TEXT</b></i></td>
		</tr>
		<tr>
			<td><b>STRING</b></td>
			<td>possibly empty string of printable characters other than '<' and '>')</td>
		</tr>
		<tr>
			<td><b>TAG</b></td>
			<td><i><b>BOLD</b></i> | <i><b>ITALICS</b></i> | <i><b>LINK</b></i></td>
		</tr>
		<tr>
			<td><b>BOLD</b></td>
			<td><B><i><b>TEXT</b></i></B></td>
		</tr>
		<tr>
			<td><b>ITALICS</b></td>
			<td><I><i><b>TEXT</b></i></I></td>
		</tr>
		<tr>
			<td><b>LINK</b></td>
			<td><A HREF=<i><b>URL</b></i>><i><b>TEXT</b></i></A></td>
		</tr>
		<tr>
			<td><b>URL</b></td>
			<td>http://<i><b>STRING</b></i>.com</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>The first line contains a single integer <i>n</i> indicating the number of data sets.</p>

<p>The following <i>n</i> lines each represent a data set and consists of up to 1000 characters. Spaces can be contained anywhere within the data set.</p>

<p>Note that all tags are case sensitive.</p>

### 출력 

 <p>If the code is syntactically correct, the following string will be printed:</p>

<p>"Syntax Included"</p>

<p>Otherwise the following string will be printed:</p>

<p>"No Syntax Included"</p>

