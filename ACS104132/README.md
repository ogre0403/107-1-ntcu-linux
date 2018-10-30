1.
groupadd mygroup
groupadd nogroup
useradd -G mygroup -c  myuser1
useradd -G mygroup -c  myuser2
useradd -G mygroup -c  myuser3
echo "MyPassWord" | passwd --stdin myuser1
echo "MyPassWord" | passwd --stdin myuser2
echo "MyPassWord" | passwd --stdin myuser3
useradd -G nogroup -c  nouser1
useradd -G nogroup -c  nouser2
useradd -G nogroup -c  nouser3
echo "MyPassWord" | passwd --stdin nouser1
echo "MyPassWord" | passwd --stdin nouser2
echo "MyPassWord" | passwd --stdin nouser3
mkdir  /srv/myproject
chgrp projecta /srv/myproject
chmod 2770 /srv/myproject
su myuser1 
cd /srv/myproject 
vi myuser1.data
exit
cp /usr/bin/ls /usr/local/bin/myls

2.
ps -l
ps aux
top

3.
find usr/bin usr/sbin
ls -l

