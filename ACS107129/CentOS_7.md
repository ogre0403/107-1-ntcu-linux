# Linux Centos-7 �w�ˤ߱o
==========================

### ���H���ѹϤ�

### �����n�T�{�w�˫�Ʊ�F�����ĪG

>�]���ڳo�����w�˥u�O�b�ӤH�q�����@�ӽm�ߡA�ӫD�n�Ψ�󬰽������\��Ӱ���������Ʊ��A�ҥH�ڪ��򥻵w��t�Ƥ@�w���ڨϥ�Linux CentOS-7 minimal�t�ΡC�o���D�n���m�߬O�϶����ΡA�]����L��������]�w�����S�ʨ�C

## �T�{�ˬd�M��
>�ھڳ������Ѫ�[�ˬd�M��](http://linux.vbird.org/linux_basic/0157installcentos7.php#design)�ӽT�{�ƫe�ǳƪ�������

*	�O�AISO��

*	CentOS 7-x86_64-Minimal-1804

*	x86_64

*	�O

*	�w�M�w�w�Ф��Τ�k

*	�S

*	X

*	�۰ʳ]�w�A���Ӥ]�bMBR

*	�ϥ�DHCP

*	Virtualbox

### �}�l�i�J�w�����`

>���}��Virtualbox�çQ�Υ��W���s�W�ϥܫإߤ@�ӷs�����������A�W�ٴN�]�wCentOS_7�A*����*���Linux�B*����*���Other Linux(64-bit)�B�]�w���O���馳�򥻤j�p�H�K��M�Χ��A���۫إߡC
>�إߧ�����A����ܨ��I��k�W��**�]�w**�ȶi��]�w�C�I��]�w����**�s��˸m**�A�I�ﱱ��Ǫ��s�W�ϥܡA�I����ܺϺШæb�s������ܤw�g�U��������CentOS-7-x86_64-Minimal-1804�M����(ISO��)�C������A�ھڦѮv����ĳ�I��**�]�w**��**����**�i��]�w�A�I�������d2�äĿ�ҥκ����d�A�b**���[��**����ܡu�ȭ��D���v�����d�A�U��W�٫h�۰ʳ]�w�nVirtualbox�F�C
>���ۦ^Virtualbox�����Ұʫإߦn�����������C

===========================

## �i�J�Ұʵe��

![1](https://images2.imgbox.com/d0/70/IHTM2kui_o.png)

![2](https://images2.imgbox.com/69/37/BIHobIwv_o.png)

![3](https://images2.imgbox.com/31/b5/dttXZAMc_o.png)

>�]���O�b�������W�m�ߡB�ɮפ]�O�x���쪺�A�ҥH�N�������Install CentOS 7�A���۸g�L�@�q���ݮɶ���i�J�y���w�˪���ܤ����A��ܤ��� **�c�餤��(�x�W)**�A���۶i�J�w�˺K�n�A���ݨt�Ϊ��۰ʳ]�w������A��ʽվ�]�w�C

![4](https://images2.imgbox.com/5c/f6/7QojaZ6C_o.png)

>�T�{�ɶ��B�䴩�y���B��L�t�m���T��O�o�]�w��L�t�m�����t�m�����Ө�U��J�y�������C

![5](https://images2.imgbox.com/84/e6/8I34pMX9_o.png)

>�w�˨ӷ��|�۰ʳ]�w�A�n���ܥi�ۦ��ܦw�˦�Minimal�u���̤p���w�ˡC

## �ϺФ���

![6](https://images2.imgbox.com/f0/f1/7PdK2fkj_o.png)

![7](https://images2.imgbox.com/12/34/SJJvDnwx_o.png)

>�I��i�J�w�˥ت��a��A�b�����зǺϺФ����Virtualbox�w�]��CentOS_7�ϺСA�U�誺��L�x�s�ﶵ����**���εw��**�I��**�ڱN�t�m����**�A�M���I�����W�觹���C

![8](https://images2.imgbox.com/12/97/isdAHkJR_o.png)

>�i�J���έ�����A���**�зǤ��ΰ�**�A�I�索�U�����[���A���b�I���**biosboot**�B��J2M�e�q����s�W�A�A�̬ۦP�B�J�إ�**/boot**�������I�B��J1G�e�q�C

![9](https://images2.imgbox.com/3a/f0/PwnFV3eb_o.png)

>�P�˨B�J�s�W**/**�M**/home**�������I�A�u�O�ھڳ�������ĳ�A�N�e��̪��˸m�����ѼзǤ��ΰϧ�אּ**LVM**�C

![10](https://images2.imgbox.com/59/b2/MpVCFHP3_o.png)

>�T�{�H�W�B�J������T�{biosboot�U�誺**vda1**�B/boot�U�誺**vda2**�B/�U�誺**centos-root**�M/home�U�誺**centos-home**�C�������I�����W�觹���A�|���X�ܧ�K�n�������A�ݹL�����ܥ��U�豵���ܧ�Y������ʤ��εw�СC

## �^��w�˺K�n

>�̫᪺KDUMP�M����(DHCP)�t�γ��w�g�۰ʳ]�w�n�F�A�ҥH��ܥ��U��}�l�w��

### �Τ�]�w

![11](https://images2.imgbox.com/38/e7/RUeait4A_o.png)

>�]�w**root�K�X**�ðO�n
>�إߥΤ�A�îھڳ�������ĳ�N�Τ�ɯŦ��޲z���A�U�@�u���ѰOroot�K�X�~���ϡC

![12](https://images2.imgbox.com/da/87/H2nuMrFe_o.png)

>�����]�w���ܥ��U�譫�s�}���A���ҫ�Y�����w�ˡA���OMinimal�S���ϧΤ����C