1.打開虛擬器，登入root，輸入vi ~/.bashrc來進入編輯檔案的模式，在按下i即可開始編輯
2.在檔案內的一處輸入HOSTS_PATH="/etc/hosts"，來新增這個變數，輸入完後按下ESC鍵離開編輯，
再輸入:wq就可以儲存然後離開編輯模式了。
3.輸入source ~/.bashrc，讀入環境設定檔的指令，讓他可以不用重新登入，變數也能生效。
3.離開後，輸入cat $HOSTS_PATH確認是否能成功讀取到檔案內容。(附圖1)
------------------------------------------------------------------------------------------------------------------------
1.輸入yum groupinstall "Development Tools"來安裝GCC，卻在最後一行跑出cannot find a valid baseurl for repo base/7/x86_64，
所以輸入nmtui，去檢查網路是否有開啟，打開網路設定之後，再輸入一次yum groupinstall "Development Tools"即可安裝成功。
2.安裝成功後，輸入cd回家目錄，輸入vi cprogram，將程式碼輸入到cprogram這個檔案中(檔名是隨便取的)，
按ESC離開編輯模式，再輸入:wq儲存並離開。
3.輸入gcc cprogram.c來進行程式碼的編譯，沒有出現error的話，輸入gcc -c cprogram.c，再輸入ll cprogram*，
可以找到新的目標檔cprogram.o。
4.輸入gcc -o cprogram cprogram.o來產生執行檔，輸入ll cprogram*，可以看到執行檔為cprogram。
5.輸入./cprogram來執行此程式碼。(附圖2)
6.輸入echo $?，會跑出1。
7.沒有讀到HOSTS_PATH，因為它不在子程序內。
-------------------------------------------------------------------------------------------------------------------------
1.輸入vi ~/bashrc進行修改檔案的動作，按下i開始編輯，在前面更改變數的下方輸入export HOSTS_PATH，
按ESC離開編輯模式，在輸入:wq儲存並離開，在輸入source ~/bashrc，讓輸入的指令生效。
2.再輸入一次./cprogram執行程式，再輸入一次echo $?，會跑出1。

