### 1.請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。<br>
在.bashrc裡新增變數HOSTS_PATH=/etc/hosts<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-6/ACS107135/photo/1.PNG)<br>
使用source .bashrc 就可以馬上讀取剛新增的變數，而不用重新登入。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-6/ACS107135/photo/2.PNG)<br>
### 2.在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。<br>
依照題意新建一個C檔案。(程式碼如下)<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-6/ACS107135/photo/3.PNG)<br>
編譯並執行，但讀取 HOSTS_PATH 失敗，回傳值為1。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-6/ACS107135/photo/4.PNG)<br>
若想要讓 HOST_PATH 也在子程序被讀取，則需先以 export 宣告變數。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-6/ACS107135/photo/5.PNG)<br>
成功讀取HOST_PATH變數，回傳值為0。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-6/ACS107135/photo/6.PNG)<br>
