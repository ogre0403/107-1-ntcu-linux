第一題
使用 vim 編輯 bashrc

![5](https://user-images.githubusercontent.com/43788227/51441239-79b08200-1d0a-11e9-82bc-41326052a262.PNG)

在最末行新增shell變數HOSTS_PATH=/etc/hosts

![6](https://user-images.githubusercontent.com/43788227/51441295-0eb37b00-1d0b-11e9-84b4-17016e92b199.PNG)

用 source ~/.bashrc 使修改過的變數不用再次登入就生效

![7](https://user-images.githubusercontent.com/43788227/51441337-51755300-1d0b-11e9-8b9b-e653c94b1372.PNG)

用 cat $HOSTS_PATH 來確認有寫入

![8](https://user-images.githubusercontent.com/43788227/51441363-897c9600-1d0b-11e9-9e94-6773c1070674.PNG)

第二題
執行yum groupinstall "Development Tools"安裝GCC
貼上 題目附上的CODE
使用gcc env.c進行編譯
執行./a.out
使用echo $? 觀察前一個指令之回傳值
得知此程式無法讀取到HOSTSPATH且$?回傳值為1
由於 $HOSTS_PATH為一個區域變數，
導致程式無法正常讀取此變數並且可以發現讀取到空值時系統會return 1

