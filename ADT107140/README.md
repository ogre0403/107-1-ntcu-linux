##第一題
*創建mygroup nogroup

*利用useradd -G mygroup myuser1~3(建立myuser1~3時同時加入mygroup)
*同理nogroup 和nouser1~3一樣的方式
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/01.png)
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/03.png)
*id 每個user
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/04.png)
*mkdir /srv/myproject
*chgrp mygroup /srv/myproject
*chmod 770 /srv/project
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/05.png)
*切換myuser1 touch myuser1.data
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/06.png)
*cp /usr/bin/ls /usr/local/bin/myls
*切換nouser1 myls /srv/myproject :permission denied
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/07.png)
*su - root 把/srv/myproject的user setuid 
*nouser1即可myls /srv/myproject
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/08.png)
##第二題
*ps aux | grep rsyslog pid為990 command /usr/sbin/rsyslogd-n
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/09.png)
*top  pr20 ni0
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/10.png)
*ps aux | grep rsyslog > /root/process_syslog.txt
*vi process_syslog.txt
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/11.png)
##第三題
*以照此網址find教學:https://blog.gtwang.org/linux/unix-linux-find-command-examples/
*find /usr/bin /usr/sbin -perm /4000
*4為suid
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/12.png)
*find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \;
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/14.png)
*find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \; >  /root/findsuidsgid.txt
*vi findsuidsgid.txt
![](/User/Desktop/新增資料夾 (2)/107-1-ntcu-linux/ADT107140/15.png)

