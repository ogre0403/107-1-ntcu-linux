### 1.關於連結檔案的建置行為:<br>
------------------------------------
### 在 /etc/hosts 檔案，請找出<br>
###  <li>該檔案的 inode 號碼為幾號？ <br>
###  <li>這個 inode 共有幾個檔名在使用？<br>
<br>
在" ls -al "的後面加上參數" i "就可以查看檔名的inode號碼，以及該inode共有幾個檔名在使用。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-5/ACS107135/photo/1.PNG)<br>

*****

### 建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出<br>
###  <li>srv/hosts.hard的 inode 號碼為幾號？<br>
###  <li>這個 inode 共有幾個檔名在使用？<br>
###  <li>說明原因。<br>
<br>
說明: 用指令"ln"來建立實體連結(這裡會先發現一般使用者會產生權限不足的問題，所以必須先把使用者切換為root再來進行)，然後用"ls -ali"觀察該inode號碼和其連結數。就會發現" /srv/hosts.hard的 inode 號碼 "和" /etc/hosts 的 inode 號碼 "同樣皆為" 4212682 "(兩者為同一檔案，只是檔名不同)，該inode號碼的連結數也從1改變為" 2 "。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-5/ACS107135/photo/2.PNG)<br>

*****

### 建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出<br>
###  <li>/srv/hosts.soft的 inode 號碼為幾號？<br>
###  <li>這個 inode 共有幾個檔名在使用<br>
###  <li>說明原因<br>
<br>
#### 用 ln -s 指令來建立符號連結(Symbolic Link)<br>
"-s"為建立符號連結(Symbolic Link)的參數。
<br>
可以得知:<br>
1.inode 號碼為" 12944883 "<br>
2.該inode只有1個檔名正在使用。<br>
<br>
說明: Symbolic Link 與 Hard Link 兩者不同。<br>
" Hard Link "是把一個檔案新增出一個不同的檔名，但是這2個不同的檔名所開啟的是同一個檔案，所以他們的inode會是相同的(為同一檔案)。<br>
" Symbolic Link "是建立一個新檔案做為另一個檔案開啟的捷徑，2者為不同的檔案，所以自然inode就不會相同(為不同檔案)。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-5/ACS107135/photo/3.PNG)<br>
