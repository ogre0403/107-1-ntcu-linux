# 第一題
1. 先 vi  .bashrc 檔案。
![](https://i.imgur.com/99CIdSr.png)
2. 輸入 HOSTS_PATH=/etc/hosts進.bashrc，然後儲存離開。
![](https://i.imgur.com/fiTw3Yf.png)
3. source .bashrc，這樣不登出也刻意讓變數生效。
4. cat $HOSTS_PATH檢查設定是否成功。
![](https://i.imgur.com/RTskU01.png)
# 第二題
1. 確認是否有GCC
![](https://i.imgur.com/Sgkpudf.png)
2. 用vi建立C檔案(檔名.c)，用GCC編譯。
![](https://i.imgur.com/i1BQQWy.png)
![](https://i.imgur.com/zIFUF2P.png)
3. 用a.out檢查，發現檔案無法執行
![](https://i.imgur.com/uZPcreP.png)
4. 解決:vi .bashrc ，在變數前加上export使他可以分享給其他子程序。
5. source .bashrc ，然後a.out，檢查是否解決問題。
![](https://i.imgur.com/YWJ0WIu.png)
![](https://i.imgur.com/smb8ZjQ.png)