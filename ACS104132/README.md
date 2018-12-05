1.
(1)
version=$(uname -r)
ver="my kernel version is $version"
echo $ver
(2)
echo $PATH
執行檔搜尋的路徑

2.
(1)
檔名為目錄檔
擁有者為:root
擁有群組是:mail
容量:4096
最後一次被修改/修訂的日期時間:2月16日2017年
檔名:mail
檔案連結數:3
user:可讀寫執行
group:可讀寫執行
others:可讀不可寫可執行
(2)
chmod 755 script
chmod u=rwx,g=rx,o=rx script

3.
(1)
Hard Link 實體連結:
每個檔案都會佔用一個 inode ，檔案內容由 inode 的記錄來指向；
讀取該檔案，必須要經過目錄記錄的檔名來指向到正確的 inode 號碼才能讀取。
Symbolic Link 符號連結:
建立一個獨立的檔案，而這個檔案會讓資料的讀取指向他link的那個檔案的檔名
會佔用掉 inode 與 block
(2)
ln /etc/hosts ~/hosts.real
(3)
ln -s /etc/hosts ~/hosts.symbo

4.
fdisk /dev/sda
n
p
1
1048576
3145728
w






