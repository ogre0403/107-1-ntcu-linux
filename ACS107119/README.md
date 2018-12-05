#1

1.先輸入vi ~/.bashrc進入.bashrc進行編輯，再輸入HOSTS_PATH=/etc/hosts新增變數，儲存後執行source ~/.bashrc來套用設定，然後輸入echo $HOSTS_PATH確認是否有新增，再打cat $HOSTS_PATH驗證有毒取道檔案內容。

#2

1.先輸入yum groupinstall "Development Tools"安裝gcc，再用touch新增一個c的程式檔案，並用vi編輯打入程式碼，最後用執行gcc env.c來編譯，用./a.out執行，用echo $?來查看上個指令的回傳值，回傳值為1，而因為$HOSTS_PATH是區域變數，所以程式無法讀取這個變數，
從程式碼可以看出當讀取到空值時會return 1。

#3

1.輸入vi ~/.bashrc，然後進入 .bashrc 進行編輯，再輸入export HOSTS_PATH=/etc/hosts，把之前輸入之變數前面加上export，然後輸入source .bashrc讀取剛剛修改過的檔案內容，輸入gcc test.c編譯 test.c，輸入./a.out，輸出test.c的結果，最後輸入echo $?印出?的內容。 



![](https://ppt.cc/fj4r9x@.png)
![](https://ppt.cc/fTegtx@.png)
  