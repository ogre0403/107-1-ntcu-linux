一.

1.得知apache log的網址是https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log

2.輸入curl https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log | grep error > screen 將error的原因輸入到screen這個檔案

3.cat screen 將error輸出至螢幕(圖1)

二.

1.輸入tar -jcv -f filename.tar.bz2 /var 2> tar-err.log 將/var進行壓縮並將錯誤訊息傳到 tar-err.log

2.再輸入cat tar-err.log可查看錯誤訊息(圖2)