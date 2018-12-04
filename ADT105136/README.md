1.

使用curl時配上參數-o來將輸出結果儲存至檔案中
再利用cat搭配pipe找出顯示error的地方

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-7/ADT105136/004.PNG)

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-7/ADT105136/001.PNG)

2.

使用tar可以壓縮檔案也可以觀看壓縮檔或者解壓縮檔案


如果要壓縮檔案用-c

如果要查看檔案用-t

如果要解壓縮檔案-x


-z:透過 gzip  的支援進行壓縮/解壓縮：此時檔名最好為 *.tar.gz

-j:透過 bzip2 的支援進行壓縮/解壓縮：此時檔名最好為 *.tar.bz2

-J:透過 xz    的支援進行壓縮/解壓縮：此時檔名最好為 *.tar.xz



而-則是v解壓縮的過程中將正在處理的檔名顯示出來

-f filename 後面必須接檔案名稱所以會單獨寫出來



最後再利用重導向輸出將標準錯誤輸出(stderr)導至tar-err.log檔案然後顯示出來

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-7/ADT105136/002.PNG)

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-7/ADT105136/003.PNG)
