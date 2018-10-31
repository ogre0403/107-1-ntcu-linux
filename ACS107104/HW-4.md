#管理群組共用資料的權限設計
##建立群組
###登入root
###建立群組(輸入groupadd mygroup,nogroup)
##建立帳號並加入群組
###建立帳號並加入群組(輸入useradd -G 群組名稱 使用者名稱)→改密碼(輸入passwd 使用者名稱)
##建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
###建立目錄(輸入mkdir 目錄名稱)→chgrp mygroup 檔案名稱→chmod u=rwx,g=rwx,o= 檔案名稱→檢查有無成功ls -l→end
##暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。
###切換myuser1(輸入su myuser1)→進入/srv/myproject(輸入cd /srv/myproject)→建立檔案(vi myuser1.data)→按esc→:wq→登出myuser1(輸入su root)→輸入密碼→end
##複製/usr/bin/ls至/usr/local/bin/myls
###複製cp /usr/bin/ls /usr/local/bin/myls→查看有無成功(輸入ll /usr/local/bin/myls)→end
###雖然 nogroup 群組內的用戶對於 /srv/myproject 應該沒有任何權限，但當 nogroup 內的用戶執行 /usr/local/bin/myls 時，可以產生與 ls 相同的資訊，且暫時擁有 mygroup 群組的權限，因此可以查詢到 /srv/myproject 目錄內的檔名資訊。 也就是說，當你使用 nouser1 的身分執行【myls /srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊。
####輸入chgrp mygroup 檔案名稱→登入nouser1嘗試進入/srv/myproject→結果無法，因為沒有權限→回到root(輸入su root)→輸入密碼→更改檔案權限(輸入sudo chmod u+s 檔案名稱)→查看有無成功(輸入ll 檔案名稱)→切換nouser1(輸入su nouser1)→嘗試進入/srv/myproject→結果成功
##使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)
###回到root→查詢詳細資料(輸入ps aux | grep rsyslog)→儲存(輸入ps aux | grep rsyslog> /root/process_syslog.txt)→查看有無成功(輸入vi process_syslog.txt)→end
##使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)
###find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \;
####*perm:找出特殊權限的檔案
####*4000:因為SUID是四分
####*{}:表示的是由find找到的內容
####*-exec到\;是關鍵字，-exec是開始，\;是結束
####*因為;在bash環境中是有意義的，所以加\來跳脫
###接著儲存(輸入find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \;> /root/findsuidsgid.txt)→查看有無成功(輸入vi findsuidsgid.txt)→end
 