## 在 /etc/hosts 檔案，請找出<br>
### 1.該檔案的 inode 號碼為幾號？<br>
#### Ans:2107882<br>
### 2.這個 inode 共有幾個檔名在使用？<br>
#### Ans:1<br>
用"ls -ali (檔名)"來觀察inode碼與link數<br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-5/ACS107137/img/1-1.png?raw=true)<br><br>

## 建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出<br>
### 1./srv/hosts.hard的 inode 號碼為幾號？<br>
#### Ans:2107882<br>
### 2.這個 inode 共有幾個檔名在使用？<br>
#### Ans:2<br>
用"ln"建立實體連結，並用"ll -i"觀察inode碼與link數(因為檔案權限的關係，記得切換為root)<br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-5/ACS107137/img/1-2.png?raw=true)<br>
### 3.說明原因<br>
#### 實體連結(hard link)是在某個目錄下新增一個該檔案的關連資料而已，兩個檔名連結到同一個inode碼，所以檔案連結數為2<br>
#### 另外，不論使用哪一個檔名來編輯，結果都是相同的喔!<br><br>

## 建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出<br>
### 1./srv/hosts.soft的 inode 號碼為幾號？<br>
#### Ans:6709889<br>
### 2.這個 inode 共有幾個檔名在使用？<br>
#### Ans:1<br>
用"ln -s"建立符號連結，並用"ll -i"觀察inode碼與link數<br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-5/ACS107137/img/1-3.png?raw=true)<br>
### 3.說明原因<br>
#### 符號連結(soft link)是建立一個獨立的檔案，而這個檔案會讓資料的讀取指向他 link 的那個檔案內容<br>
#### 因為是新的獨立檔案，所以會有一個新的inode碼，檔案連結數為1<br>
