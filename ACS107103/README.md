<em>1-1<em>
+ 用uname -r查看核心的版本
+ 我的是3.10.0-862.e17.x86_64
+ 執行ver="my kernel version is 3.10"

<em>1-2<em>
+ 執行echo $PATH
+ 出現/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
+ 作業系統在執行指令的時候會依照環境變數中所設定的路徑順序，依序尋找路徑下是否有可用的指令，環境變數PATH就是一個紀錄這些路徑的變數

<em>2-1<em>
+ drwxrwsr-x 3 root mail 4096 2月 16 2017 mail
+ 最左邊的d代表這是一個目錄
+ 第一組rwx表示該目錄的擁有者有"讀 寫 執行"的權限
+ 第二組rws表示所屬群組的使用者有"讀 寫 執行"的權限，並且執行者在執行的過程中會獲得該目錄全組的權限(SGID)
+ 第一組r-x表示該目錄的擁有者有"讀 執行"的權限
+ 3這個位置是檔案連結數，這裡表示有三個檔案對應到相同的inode
+ root mail這兩個欄位代表擁有者為root所屬群組為mail
+ 4096這個欄位是檔案的大小，這裡有4096Bytes
+ 2月 16 2017這個欄位是最後一次被修改時間
+ 最右邊的mail則是表示這個目錄的名稱

<em>2-2<em>
+ 若script.sh檔案的權限為-rw-r--r--且希望讓所有人可以執行這個檔案
+ 則必須讓"擁有者 所屬群組 其他人"都具有執行的權限
+ 數字法 : chmod 755 script.sh
+ 符號法 :　chmod u+x,g+x,o+x script.sh

<em>3-1<em>
+ 實體連結是在目錄下創建一筆inode與檔名的對應，所以實際上並不會改變磁碟空間和inode的數量
+ 符號連結是另外創建一個新的文件並指向目標檔案，由於另外創建了一個獨立的檔案，所以實際上會改變磁碟空間和inode的數量

<em>3-2<em>
+ 實體連結 : ln /etc/hosts ~/hosts.real

<em>3-3<em>
+ 符號連結 : ln -s /etc/hosts ~/hosts.symbo

<em>4-1<em>
+ 用df -h指令檢視
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/midterm/ACS107103/centos-2018-11-14-15-51-58.png)

<em>4-2<em>
+ cat /etc/fstab | grep /srv/maildir
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/midterm/ACS107103/centos-2018-11-14-15-52-58.png)

<em>4-3<em>
+ ls -al /srv
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/midterm/ACS107103/centos-2018-11-14-15-54-09.png)

<em>4-4<em>
+  id mailuser
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/midterm/ACS107103/centos-2018-11-14-15-54-36.png)

<em>4-5<em>
+  cat /etc/passwd | grep mailuser
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/midterm/ACS107103/centos-2018-11-14-16-10-54.png)
