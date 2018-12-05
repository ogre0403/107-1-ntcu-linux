(一)
1.輸入" vi ~/.bashrc ": 編輯檔案，按下 i 進行編輯。
2.檔案內輸入" HOSTS_PATH="/etc/hosts" "
3. 按ESC鍵，輸入" wq " !!!
4. 輸入" source ~/.bashrc "，讀入環境設定檔的指令
5. 輸入" cat $HOSTS_PATH "確認
(二)
*失敗
1.用" vi/vim 檔名.c "新增一個檔案，並輸入程式碼
2.執行" gcc 檔名.c "(或用yum groupinstall "Development Tools"安裝gcc)
3.輸入" ll 檔名.c a.out "
4.執行" a.out " 讀不到" HOSTS_PATH "，因為不在子程序
5.輸入" echo $? "，會顯示" 1 "，代表無法成功執行
*成功 
1. 新增" export HOSTS_PATH "
2. 再輸入一次" source ~/.bashrc "
(下面的其實就是前面的再做一次)
3. 用" vi/vim 檔名.c "新增一個檔案，並輸入程式碼
4. 執行" gcc 檔名.c "(或用yum groupinstall "Development Tools"安裝gcc)
5. 輸入" ll 檔名.c a.out "
6. 執行" a.out "，可以讀到" HOSTS_PATH "
7. 輸入" echo $? "，會顯示" 0 " ，代表成功執行
(三)
1. 輸入" vi ~/.bashrc "，進入 .bashrc 編輯
2. 輸入" export HOSTS_PATH=/etc/hosts "
3. 在輸入的變數前面輸入" export "
4. 輸入" source .bashrc "讀取修改內容
5. 輸入" gcc test.c "編譯 test.c
6. 輸入" ./a.out "
7. 輸出" test.c "的結果
8. 輸入" echo $ "所印出內容。