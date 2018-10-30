![GITHUB](https://imgur.com/6LZPM77.jpg"git圖示")

+ 建立群組mygroup、nogroup

![GITHUB](https://imgur.com/ytnEHfJ.jpg"git圖示")

+ 使用useradd -G mygroup myuser1-3

![GITHUB](https://imgur.com/xiInYE7.jpg"git圖示")

+ 設定密碼

![GITHUB](https://imgur.com/Tp1s0lX.jpg"git圖示")

+ 同樣方法設定帳號nouser1-3

![GITHUB](https://imgur.com/FWIIDZR"git圖示")

+ 建立資料夾srv後進入後再建立myproject後用chgrp改變群組chmod改變權限

![GITHUB](https://imgur.com/ePzh7y9.jpg"git圖示")

+ 切換使用者為myuser1後用touch在myproject建立myuser1.data
 

![GITHUB](https://imgur.com/MD4WcRA.jpg"git圖示")

+ 復制/usr/bin/ls至/usr/local/bin/myls

![GITHUB](https://imgur.com/ArhpxEr.jpg"git圖示")

+ 切換使用者為nouser1後用myls看myproject

+ 第一題結束

![GITHUB](https://imgur.com/4Z3oZeJ.jpg"git圖示")

+ 使用ps aux | grep rsyslog看其UID為851及其他資料

![GITHUB](https://imgur.com/hIc7I8E.jpg"git圖示")

+ 使用top看UID的詳細資料

+第二題結束

![GITHUB](https://imgur.com/VxL3Wy6.jpg"git圖示")

+ 用find /usr/bin /usr/sbin -perm /4000看題目要求的資料

![GITHUB](https://imgur.com/SYxxMa6.jpg"git圖示")

+ 用find /usr/bin /usr/sbin -perm /4000 -exec ls -s {}\;看權限

![GITHUB](https://imgur.com/Pys7Qrp.jpg"git圖示")

+ 用find /usr/bin /usr/sbin -perm /4000 -exec ls -s {}\; > /root/findsuidsgid.txt

![GITHUB](https://imgur.com/MASPX2V.jpg"git圖示")

+ 用vi看findsuidsgid.txt

