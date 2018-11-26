### 請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。
* 輸入`vi ~/.bashrc`
> 進入 .bashrc 進行編輯
* 輸入`HOSTS_PATH=/etc/hosts`
> 新增變數 

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-6/ACS107144/6-1-1.png)

* 輸入`echo $HOSTS_PATH`
> 確認有新增到 HOSTS_PATH                   
* 輸入`source .bashrc`
> 讀取檔案內容
* 輸入`cat $HOSTS_PATH`
> 驗證有讀取到檔案內容

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-6/ACS107144/6-1-2.png)


## 在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。

* 輸入`vim test.c`
> 新增一個名為 test.c 的檔案，編輯其內容

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-6/ACS107144/6-2-1.png)

### 在Linux裡編譯此範例程式並執行
* 輸入`gcc test.c`
> 編譯 test.c
* 輸入`./a.out`
> 輸出test.c的結果
* 輸入`echo $?`
> 印出?的內容

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-6/ACS107144/6-2-2.png)

### 請問否有讀到HOSTS_PATH以及$?的值為何，請說明。
* 沒有讀到 HOSTS_PATH 的值
> `getenv() return NULL`
* $?的值為1 (有誤)

### 在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。
* 輸入`vi ~/.bashrc`
> 進入 .bashrc 進行編輯
* 輸入`export HOSTS_PATH=/etc/hosts`
> 在之前輸入之變數前加上export 

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-6/ACS107144/6-3-1.png)

* 輸入`source .bashrc`
> 讀取剛剛修改過的檔案內容
* 輸入`gcc test.c`
> 編譯 test.c
* 輸入`./a.out`
> 輸出test.c的結果
* 輸入`echo $?`
> 印出?的內容

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-6/ACS107144/6-3-2.png)

### 請問否有讀到HOSTS_PATH以及$?的值為何?
* 有讀到 HOSTS_PATH 的值
* $?的值為0 (正確)
