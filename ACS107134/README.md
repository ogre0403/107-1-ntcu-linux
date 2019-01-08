* 的使用
">" 的使用
![]()
`的用法
空四個有另一種用法
### 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。
### 完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務，範例如下：

` $ netstat -alntp | grep ssh `
` tcp        0      0 0.0.0.0:22     0.0.0.0:*     LISTEN      1300/sshd `
` tcp        0      0 0.0.0.0:2222   0.0.0.0:*     LISTEN      15275/sshd `
` tcp6       0      0 :::22          :::*          LISTEN      1300/sshd `
` tcp6       0      0 :::2222        :::*          LISTEN      15275/sshd `

1.找到設定ssh連接埠的設定檔
複製一份改連接埠為2222

2.再找到ssh的設定腳本
複製一份將某內容改成步驟一得到得設定檔名