請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-6/ADT105136/001.PNG)
![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-6/ADT105136/002.PNG)

在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-6/ADT105136/003.PNG)
![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-6/ADT105136/004.PNG)

目前變數只有在父程序才能夠使用

在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-6/ADT105136/005.PNG)

在.bashrc中把變數用export來讓子程序也能使用此變數
