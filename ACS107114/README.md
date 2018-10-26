# HW3 ACS107114

## 第一題
* 使用useradd建立帳戶examuser1,examuser2,examuser3
![](https://i.imgur.com/LSbXfAF.png)
* 刪除examuser3,連同家目錄與郵件檔案同步刪除
![](https://i.imgur.com/TEu9lvn.png)
* examuser1被刪除 嘗試還原該使用者
以sudo userdel examuser1模擬情形 並以ll /home/檢查
![](https://i.imgur.com/aiCfLcH.png)
以sudo user -u 1001 -m examuser1還原examuser1
![](https://i.imgur.com/PTaUHAC.png)

## 第二題
* 建立examuser4
![](https://i.imgur.com/IVcscn9.png)
* 使用 root 將 /etc/securetty 複製給 examuser4 並賦予所有權限
![](https://i.imgur.com/Ugdo93o.png)

* 檢查是否成功修改權限
![](https://i.imgur.com/DFFDjgI.png)

* 建立 /examdata/change.txt
![](https://i.imgur.com/SED0AIq.png)
* 更改擁有者為 sshd 擁有群組為 users，sshd 可讀可寫 users 群組成員可讀 其他人沒權限
![](https://i.imgur.com/kZtkInt.png)
* 並把日期調整成2012年12月21日
![](https://i.imgur.com/vP14TM0.png)

## 第三題
* 進入/dev/shm/ 並建立unit05(修改其權限) 再建立dir1,dir2,dir3,dir4四個資料夾
![](https://i.imgur.com/uIfIS64.png)
* 修改dir1,dir2,dir3,dir4權限
![](https://i.imgur.com/tte5XgO.png)
* 複製/etc/hosts至 dir1,dir2,dir3,dir4 並將檔名改為 file1,file2,file3,file4
![](https://i.imgur.com/Nn7lfdn.png)
* 修改file1權限
![](https://i.imgur.com/g4zg29e.png)

* 修改file2權限
![](https://i.imgur.com/v6F2CDp.png)

* 修改file3權限
![](https://i.imgur.com/zoKuH4n.png)

* 修改file4權限
![](https://i.imgur.com/NDfjkJH.png)

#### 請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
* dir1 因是 drwxr-xr-- 其他人只能讀
* dir2 因是 drwxr-x--x 只能執行 無法讀
* dir3 因是 drwxr-xr-x 能讀跟執行 無法修改
* dir4 因是 drwxrwxrwx 可以任意執行

#### 請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？
* file1 因是 -rw-r--r-- 只能讀取
* file2 也是 -rw-r--r-- 只能讀取
* file3 因是 -rw-rw-rw- 可以讀取與修改
* file4 因是 -rw------- 故無法使用

#### 請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？
* 無法儲存
* unit05 因是 drwxrwxr-x 其他人沒有修改的權限