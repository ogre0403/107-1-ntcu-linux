# ADT105137_HW6

1.請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。

A:打指令vi .bashrc編輯檔案， 打入HOSTS_PATH=/etc/hosts

![image](https://github.com/Yubo0826/1127/blob/master/1-1.PNG)

A:利用source指令，使不登出讓HOSTS_PATH變數生效

![image](https://github.com/Yubo0826/1127/blob/master/1-2.PNG)

![image](https://github.com/Yubo0826/1127/blob/master/1-3.PNG)

2.在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。

A:建立檔案test.c， .c是C語言檔案的常用副檔名，打完範例檔案後，用gcc指令編譯，此時家目錄會出現一個叫做.a.out的檔案，再輸入./.a.out，使編譯完的程式顯示出來

![image](https://github.com/Yubo0826/1127/blob/master/2-1.PNG)

![image](https://github.com/Yubo0826/1127/blob/master/2-2.PNG)


