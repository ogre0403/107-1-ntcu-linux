##設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。(10%)
uname -r 
version is 3.10.10-862.el7.x86_64
ver="version is 3.10.10-862.el7.x86_64"
echo $ver會得到
my kernel version is 3.10.10-862.el7.x86_64

##請顯示目前PATH環境變數的值為何，並說明PATH的功用為何? (10%)
系統會照PATH中寫的路徑順序去找指令

##有一個檔案的屬性權限為 drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/，請說明此檔案的特性。(10%)
其他人只能read跟run，而不是mail群組的人可以暫時提升權限為mail的

##假設有一個script.sh檔案的權限為-rw-r--r--，若希望讓所有人可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。(10%)
數字:chmod 755 script.sh 可以用ll檢查
符號:chomd u+x,g+x,o+x script.sh 可以用ll檢查

##說明實體連結與符號連結的差異。(10%)
實體連結=>硬式連結或實際連結，檔案刪除硬體還是能使用，實體連接不會占用inode 
符號連結=>捷徑，原檔刪除就報廢不能用，會占用inode

##在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄) (5%)
ln /etc/host host.real 可以用ll檢查

##在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄) (5%)
ln -s /etc/host host.symbo 可以用ll檢查

