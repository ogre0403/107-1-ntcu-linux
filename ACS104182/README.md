<strong>第一大題</strong><br>
<em>1.<em><br>
ver = "my kernel version is $(uname -r)" <br>
echo $ver

<em>2.<em><br>
1.echo $PATH<br>
2.當我們在執行一個指令的時候，系統會依照 PATH 的設定去每個 PATH 定義的路徑下搜尋檔案，先搜尋到的指令檔案先被執行之<br>


<strong>第二大題</strong><br>
<em>1.<em><br>
擁有者為root,群組為mail,檔案擁有者可讀、可寫亦可執行,檔案所屬群組可讀、可寫、有特殊權限s,能臨時變成root，間接的修改/etc/passwd，以達到修改自己指令的權限,其他人可讀、可執行但不可寫<br>

<em>2.<em><br>
chmod 647 script.sh <br>
chmod u=rw,g=r,o=rwx script.sh <br> 




<strong>第三大題</strong><br>
<em>1.<em><br>
硬連結: 為同一份資料多新增一個inode，兩個inode指向同一份資料 <br>
符號連結: 作用類似於Window中快捷方式，建立一個文件名指向原來文件 <br>

<em>2.<em><br>
ln ~/hosts.real /etc/hosts <br>

<em>3.<em><br>
ln -s ~/hosts.symbo /etc/hosts <br>






<strong>第四大題</strong><br>
設定1g選項<br>
![5](IMG_0498.jpg)<br>

檢查是否有新增<br>
![5](IMG_0499.jpg)<br>
![5](IMG_0500.jpg)<br>

建立檔案系統<br>
![5](IMG_0501.jpg)<br>

修改/etc/fstab 設定自動掛載路徑<br>
![5](IMG_0502.jpg) <br>





<em>1.<em><br>

<em>2.<em><br>

<em>3.<em><br>

<em>4.<em><br>

<em>5.<em><br>

