# HW4
#### �Ĥ@�D
+ 1.�إ߸s�զW�٬��G mygroup, nogroup
![GITHUB](https://imgur.com/MmCsqE2.jpg"git�ϥ�")
+ ������root�v��
![GITHUB](https://imgur.com/f2iXbHp.jpg"git�ϥ�")
+ ��groupadd �Ыب�ӷs�s��
+ 2.�إ߱b���W�٬��G myuser1, myuser2, myuser3 �A�q�q�[�J mygroup�A�B�K�X�� MyPassWord
![GITHUB](https://imgur.com/BjVnGCE.jpg"git�ϥ�")
+ ��useradd�����O�̧ǫإ�myuser1,2,3
![GITHUB](https://imgur.com/DlNlzTj"git�ϥ�")
+ �Nmyuser1,2,3�[�Jmygroup ->usermod -g mygroup myuser1
![GITHUB](https://imgur.com/GZAmrzn.jpg"git�ϥ�")
![GITHUB](https://imgur.com/mXHAXPv.jpg"git�ϥ�")
![GITHUB](https://imgur.com/tSaKq7Z.jpg"git�ϥ�")
+ ��passwd�Nmyuser1,2,3�K�X��MyPassWord
+ 3.�إ߱b���W�٬��G nouser1, nouser2, nouser3 �A�q�q�[�J nogroup�A�B�K�X�� MyPassWord
![GITHUB](https://imgur.com/bGZVDfm.jpg"git�ϥ�")
+ ��useradd -g nouser nouser1�����O�̧ǫإ�nouser1,2,3�A�æP�ɱNnouser1,2,3�[�Jmygroup
![GITHUB](https://imgur.com/BDBRR6z.jpg"git�ϥ�")
![GITHUB](https://imgur.com/ofRPrfW.jpg"git�ϥ�")
![GITHUB](https://imgur.com/oAmWOrr.jpg"git�ϥ�")
+ ��passwd�Nnouser1,2,3�K�X��MyPassWord
+ 4.�إߤ@�ӦW�� /srv/myproject ���ؿ��A�o�ӥؿ��i�H�� mygroup �s�դ����ϥΪ̧���ϥΡA�B�i�s�ت��ɮ׾֦��s�աj�� mygroup �C���L��L�H���঳�����v��
![GITHUB](https://imgur.com/VfpkTA0.jpg"git�ϥ�")
+ �إ�/srv/myproject ���ؿ��A��mkdir /srv/myproject
+ �A�N�ӥؿ����ܨ�mygroup�s�աAchgrp mygroup /srv/myproject
![GITHUB](https://imgur.com/PZaBWOz.jpg"git�ϥ�")
+ �����v���Achmod 770 /srv/myproject
+ 5.�Ȯɤ������� myuser1 �������A�ëe�� /srv/myproject �ؿ��A���իإߤ@�ӦW�� myuser1.data ���ɮסA����n�X myuser1
![GITHUB](https://imgur.com/BF2oEHr.jpg"git�ϥ�")
+ ������myuser1�b���Asu myuser1
+ �A������/srv/myproject ���ؿ��U�Acd /srv/myproject
![GITHUB](https://imgur.com/tZPA09M.jpg"git�ϥ�")
+ �b�ӥؿ��U������root�v��
+ �A�Ы�myuser1.data�Amkdir myuser1.data
![GITHUB](https://imgur.com/eWer8Rb.jpg"git�ϥ�")
+ �h�X�ؿ��Acd ..
+ 6.�_��/usr/bin/ls��/usr/local/bin/myls��A�����U�C�ާ@
![GITHUB](https://imgur.com/9W5sFIi.jpg"git�ϥ�")
+ ��Jcp /usr/bin/ls /usr/ocal/bin/myls
+ �A��Jll /usr/local/bin/myls�A�˵��O�_���\
#### �ĤG�D
+ �ϥε{���[����O�A�f�t grep ������r�d�ߥ\��A�N��쪺 rsyslog �������{�Ǫ� PID, PRI, NI, COMMAND ����T��s�� /root/process_syslog.txt �ɮפ��C(�f�t>���ɦV��X)
![GITHUB](https://imgur.com/XEDnTIw.jpg"git�ϥ�")
+ ��Jps aux | grep rsyslog�˵�
![GITHUB](https://imgur.com/CGxCGSQ.jpg"git�ϥ�")
+ ��Jps -l�A�˵�PID�BPRI�BNI�BCMD
![GITHUB](https://imgur.com/jHMwFPd.jpg"git�ϥ�")
![GITHUB](https://imgur.com/Zafdzop.jpg"git�ϥ�")
![GITHUB](https://imgur.com/HY25zi9.jpg"git�ϥ�")
+ �Q��top�Bps aux��XPR��NI�����
![GITHUB](https://imgur.com/MKWCXE3.jpg"git�ϥ�") 
+ ��Jps aux | grep rsyslog > /root/process_syslog.txt
![GITHUB](https://imgur.com/lke37iq.jpg"git�ϥ�")
+ ��Jvi process_syslog.txt�˵�
#### �ĤT�D
+ �ϥ� find ��X /usr/bin �� /usr/sbin ��ӥؿ����A�t�� SUID ���S���ɮ��ɦW�A�èϥ� ls -l �h�C�X��쪺�ɮת������v����A�N�ù������s�� /root/findsuidsgid.txt �ɮפ��C(�ۦ�d��find���O�Ϊk�A�H�Ψϳz�L���ɦV�Ÿ�>��X�ɮ�)
![GITHUB](https://imgur.com/oPA3E76.jpg"git�ϥ�")
+ ��Jfind /usr/bin /usr/sbin -perm /4000�A�C�X�ɦW�Achfn,chsh,mount,chage,gpasswd,newgrp,su,umount,sudo,pkexec,crontab,passwd,pam_timestamp_check,uniz_chkpwd,usernetct1
+ find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \�A�C�X�v��
+ find /usr/bin /usr/sbin -perm/4000 -exec ls -l {} \; > /root/findsuidsgid.txt�A�N�ɮצs��findsuidsgid.txt
+ ��Jvi findsuidsgid.txt�ݬO�_�s�����\