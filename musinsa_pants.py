import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox


ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
title, link, brand, price, star, starnum, imglink = "","","","","","",""


## 함수 선언 부분

# 크롤링 데이터 INSERT
def insertData(title, link, brand, price, star, starnum, imglink,num, pagenum) :
    con, cur = None, None
    sql=""
    data1, data2, data3, data4, data5, data6, data7 = "", "", "", "", "", "", ""

    con = pymysql.connect(host='127.0.0.1', user='root', password='k404', database='musinsarank', charset='utf8')
    cur = con.cursor()

   
    data1, data2, data3, data4, data5, data6, data7 = title, link, price, brand, star, starnum, imglink
    try :
        print("-------%d페이지-%d번---------------------------------" % (pagenum-1,num))
        print(data1)
        print(data2)
        print(data3)
        print(data4)
        print(data5)
        print(data6)
        print(data7)
        sql = "INSERT INTO pants (title,link,price,brand,star,starnum,imglink,updatedate) VALUES ('"+ data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','"+ data5 +"','"+data6+ "','"+data7+ "', NOW())"
        print(sql)
        print("----------------------------------------")
        cur.execute(sql)

    except Exception as err:
        print("예외 발생")
        print(str(err))

    else :
        print("성공")
    
    con.commit()
    con.close()


# 10분마다 데이터 리셋
def resetData() :
    con, cur = None, None 
    con = pymysql.connect(host='127.0.0.1', user='root', password='k404', database='musinsarank', charset='utf8')
    cur = con.cursor()   

    try :    
        cur.execute("DELETE FROM pants")
        cur.execute("ALTER TABLE pants AUTO_INCREMENT=1") 
    except Exception as err:
        print("예외 발생")
        print(str(err))
    else :
        print("리셋+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    con.commit()
    con.close()

##










## 전역 변수부
musinsaUrl = "https://www.musinsa.com/categories/item/003?d_cat_cd=003&brand=&list_kind=small&sort=sale_high&sub_sort=1m&display_cnt=90&group_sale=&exclusive_yn=&sale_goods=&timesale_yn=&ex_soldout=&kids=&color=&price1=&price2=&shoeSizeOption=&tags=&campaign_id=&includeKeywords=%EB%82%A8%EC%84%B1&measure=&page="
pagenum = 1





## 메인 코드부
while(True):
    resetData()
    pagenum = 1
    while(pagenum<7):
        htmlObject = urllib.request.urlopen(musinsaUrl+str(pagenum),context=ssl_context)
        pagenum +=1

        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

        tag = bsObject.find('ul', {'id': 'searchList'})
        tag_list = tag.findAll('div', {'class': 'li_inner'})

        print('###### 실시간 무신사 남성 상의 랭킹 ######')
        num = 1
        for tag in tag_list :

            title = tag.find('p', {'class': 'list_info'})
            mTitle = title.find("a").text.strip()
            uTitle = mTitle.replace("\n", "/")
            #옷이름
            muTitle = uTitle.replace("  ", "")

            link = title.find("a")['href']
            #옷링크
            muLink = 'https:' + link.strip()

            #옷브랜드
            muBrand = "-"
            try:
                brand = tag.find('p', {'class': 'item_title'})
                
                muBrand = brand.find("a").text.strip()
            except: pass

            price = tag.find('p', {'class': 'price'}).text.strip()
            mPrice = price.replace(" ", "")
            #옷가격
            muPrice = mPrice.replace("\n", "->")
            
            #별점
            muStar = "별점없음"
            try : 
                star = tag.find('span', {'class': 'bar'})['style'].strip()
                star = star.replace("width:","")
                star = star.replace("%", "")
                muStar = str(int(star)/20)
            except : pass
            
            #별점참여인원
            muStarnum = "-"
            try : muStarnum = tag.find('span', {'class': 'count'}).text.strip()               
            except : pass
            
          
            #이미지링크
            muImglink = tag.find('img', {'class': 'lazyload lazy'})['data-original'].strip()


            insertData(muTitle, muLink, muBrand, muPrice, muStar, muStarnum, muImglink, num, pagenum)
            num += 1



    #10분에 한번씩 최신화    
    now = time
    print(now.strftime('%Y-%m-%d %H:%M:%S'), end=' ')
    print("pants 크롤링 완료")
    time.sleep(600)





