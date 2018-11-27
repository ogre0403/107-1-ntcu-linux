## HW6

### 1.請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts。
+ 輸入指令。
##### vim ~/.bashrc
+ 進入編輯模式。
+ 加入變數。
##### HOSTS_PATH="/etc/hosts"
+ 離開編輯模式。

### 2.如何不登出讓HOSTS_PATH變數生效?
##### source ~/.bashrc

### 3.執行cat $HOST_PATH確認有讀取到檔案內容。
+ 輸入指令。
##### cat $HOSTS_PATH

### 4.在Linux裡編譯此範例程式並執行。
+ 安裝GCC
##### yum groupinstall "Development Tools"
+ 寫程式
##### vim test.c 
![GITHUB]( https://imgur.com/fjgPUUp.jpg"git圖示")
##### gcc. test.c
##### ll test.c a.out

### 5.請問否有讀到HOSTS_PATH以及$?的值為何，請說明。
+ 否，因為變數不在子程序裡
+ $ ? = 1

### 6.在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示?
+ 修改
##### vim ~/.bashrc
+ 使用export
##### export HOSTS_PATH="/etc/hosts"
+ 使變數生效
##### source ~/.bashrc
+ 用GCC執行
##### gcc.test.c
+ 檢查
##### ll cp.c a.out
##### ./a.out
+ 如果$?=0即表示程式執行成功。
