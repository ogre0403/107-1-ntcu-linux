# HW4
## ADT104138 羅苡倫
*****
## 一、管理群組共用資料的權限設計：
*	建立群組名稱為： mygroup, nogroup</br>
*	建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord</br>
*	建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord</br>
*	建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限</br>
*	暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。</br>
*	復制/usr/bin/ls至/usr/local/bin/myls後，完成下列操作</br>
		雖然 nogroup 群組內的用戶對於 /srv/myproject 應該沒有任何權限，但當 nogroup 內的用戶執行 /usr/local/bin/myls 時，可以產生與 ls 相同的資訊，且暫時擁有 mygroup 群組的權限，因此可以查詢到 /srv/myproject 目錄內的檔名資訊。 也就是說，當你使用 nouser1 的身分執行【myls /srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊。

1.利用groupadd指令新增mygroup和nogroup群組。</br>
![新增](https://i.imgur.com/y0eBkf0.jpg)</br>

2.利用useradd -G指令，同時新增使用者並指定群組，再用HW3利用過的技巧--stdin設置密碼。</br>
![新增](https://i.imgur.com/mpx7cpf.jpg)</br>
![新增](https://i.imgur.com/BSzBUaz.jpg)</br>

3.確認創建成功。</br>
![新增](https://i.imgur.com/gg1TB4X.jpg)</br>

4.利用mkdir、chmod和chgrp指令來創建目錄、更改權限和更改群組。</br>
![新增](https://i.imgur.com/Hknbjvd.jpg)</br>

5.利用touch指令來建立檔案。</br>
![新增](https://i.imgur.com/tv54qej.jpg)</br>

6.利用cp A路徑 B路徑 指令來複製目錄，再登入nouser1會發現myls指令無法作用於myproject，這時候先換回root更改目錄權限(u+s指令代表執行時會透過SUID轉換成擁有者)，再切換回去即可執行。</br>
![新增](https://i.imgur.com/KVpjuaX.jpg)</br>
![新增](https://i.imgur.com/a9DoaIG.jpg)</br>
*****
## 二、使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)

1.利用ps aux指令搭配grep搜尋關鍵字，再利用>輸出想要的.txt檔案，執行後透用cat指令察看結果。</br>
![新增](https://i.imgur.com/WSQB8KK.jpg)</br>

*****
## 三、使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)

1.利用find / -perm /4000指令找出含有SUID 的特殊檔案檔名</br>
![新增](https://i.imgur.com/mwklvAN.jpg)</br>

2.加上ls -l以及 > 輸出結果至.txt檔案上。</br>
![新增](https://i.imgur.com/UUEAzU6.jpg)</br>

3.執行vi指令檢查結果。</br>
![新增](https://i.imgur.com/xUBEp8T.jpg)</br>


# 參考資料：[點擊這裡](https://docs.oracle.com/cd/E19683-01/816-4883/6mb2joatb/index.html "參考資料")
# 感謝觀看 The End
