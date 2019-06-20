# home page: https://www.pixiv.net/
# login_get: https://accounts.pixiv.net/login?lang=zh_tw&source=pc&view_type=page&ref=wwwtop_accounts_index
# login_post: https://accounts.pixiv.net/api/login?lang=zh_tw
from bs4 import BeautifulSoup
import requests
import re
import os


class Pixiv_user:
    def __init__(self):
        self.session=requests.session()
        self.home_page='https://www.pixiv.net/'
        self.login_get='https://accounts.pixiv.net/login?lang=zh_tw&source=pc&view_type=page&ref=wwwtop_accounts_index'
        self.login_post='https://accounts.pixiv.net/api/login?lang=zh_tw'
        self.params={ 
        'lang': 'zh_tw',
        'source': 'pc',
        'view_type': 'page',
        'ref': 'wwwtop_accounts_index'
        }
        self.data={
            'pixiv_id':'',
            'password':'',
            'return_to':'https://www.pixiv.net/',
            'post_key':''
            }
        self.headers={
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'connection':'keep-alive',
        'content-type':'application/x-www-form-urlencoded',
        'referer':'https://www.pixiv.net/',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
        }

    def login(self): # login
        print('\nStart to login Pixiv...\n')
        # acess home page
        self.session.get(self.home_page,headers=self.headers) 
        
        # get post_key
        key_html=self.session.get(self.login_get,data=self.params,headers=self.headers)
        key_soup=BeautifulSoup(key_html.text,'lxml')
        self.data['post_key']=key_soup.find('input')['value']
        print('\nPost_key:',self.data['post_key'])
        
        # login
        req=self.session.post(self.login_post,data=self.data,headers=self.headers)

        # test login
        if(req.status_code==requests.codes.ok):
            test_html=self.session.get(self.home_page,headers=self.headers).text
            test_soup=BeautifulSoup(test_html,'lxml')
            body_class=test_soup.find('body',{'class':'not-logged-in'})
            if(body_class==None):
                print('\nCode:',req.status_code,' Login success')
            else:
                print('\nLogin failure! Check your id and password!')
                exit()
        else:
            print('\nCode:',req.status_code,' message:',req.json(),'\n\nLogin failure!')
            exit()

    def getImg(self): # download home page illusts
        print('\nStart to get img\n')
        html=self.session.get(self.home_page,headers=self.headers).text

        soup=BeautifulSoup(html,'lxml')
        img_src=soup.find_all('img',{'class':'_thumbnail ui-scroll-view'})
        img_recommend=img_src[:12] # recommend illusts
        img_everyone=img_src[12:18] # everyone new illusts
        img_following=img_src[18:] # following new illusts
        img_want=img_recommend+img_following # You want

        print('\ndownload img: ',len(img_want))

        for i in range(len(img_want)): # for download
            # get img url
            img_url='https://i.pximg.net/'+img_want[i]['data-src'][29:]

            # make directory and find img
            os.makedirs('./Pixiv_img_scraping',exist_ok=True)
            img_r=self.session.get(img_url,headers=self.headers,stream=True)

            # write in file
            img_name=img_url.split('/')[-1]
            with open('./Pixiv_img_scraping/%s' % img_name,'wb') as f:
                for chunk in img_r.iter_content(chunk_size=128):
                    f.write(chunk)
                print('\nSave %s' % img_name)

        print('\nDownload success!')


user=Pixiv_user()
user.data['pixiv_id']=input('Enter your pixiv_id:')
user.data['password']=input('Enter your password:')

try:
    user.login()
except Exception as e:
    print(e)
    exit()
    
user.getImg()
print('\nCall "user.getImg()" for more img!')

            
