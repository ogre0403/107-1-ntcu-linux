# ADT105137-HW7
1-1請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。

A: curl指令後加上要下載目標的網址，之後輸入至一個html檔。

![image](https://github.com/Yubo0826/1204/blob/master/1-1.PNG)

1-2使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。

A:cat指令查看剛建立的html檔案，後接管線指令-grep找出error的原因。

![image](https://github.com/Yubo0826/1204/blob/master/1-2.PNG)

2、tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。

A:

參數：

-c ：建立一個壓縮文件的參數指令(create 的意思)；

-x ：解開一個壓縮文件的參數指令！

-t ：查看 tarfile 裡面的文件！

-z ：是否同時具有 gzip 的屬性？亦即是否需要用 gzip 壓縮？

-v ：壓縮的過程中顯示文件！這個常用，但不建議用在背景執行過程！

![image](https://github.com/Yubo0826/1204/blob/master/2-1.PNG)

A: 2> 輸入錯誤訊息

![image](https://github.com/Yubo0826/1204/blob/master/2-2.PNG)
