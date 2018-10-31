#檔案系統管理

檔案系統能夠紀錄檔案的屬性，讓使用者方便管理檔案及目錄

superblock：記錄整體檔案系統的資訊，inode、block的使用量，剩餘量等等，若superblock資料毀損，磁碟就幾乎報銷
inode：記錄檔案屬性，一個檔案占用一個inode，但是可以利用實體連結的方式讓多個檔案擁有同個inode，inode同時也記錄著檔案資料的block號碼
block：檔案資料放置的實體位置，block大小會根據磁區分割的方式來決定，在Ext2中有1K、2K、4K三種級別，當檔案過大時就會占用複數個block，且一個block只能放置一個檔案資料
換句話說，檔案太小有可能會造成空間浪費


#實體連結與符號連結

實體連結(hard link)：建立一個新的檔案，inode、檔案屬性和原本檔案相同，即使原本的檔案刪除新檔案也不會受到影響(block裡的資料沒有被刪除影響)，很像是備份，但限制是不能實體連結到其他硬碟中
符號連結(soft link、symbolic link)：建立一個全新的檔案，此檔案inode、檔案屬性都和原本檔案不同，此檔案會儲存連結檔案的名稱，所以需要使用別的block來儲存，類似捷徑的概念

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-5/ADT105136/001.PNG)

剛開始複製過來的檔案只有一個連結數，但是當做了實體連結後見變成了兩個，一個是原本的/etc/hosts，另一個則是現在看到的/srv/hosts.hard，這兩個檔案最後都會去同一個block抓資料
此時再做一個符號連結，因為要儲存檔案名稱，所以找了還未被放置資料的block，inode不同，同時也造成檔案資訊不同


#連結測試

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-5/ADT105136/002.PNG)

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-5/ADT105136/003.PNG)

![image](https://github.com/boolenboom/107-1-ntcu-linux/blob/HW-5/ADT105136/004.PNG)
