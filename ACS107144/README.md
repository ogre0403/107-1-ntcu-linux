### 上網下載VirtualBox

* [VirtualBox下載處](https://www.virtualbox.org/wiki/Downloads)

* 選擇Windows hosts 或 OS X hosts，點按下載。

   > 因為本人的電腦是Mac，所以接下來的步驟為Mac的安裝步驟。

1. 選擇OS X hosts。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/01.png)
2. 下載完成後，在Safari右上角的下載項目中找到VirtualBox的檔案，快速點按兩下開啟。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/02.jpeg)
3. 開啟後，找到VirtualBox.pkg快速點兩下，開始安裝。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/03.jpeg)
4. 此時電腦會詢問你是否同意繼續安裝此程式，選擇「繼續」後，按下右下角的「安裝」。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/04.jpeg)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/05.jpeg)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/06.jpeg)
5. 若安裝受阻擋，請到「系統偏好設定」中的「安全性與隱私權」開啟VirtualBox的安裝權限。
6. 開始進行安裝前電腦會要求用戶輸入密碼，輸入密碼後方可執行安裝。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/07.jpeg)
7. 安裝成功後按下右下角的「關閉」。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/08.jpeg)

### CentOS 7 安裝

* [CentOS 7下載處](https://www.centos.org/download/)

1. 選擇Minimal IOS。點按下載。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/09.jpeg)
2. 下載完畢後，在Safari右上角的下載項目中找到CentOS 7 Minimal ISO，確定下載成功。 


### 建立虛擬機器
* 在Launchpad中開啟VirtualBox
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/10.jpeg)
* 新增
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/11.jpeg)
## 1.名稱和作業系統：
* 名稱：CentOS-7
* 類型：Linux
* 版本：Other Linux (64-bit)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/12.jpeg)

## 2.記憶體大小
* 預設值：512MB
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/13.jpeg)

## 3.硬碟
* 建立虛擬硬碟(VDI)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/14.jpeg)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/15.jpeg)
* 存放裝置：動態配置
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/16.jpeg)
* 硬碟大小：8GB
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/17.jpeg)

## 4.完成新增

### 修改設定值

## 點選設定值(左上方的橘色齒輪)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/18.jpeg)

## 1.存放裝置
* 控制器(IDE)-光碟機(IDE第二個主)-選擇虛擬光碟檔案
* 找到剛剛下載的CentOS 7 Minimal ISO
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/20.jpeg)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/21.png)
## 2.網路設定
* 介面卡一：NAT
* 介面卡二：[僅限主機]介面卡
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/19.jpeg)

### 安裝CentOS作業系統

## 1.啟動
* 選擇Install CentOS 7
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/22.jpeg)

## 2.設定語言
* 中文-繁體中文(台灣)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/23.jpeg)

## 3.安裝目的地(掛載)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/24.jpeg)
* 選擇「讓我自行配置磁碟分割」
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/25.jpeg)
* 進入手動處理分割
* 在列表中找到「+」
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/26.jpeg)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/27.jpeg)
   > /:4096MB

   > /home:2048MB

   > /boot:2048MB

   > swap:366MB
* 確認新增無誤後，按下右上角的「完成」。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/28.jpeg)

## 4.網路與主機名稱：
* 兩張介面卡皆開起
* 修改設定:手動
* IP位址：192.168.0.100和自己的網路 子網路遮罩：255.255.255.0

## 5.開始安裝
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/29.jpeg)

### 用戶設定
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/30.jpeg)
## 1.root密碼

## 2.用戶建立
* 勾選「讓這位使用者成為管理員」

## 6.重新開機
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-2/ACS107144/33.jpeg)
