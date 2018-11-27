# HW6
## 1
* 使用`vi ~/.bashrc`更改bashrc，在其中新增一個變數**HOSTS_PATH=/etc/hosts**
![](https://i.imgur.com/0DfEeQf.png)
* 然後輸入`source ~/.bashrc`使變數生效，然後輸入`cat $HOSTS_PATH`執行該檔案。
![](https://i.imgur.com/pdEn3k4.png)

## 2
* 使用`touch test.c`新增**test.c**的C檔案，並使用`vi test.c`修改檔案，輸入題目所給的程式碼
![](https://i.imgur.com/YmxwmJ0.png)
* 使用`gcc test.c`，在使用`./a.out`執行該檔案，最後使用`echo $?`，顯示出該檔案回傳之變數為**1**
![](https://i.imgur.com/REFA6ab.png)
* 說明:因**getenv()**所輸入環境變數為符號，則輸出字元型別指標，如果名稱不存在於環境變數名單，則會輸出null，因此當我們找不到變數，指標會被設定為null，並且映出錯誤訊息，然後回傳數值 1 。

## 3
* 在第一題所輸入的**HOSTS_PATH="/etc/hosts**，前面加上**export**，形成**export HOSTS_PATH="/etc/hosts** 
![](https://i.imgur.com/5zpEztx.png)
* 接著輸入`source ~/.bashrc`，在按照上題流程做，即可完成
![](https://i.imgur.com/Q58Riq0.png)