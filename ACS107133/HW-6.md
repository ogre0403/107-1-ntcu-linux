一  請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。

1.輸入vi ~/.bashrc來編輯檔案，進入編輯檔案模式後，按下i鍵可以進行編輯。

2.在檔案內輸入HOSTS_PATH="/etc/hosts"，接著按ESC鍵，再輸入:wq，才能真正的儲存離開。

3.輸入source ~/.bashrc ，讀入環境設定檔的指令，這樣就不用重新登入變數也能生效了。

4.在輸入cat $HOSTS_PATH來確認有沒有讀取到檔案內容(圖片1)

二  在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。

1.輸入yum groupinstall "Development Tools" 來安裝gcc，但我的會一直跑出cannot find a valid baseurl for repo base/7/x86_64。

2.我上網google了一下解決方法，首先輸入cd /etc/sysconfig/network-scripts，再輸入ls -a，接著輸入vi ifcfg-ens33，將裡頭的ONBOOT=no改成yes，就可以安裝gcc了。

3.輸入vi cprogram.c，將題目上的程式碼輸入到這個檔案中，在按下ESC並輸入:wq儲存離開。

4.輸入gcc cprogram.c編譯程式碼，接著輸入gcc -c cprogram.c，在輸入ll cprogram*，就能看到新產生的目標檔cprogram.o。

5.輸入gcc -o cprogram cprogram.o來產生執行檔，輸入ll cprogram*，執行檔為cprogram。

6.輸入./cprogram來執行此程式碼。(圖2)

7.輸入echo $? ，其值為 1 。

8.沒有讀到HOSTS_PATH，因為它不在子程序內。

三  在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。

1.輸入vi ~/.bashrc來修改檔案，按i進入編輯在剛剛更改變數的下方輸入export HOSTS_PATH，按下ESC輸入:wq儲存並退出，並輸入source ~/.bashrc讓剛剛輸入的指令生效

2.再輸入一次./cprogram執行程式碼，再輸入一次echo $?，結果為(圖3)。


