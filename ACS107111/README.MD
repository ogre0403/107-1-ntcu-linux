+ 用vi .bashrc進入後加上HOSTS_PATH=/etc/hosts
![GITHUB](https://imgur.com/tALweLG.jpg"git圖示")

+ 用source ~/.bashrc使變數生效
![GITHUB](https://imgur.com/2bUR0N9.jpg"git圖示")

+ 用cat $HOSTS_PATH 確認有無讀取到
![GITHUB](https://imgur.com/Mld7hhe.jpg"git圖示")

+ 用vi打入程式碼
![GITHUB](https://imgur.com/jsuUA52.jpg"git圖示")

+ 使用gcc ./a.out執行程式，使用echo $?顯示1
![GITHUB](https://imgur.com/jrW2uWh.jpg"git圖示")

+ 因為是區域變數所以無法讀取


+ 加入export HOSTS_PATH
![GITHUB](https://imgur.com/e5dWaZ1.jpg"git圖示")

+ 使用source ~/.bashrc後再執行一次程式
![GITHUB](https://imgur.com/mmWXPkx.jpg"git圖示")

+ 能讀取到變數echo $?為0