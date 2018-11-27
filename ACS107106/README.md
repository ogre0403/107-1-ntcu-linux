#第一題
(1)用vi ~/.bashrc進入，按i進入編輯，輸入HOSTS_PATH="/etc/hosts"，按esc離開編輯，然後:wq儲存離開，用source ~/.bashrc在不登出的情況下讓HOSTS_PATH變數生效，用cat $HOST_PATH可知有讀到檔案(圖1)。

(2)用vi test.c進入，按i進入編輯，輸入範例程式(圖2)，按esc離開編輯，然後:wq儲存離開，接著輸入gcc test.c和./a.out會發現getnev() return NULL，用echo $?，顯示1(代表執行失敗，讀不到HOSTS_PATH)。

(3)用vi ~/.bashrc進入，按i進入編輯，在剛才輸入的變數前面加export，用source ~/.bashrc在不登出的情況下讓HOSTS_PATH變數生效，用cat $HOST_PATH將檔案內容顯示，接著用echo $?，顯示0(代表執行成功，有讀到HOSTS_PATH)(圖3)。