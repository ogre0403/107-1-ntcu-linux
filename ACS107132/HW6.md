##�@.

#�Цb�a�ؿ��U��.bashrc�̷s�W�@��shell�ܼ� HOSTS_PATH=/etc/hosts
1. [vi ~/.bashrc]
2. ��i�s��A���W{HOSTS_PATH="/etc/hosts"}
3. ��Esc�A��[:wq]�x�s���}
+ [:p!]���x�s���}

#�����p�󤣵n�X��HOSTS_PATH�ܼƥͮġA����cat $HOST_PATH�T�{��Ū�����ɮפ��e�C
1. [source ~/.bashrc]�Asource�i���ܼƤ��n�X�l�ͮ�(1.jpg)
2. [cat $HOSTS_PATH](2.jpg)

##�G.

#�bC�y���{���i�H��getenv()Ū��LINUX�������ܼơC�ЦbLinux�̽sĶ���d�ҵ{���ð���A�аݧ_��Ū��HOSTS_PATH�H��$?���Ȭ���A�л����C�]�\�ݳz�Lyum groupinstall "Development Tools"�w��gcc�C
1. [vi program.c]
2. ��J�{���X[:wq]�x�s���}(3.jpg)
3. [gcc program.c]-[ll program.c a.out]-[./a.out]
4. ��J[echo $?]��=1
5. �S��Ū��HOSTS_PATH�A�]�������b�l�{�Ǥ�

##�T.

#�b.bashrc�̭n�p��ץ��A��C�y���{���i�HŪ�������ܼƨñN�ɮפ��e��ܡC
1. [vi ~/.bashrc]
2. ��i�s��A��{export HOSTS_PATH}�A��Esc�A[:wq]�x�s���}
3. [source ~/.bashrc]���ܼƤ��n�X�l�ͮ�
4. �A����@��[gcc program.c]-[ll program.c a.out]-[./a.out]
5. ��J[echo $?]��=0