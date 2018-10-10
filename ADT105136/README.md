# 使用VirtualBox安裝Linux作業系統

1.打開你的VirtualBox，還沒有的可以去https://www.virtualbox.org/wiki/Downloads 這裡下載。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(1).PNG)
2.先建立一個虛擬機器，打上名稱。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(2).PNG)
3.設置記憶體大小，通常只要是非圖形介面的作業系統1G的記憶體就很夠用，但我貪心還是給他2G。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(3).PNG)
4.再來建立磁碟機，可以存放資料的磁碟機。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(4).PNG)
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(5).PNG)
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(6).PNG)
5.設定磁碟機要多大，這裡我設置20GB。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(7).PNG)
6.按建立之後就會多出一台屬於你的虛擬機器啦！不過這台機器上面還沒有安裝任何作業系統。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(8).PNG)
7.所以這時候就要去網站上下載Linux的光碟映像檔(.iso)。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(10).PNG)
8.這裡有三種，都是可以使用的，這裡我選擇檔案容量最小的minimal，以後有我想要用的程式在安裝就行了。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(11).PNG)
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(12).PNG)
9.下載好了之後就可回到VirtualBox設定一下虛擬機器
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(9).PNG)
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(13).PNG)
10.找出剛剛下載的ISO檔，此時應該會長這樣。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(14).PNG)
11.再來是設定虛擬機器的網路，預設已經有連到外面的網路卡了，要再開一張連到自己電腦的網路卡，選到介面卡2並且勾選「啟用網路卡」，如下圖。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(15).PNG)
12.這樣設定就完成了，現在我們將虛擬機器開機，此時會出現這個畫面，選擇Install CentOS 7。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(16).PNG)
13.等他跑一下。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(17).PNG)
14.此時會出現這個畫面，語言的選擇就用預設的英文即可，按Continue。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(18).PNG)
15.在這個頁面時要做一些設定，要手動將磁區分割，按下「INSTALLATION DESTINATION」。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(19).PNG)
16.找到「I will configure partitioning.」並選起來，接著按左上角的「Done」。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(20).PNG)
17.找到下圖中滑鼠所在的「+」並且按下去。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(21).PNG)
18.依照Linux作業系統的規劃，必須先建立根目錄「/」。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(22).PNG)
19.依照上述方法把剩下的磁區分完，如下圖，按「Done」之後會出現一個視窗，選擇「accept」，完成後會回到原本的頁面，這裡就設定完了，繼續下一頁的設定。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(23).PNG)
20.這裡設定root及使用者的帳戶，密碼就自己設定。設定完密碼之後等待一下直到畫面中出現「Reboot」的按鈕後按下。
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(24).PNG)
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(25).PNG)
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(26).PNG)
21.接下來只要輸入剛剛設定的帳戶登入，就成功完成Linux作業系統的安裝了！
![image](https://github.com/boolenboom/ADT105136/blob/boolenboom-image/LinuxOS%20(27).PNG)
