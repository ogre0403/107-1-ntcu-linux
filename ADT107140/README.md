#第一題
#用useradd和passwd建立examuser123三個使用者
#https://imgur.com/1vTPk5o
#利用userdel -r刪除examuser3
#利用userdel刪除examuser1
#然而examuser1並未完整刪除
#https://imgur.com/WYwsswG
#利用useradd -u ID -U user 使examuser1恢復
#https://imgur.com/TJBEi9C

#第二題
#建立examuser4
#輸入cp 原地 目的地來複製/etc/securetty
#https://imgur.com/wptdxIw
#用chown使securetty檔案所有權交給examuser4
#https://imgur.com/T9ZlTii
#建立一個examdata資料夾 並於此資料夾內建一txt檔
#https://imgur.com/E28FZmV
#使用chmod chgrp使txt使用者與團體改為sshd和users
#chmod使txt為使用者可讀可寫,團體可讀,他人無權限
#https://imgur.com/w4rD3xV
#touch -t 日期時間改變檔案時間
#https://imgur.com/s8Ilz3s

#第三題
#在/dev/shm建立unit05資料夾
#並於unit05建立dir1~4資料夾
#https://imgur.com/XoHoWyM
#cp /etc/hosts到dir1~4中
#https://imgur.com/3gj0Knl
#chmod dir1~4的權限
#https://imgur.com/TGYmqrJ
#chmod dir2~4裡的hosts權限 因dir1的hosts無需修改
#https://imgur.com/QFdDofO
#切換為一般使用者
#ll /dev/shm/unit05/dir1~4 
#dir1沒x無法進入,dir2可進入然而卻沒有r無法閱讀
#dir3有rx可進入可閱讀,dir4有rwx可閱讀可進入甚至可編輯
#https://imgur.com/9bIE0fD
#ll /dev/shm/unit05/dir1~ 4/hosts
#dir1的hosts沒有x無法進入
#dir2的hosts只有獨而已
#dir3的hosts有rw可讀可寫
#dir4的hosts沒有任何權限
#https://imgur.com/H5J9hzx
#vim每個檔案,dir1沒有x使期中的檔只能閱讀
#https://imgur.com/Xp1t7EF
#dir2也是只有讀的權限而已
#https://imgur.com/lnNizC2
#dir3有rw可讀可寫
#https://imgur.com/fMZB4gv
#dir4沒有任何權限連進入都無法
#https://imgur.com/MEGgqLu

