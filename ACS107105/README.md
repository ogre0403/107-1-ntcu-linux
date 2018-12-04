# (I)

+ 由於CentOS7尚未內建*wget*。
+ 所以先使用 指令*yum -y install wget* 安裝wget。
+ 使用 *wget* 指令。
## ![GITHUB](https://imgur.com/EjfWj5t.jpg "git圖示")

+ 執行 *cat* 指令 將錯誤的部分找出來。
## ![GITHUB](https://imgur.com/rpsipQA.jpg "git圖示")

# (II)

+ 執行*tar -czf var.tgz /var 2> tar-err.log* 指令。
+ 把錯誤相關訊息導出。
## ![GITHUB](https://imgur.com/FSf4w9b.jpg "git圖示")

+ 使用 *cat tar-err.log* 查看剛剛導出的錯誤。
## ![GITHUB](https://imgur.com/RjrF5Mh.jpg "git圖示")

