##  <li>請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。</br>

###  用"vi ~/.bashrc"進入編輯模式，並輸入"HOSTS_PATH=/etc/hosts"這個變數。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-6/ACS107127/screen/1.png)</br></br>

###  輸入"source ~/.bashrc"使修改過的變數不用再次登入就生效。</br>
###  執行"cat $HOST_PATH"，來確認是否有寫入。
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-6/ACS107127/screen/2.png)</br></br>



##  <li>在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。</br></br>

###  用"vi/vim 檔名.c"新增一個檔案，並在內容輸入程式碼。
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-6/ACS107127/screen/3.png)</br></br>

###  1.執行"gcc 檔名.c"。(如果無法使用gcc則要先用yum groupinstall "Development Tools"安裝)</br>
###  2.輸入"ll 檔名.c a.out"。("a.out"為預設的執行檔)</br>
###  3.執行"a.out" 沒有讀到"HOSTS_PATH"。(因為該變數不在子程序當中)</br>
###  4.輸入"echo $?"，得到"1"。(因為程式無法成功執行(0代表成功執行))</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-6/ACS107127/screen/4.png)</br></br>

###  回到先前編輯的檔案，並新增"export HOSTS_PATH"。
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-6/ACS107127/screen/5.png)</br></br>

###  <strong>記得再輸入一次"source ~/.bashrc"<strong>。</br>
###  按照先前的步驟重複執行一次。</br>
###  執行"a.out"，讀到"HOSTS_PATH"。</br>
###  輸入"echo $?"，得到"0"(表示執行成功!!!)。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-6/ACS107127/screen/6.png)</br></br>

##  完成~





 
