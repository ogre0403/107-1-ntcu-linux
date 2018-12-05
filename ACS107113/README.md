##Limux期中考

####第一題

+1.

+輸入指令，檢視資訊。
---
# uname -r
---

+設定變數。
---
ver="my kernel version is 3.10"
---
---
echo $ver
---

+2.輸入指令
---
# echo $PATH
---

+作業系統會在PATH環境變數中設定的路徑，依序尋找各路徑下是否有要使用的指令。

####第二題

+1.

+擁有者有權讀取、寫入及執行，群組內的人有權讀取、寫入及能以檔案擁有者的身分執行，其他則只能讀取和執行。

+擁有者為root。

+所屬群組為mail。

+檔案容量為4069。

+檔案最後修改時間為2017/02/16。

+檔名為mail/。

+2.

+數字法
---
# chmod 755 script.sh
---

+符號法
---
# chmod u=rwx,g=rx,o=rx script.sh
---

####第三題

+1.

+實體連結

+使用實體連結時，磁碟空間與inode數目不會改變，只是在目錄家一筆inode與檔名的對應。

+符號連結

+符號連結是再建立一個獨立檔案，該檔案會址性目的黨，資料讀取時，會指向它連結的目的檔。

+2.

+切換到家目錄下
---
# cd
---

+建立實體連結
---
# ln /etc/hosts hosts.real
---

+檢查
---
# ll -i /etc/hosts hosts.real
---

+3.

+切換到家目錄下
---
# cd
---

+建立符號連結
---
# ln -s /etc/hosts hosts.symbo
---

+檢查
---
# ll -i /etc/hosts hosts.symbo
---

####第四題

+1.

+2.

+3.

+使用ls檢查
![GITHUB]( https://imgur.com/h4jeJa2.jpg"git圖示")

+4.

+使用id檢查
![GITHUB]( https://imgur.com/xEMJs2I.jpg"git圖示")

+5.



