# (1)

+ 使用 *echo* 指令 執行ver可得到內容為 my kernel version is 3.10.0-862.e17.x86_64
#
+ 使用 *echo* 指令 執行PATH 可得到內容為     /user/local/sbin:/usr/local/bin:/sbin:/bin:/usr/bin:/root/bin
#
+ PATH為一個紀錄路徑的環境變數

# (2)

+ 此檔案連結數為3
    此檔案擁有者為root且root具有r(讀)w(寫)x(執行)之權限(第一組權限)		
    群組設定為mail,所有加入此群組的帳號可以具有rwx的權限(第二組權限)且使用者具有該目錄全組的     權限(SGID)
    若不是root且沒有加入mail群組,只擁有rx的權限(第三組權限)
    檔案容量為4096bytes
    最後修訂時間為2017/2/16
    
# (3)

+ 若使用實體連結建立連結檔,
+ 只會在目錄中添加一筆inode與檔名對應且磁碟空間.inode數目不變
#
+ 若使用符號連結建立連結檔,會主動新增獨立的新檔案且佔用inode以及block
+ P.s實體連結不能跨越資料系統

+ 建立實體連結 *ln /etc/hosts ~/hosts.real*
+ 建立符號連結 *ln -s /etc/hosts ~/hosts.symbo*

# (4)
+ 使用 df *-h* 指令 顯示有1GB的檔案系統正掛載到/srv/maildir
![GITHUB](https://imgur.com/V0X7xhj.jpg "git圖示")
#
+ 驗證有設定開機自動掛載
![GITHUB](https://imgur.com/ST3KxWm.jpg "git圖示")
#
+ 使用 *ls* 指令 查詢/srv/maildir屬性 以及使用 *id* 指令 檢查(mailuser)使用者屬於mailgroup(群組)
![GITHUB](https://imgur.com/09nvM4E.jpg "git圖示")
#
+ 請用*grep* 指令驗證帳號無法透過shell登入
![GITHUB](https://imgur.com/RlAAwFm.jpg "git圖示")


