# 用VirtualBox裝設CentOS

1.  安裝CentOS

+   先進入CentOS官網，選擇 Minimal ISO
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-11%20(7).png?raw=true)

+   選其中一個下載點
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-11%20(8).png?raw=true)

+  把下載下來的檔案移至 DVD 光碟機
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-11%20(11).png?raw=true)



2.  VirtualBox設定

+   點選「新增」後，選擇類型為Linux，版本為RedHat 64bit，命名為CentOS，如圖，設定好後按下一步   
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-11%20(1).png?raw=true)

+   設定記憶體大小，將其設定為1024MB，如圖，設定好後按下一步
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-11%20(2).png?raw=true)

+   要建立虛擬硬碟，選擇「立即建立虛擬硬碟」，如圖，點選建立
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-11%20(3).png?raw=true)

+   設定硬碟檔案類型，建立使用VDI，如圖，設定好後按下一步
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-11%20(4).png?raw=true)

+   選擇動態配置(註:所謂的動態配置是說一開始給定的空間並不是如同固定大小般，直接吃掉一定大小的硬碟空間，而是會隨著你的硬碟使用空間多少而增長)
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-11%20(5).png?raw=true)

+   給定硬碟大小8G，如圖，點選建立
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-11%20(6).png?raw=true)

+   回到原本的畫面，按下「設定值」的按鈕
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-15%20(1).png?raw=true)

+   點選「存放裝置」，在存放裝置中，我們會看到兩個控制器，一個是IDE，一個是SATA，IDE當中的，就是光碟機，點選他後，按下右邊有個小光碟圖示，選擇ISO檔後放入
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-15%20(1).png?raw=true)



3.  CentOS主機設定

+   點選「啟動」
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-15%20(3).png?raw=true)

+   語言選擇，這裡選擇中文方便閱讀，如圖，點選繼續
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-17%20(3).png?raw=true)

+   進入首頁後，點選「安裝位置」
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-17%20(4).png?raw=true)

+   在其他存續選項中的分區點選「我要配置分區」
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-17%20(5).png?raw=true)

+  先設置根目錄(/)，再設置家目錄(/home)，最後設置swap，檔案大小自由分配，只要總和不超過8GiB，如圖，點選完成
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18.png?raw=true)

+   等它跑完再點選「接受更改」
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(1).png?raw=true)

+   退回首頁後，點選「網路與主機名」，並打開網路
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(2).png?raw=true)

+   退回首頁後，點選「開始安裝」

+   點選「ROOT密碼」
+   設定ROOT密碼，再點選完成
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(3).png?raw=true)
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(4).png?raw=true)

+   點選「創建用戶」
+   設定用戶資料，再點選完成
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(5).png?raw=true)

+   點選「完成配置」
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(6).png?raw=true)

+   等它跑一陣子後點選「重新啟動」
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(7).png?raw=true)


4.  驗證是否有掛載二個分割區

+   輸入用戶名和密碼後按enter
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(8).png?raw=true)

> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(9).png?raw=true)

+   輸入df，確認是否有兩個分割區
> ![image](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-2/ACS107150/2018-10-18%20(10).png?raw=true)

