##�]�wvirtualbox���������A�[�J�@�ihost-only�����d�A�bLinux�̳]�w����������������192.168.200.100/24�C�Х� `ifconfig`���ҡC

* �bVirtualBox���A���k�W��**����u��**->**�D�������޲z��**->**�إ�**
* ��**���e**�վ���إߪ������d�A��ܤ�ʲպA�����d�A�N**IPv4 ��}�אּ192.168.200.10**
* ![1.png]

* **�����u��**->**�]�w��**->**����**->**���[��G�ȭ��D���d**
* ![2.png]

* `ifconfig enp0s3 192.168.200.100`->`ifconfig enp0s3`�d��
* ![3.png]


##nginx�O�@�M�������A���n��A�Х�`yum`�w�ˡA�z�L`systemctl`�Ұʫ�A�ϥ�`netstat`����nginx���b�ϥ�Port 80�C

* �]�wnginx��yum�ɮ�
* `vi /etc/yum.repos.d/nginx.repo`
* �s�W���e�G
  [nginx]
  name=nginx repo
  baseurl=http://nginx.org/packages/centos/7/$basearch/
  gpgcheck=0
  enabled=1

* `yum install nginx`�w��
> �o�䤣���D���ƻ�@���X���A���G���}���N�n�F�C�C�C
* `service nginx start`�A`chkconfig nginx on`�Ұ�nginx
* `netstat -tulnp`�d��port
* ![4.png]


##�z�L���� windows �W���s�����A�s�u��192.168.200.100�C������ҥi�H�s�u��Linux�W��nginx�������A���C

* ![5.png]


##�bLinux�̡A��`curl`�s�u��192.168.200.100�C������ҥi�H�s�u��Linux�W��nginx�������A���C

* `curl 192.168.200.100`
* ![6.png]


###nginx����x�ɦ��`/var/log/nginx`�ؿ��U�A��s�u���s�b�������ɡAnginx�|�O��������T�A�榡�p�U�C�䤤client��쬰�Ȥ��ip�C

* `cat /var/log/nginx/error.log | cut -d ' ' -f 16 | sort | uniq -c`
* ![7.png]