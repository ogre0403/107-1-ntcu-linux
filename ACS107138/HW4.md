1.��Jgroupadd mygroup�A�A��Jgroupsdd nogroup�H�إ�mygroup�Mnogroup�o��Ӹs�աA
�A��Juseradd -g mygroup myuser1, myuser2, myuser3�ӫإ߳o�T�ӱb���A
�A��Jpasswd myuser1�A�M���JMyPassWord�A�]�w�����o�ӱb�����K�X�Amyuser2��myuser3���K�X�]�̦��]�w�C
2.���۴��bnogroup�إ�nouser1, nouser2, nouser3�o�T�ӱb���A
�̤W�z����k�A��Jusersdd -g nogroup nouser1 nouser2 nouser3�A
��Jpasswd nouser1�ӳ]�w���b���K�X�A��JMyPassWord�@�����b�����K�X�A�Nnouser2, nouser3���K�X�]�̷Ӧ��B�J�令MyPassWord�C
3.��J���Omkdir/srv/myproject�ӫإߥؿ��A�A��Jchmod 770�ק��v���A���s�ո̪��H�iŪ�i�g�i����A�Ө�L�ϥΪ̫h�S���v���C
4.��Jsu myuser1�Ӥ�����myuser1�o�ӥΤ�A�A��Jcd/srv/myproject�A�i�h/srv/myproject�o�ӥؿ��A��Jvi myuser1.data�ӫإ��ɮסA
�M����UEsc��J:wq�����}�A�A��Jexit�N�i�H�n�X�C
5.��Jcp /usr/bin/LS�N���ƻs��/user/local/bin/myls�A�A��Jsu nouser1�A������nouser1���Τ�A
��Jll/usr/local/bin/myls�Ӭd�ݸӥؿ����ɦW��T�C

----------------------------------------------------------------------------------------------------------------------------------
1.��Jps aux | grep rsyslog�A�ӧ�rsyslog��PID�O990�A�M���Jps -1 990���PRI�O80�ANI�O0�ACMD�Ousr/bin/rsyslog -n�A
�A���ۿ�Jps aux | grep rsyslog > /root/process_syslog.txt�A�A��Jvi process_syslog.txt�A
�N��T��s��/root/process_syslog.txt���C

----------------------------------------------------------------------------------------------------------------------------------
1.��Jfind/usr/bin usr/bin/usr/sbin -perm/4000�A�i�H���ؿ����t��SUID���S���ɦW�A
��mount change gpass newgrp su sudo pkexe cronyab passwd pam_time_check unix_chkpwd usernetctl�A
�M���Jfind /usr/bin/usr/sbin -perm/4000 -exec is -1 {} \; > /root/findsuidsgid.txt�A����v���A
��Jvi findsuidsgid.txt�A�N�����s��/ root /findsuidsgid.txt�ɮפ��C
