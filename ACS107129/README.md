# HW-7 第一題

## 使用個人筆電完成

## 第一小題

>請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。

>使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。


======
使用指令: curl https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log | grep eror > aaa ; cat aaa
======


![1](https://images2.imgbox.com/04/34/az0QudFL_o.png)


指令 **curl** 不加參數時，可以下載網址內容並使用螢幕輸出。搭配 **| grep error > aaa** 將其標準輸出內容中含error的項目重新導向aaa，並搭配 **; cat aaa** 輸出aaa的內容。


## 第二小題

>tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。


=====
使用指令: tar -c /var > /dev/null 2> tar-err.log ; cat tar-err.log
=====


![2](https://images2.imgbox.com/86/c2/WEOO1y3I_o.png)


指令 **tar** 搭配參數 **-c** 將/var進行壓縮。搭配指令 **> /dev/null** 將正常輸出丟入黑洞，並搭配 **2> tar-err.log** 將錯誤訊息導入tar-err.log。

最後加上 **; cat tar-err.log** 查看結果，結果如下圖。

![3](https://images2.imgbox.com/07/a4/GK27L7M9_o.png)

![4](https://images2.imgbox.com/f9/40/SYDrUmrv_o.png)
