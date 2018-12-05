# (I)
+ 使用 *vim* 編輯 bashrc
+ 輸入 HOSTS_PATH="etc/hosts"
+ 儲存後, 使用source ~/.bashrc進行套用設定
+ 使用 *cat* 指令測試是否真的有讀取到內容。

# (II)
+ 執行yum groupinstall "Development Tools"安裝GCC
+ 貼上 題目附上的CODE
+ 使用*gcc env.c*進行編譯
+ 執行./a.out
+ 使用echo $? 觀察前一個指令之回傳值
+ 得知此程式無法讀取到*HOSTSPATH*且$?回傳值為1
+ 由於 *$HOSTS_PATH*為一個區域變數，導致程式無法正常讀取此變數並且可以發現讀取到空值時系統會return 1

# (III)
+ 使用 *vim* 編輯 bashrc
+ 輸入export HOSTS_PATH
+ 儲存後, 使用執行source ~/.bashrc進行套用設定
+ 再次執行./a.out發現程式可以正常讀取 
