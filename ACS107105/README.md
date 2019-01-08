# HomeWork (V)

#### **First,先進入 *ssh* 先將 *sshd_config* 的內容複製至 *sshd2_config***。

![GITHUB](https://imgur.com/gdUZwDN.jpg "git圖示")

#### **接下來，在 *sshd2config* 中加入PORT(2222)**。

![GITHUB](https://imgur.com/u14YjuU.jpg "git圖示")

#### **並且把 *sshd.service* 的內容複製至 *sshd2.service* 著手進行修改**。
#### **由於Type會影響ExecStart，更改為 leo 方便後面相關判讀**。

![GITHUB](https://imgur.com/VLunS04.jpg "git圖示")

#### **使用 *yum* 指令 查詢需要使用的相關指令包並進行安裝。**
+ yum provides semanage
+ yum install policycoreutils-python

![GITHUB](https://imgur.com/B97mL6N.jpg "git圖示")
![GITHUB](https://imgur.com/rgePMkT.jpg "git圖示")

#### **使用 *semanage* 指令確認已經設定成功**。
+ semanage port -a -t ssh_port_t -p tcp 2222
+ semanage port -l | grep ssh
#### **最後，執行 *netstat -alntp | grep ssh***。
![GITHUB](https://imgur.com/g9PgWVS.jpg "git圖示")




