#1.1
指令groupadd mygroup, nogroup
#1.2
指令useradd -g mygroup myuser1, myuser2, myuser3<br />
passwd myuser1, myuser2, myuser3
再把MyPassWord輸上去
#1.3
同1.2
#1.4
mkdir /srv/myproject 
chmod 770<br />
chgrp mygroup mkdir /srv/myproject 
#1.5
su myuser1<br />
cd /srv/myproject<br />
vi myuser1.data<br />
Esc :wq<br />
然後再exit登出
#1.6
cp /usr/bin/ls至/usr/local/bin/myls<br />
su nouser1<br />
ll /usr/local/bin/myls就可以查看了
#2
ps aux | grep rsyslog找出PID為990<br />
ps -l 990<br />
找出PRI為80，NI為0,CMD為/usr/bin/rsyslogd -n<br />
ps aux | grep rsyslog > /root/process_syslog.txt<br />
vi process_syslog.txt<br />
成功轉存
#3
find /usr/bin usr/bin /usr/sbin -perm /4000
得chfn<br />
  mount<br />
  chage<br />
  gpasswd<br />
  newgrp<br />
  su<br />
  umount<br />
  sudo<br />
  pkexec<br />
  cronyab<br />
  passwd<br />
  pam_time_check<br />
  unix_chkpwd<br />
  usernetctl<br />
再
find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \; >  /root/findsuidsgid.txt<br />
   vi findsuidsgid.txt<br />
成功轉存