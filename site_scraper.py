from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
url='https://www.booker.co.uk/products/product-list?categoryName=CS5_100010'
option = webdriver.ChromeOptions()
#     option.add_argument('headless')
driver = webdriver.Chrome('chromedriver',options=option)
driver.get(url)
import urllib
import random
import string
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))
sku = 35042
print(sku)
skuprd = []
main_category = []
sub_category = []
child_category = []
product_name = []
product_feature_image = []
product_description = []
current_price = []
previous_price = []
stock = []
size = []
size_quantity = []
size_extra_price = []
colors = []
tags = []
youtube = []
policy = []
meta_tag = []
meta_description = []
product_type = []
affiliate_link = []
attributes = []
def getdata(weight,sku):
    t1 = driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/h4").text
    t2 = t1.replace("à", "a")
    t3 = t2.replace("%", " percent")
    t4 = t3.replace("®", "")
    t5 = t4.replace("'", "")
    t6 = t5.replace("é", "e")
    t7 = t6.replace("d'", "d")
    t8 = t7.replace("&", "and")
    t9 = t8.replace("£", "pound ")
    t10 = t9.replace("É", "E")
    t11 = t10.replace("Â", "A")
    t12 = t11.replace("Â©", "")
    t13 = t12.replace("©", "")
    t14 = t13.replace("+", "")
    t15 = t14.replace("Booker ", "")
    t16 = t15.replace("*", "")
    t17 = t16.replace("-", "")
    t18 = t17.replace(",", "")
    t19 = t18.replace(":", "")
    t20 = t19.replace("â", "a")
    t21 = t20.replace("€", "E")
    t22 = t21.replace("€™", "E")
    t23 = t22.replace("â€™", "aE")
    t24 = t23.replace("€“", "E")
    t25 = t24.replace("“", "")
    t26 = t25.replace("#", "")
    t27 = t26.replace("!", "")
    t28 = t27.replace("~", "")
    t29 = t28.replace("$", "")
    t30 = t29.replace("@", "")
    t31 = t30.replace("`", "")
    t32 = t31.replace("^", "")
    t33 = t32.replace("+", "")
    t34 = t33.replace("=", "")
    t35 = t34.replace("|", "")
    t36 = t35.replace("\ ", "")
    t37 = t36.replace("?", "")
    t38 = t37.replace(";", "")
    t39 = t38.replace("â„¢", "")
    t40 = t39.replace("â„", "")
    t41 = t40.replace("¢", "")
    t42 = t41.replace("Â±", "")
    t43 = t42.replace("±", "")
    t44 = t43.replace("*", "")
    t45 = t44.replace("'", "")
    title = t45
    try:
        packsizetext = driver.find_element_by_xpath("/html/body/main[1]/div[2]/div[2]/div[2]/div[1]/div[1]/p[1]").text
        time.sleep(1)
        packsizetemp = packsizetext.replace("Pack size: Case of", "", 1)
        packsize = packsizetext.replace("Pack size: Case of", "Case Of", 1)
        time.sleep(1)
        prepricetext = driver.find_element_by_xpath("/html/body/main[1]/div[2]/div[2]/div[2]/div[1]/div[2]/p[2]").text
        preprice1 = prepricetext.replace("£", "", 1)
        if int(packsizetemp) > 5:
            preprice = (float(preprice1)) + 4.00
        else:
            preprice = (float(preprice1)) + 1.00
    except:
        try:
            
            packsizetext = driver.find_element_by_xpath("/html/body/main[1]/div[2]/div[2]/div[3]/div[1]/div[1]/p[1]").text
            time.sleep(1)

            packsizetemp = packsizetext.replace("Pack size: Case of", "", 1)
            packsize = packsizetext.replace("Pack size: Case of", "Case Of", 1)
            time.sleep(1)
            prepricetext = driver.find_element_by_xpath("/html/body/main[1]/div[2]/div[2]/div[3]/div[1]/div[2]/p[2]").text
            preprice1 = prepricetext.replace("£", "", 1)
            if int(packsizetemp) > 5:
                preprice = float(preprice1) + 4.00
            else:
                preprice = float(preprice1) + 1.00
        except:
            try:
                packsizetext = driver.find_element_by_xpath("/html/body/main[1]/div[2]/div[2]/div[4]/div[1]/div[1]/p[1]").text
                time.sleep(1)

                packsizetemp = packsizetext.replace("Pack size: Case of", "", 1)
                packsize = packsizetext.replace("Pack size: Case of", "Case Of", 1)
                time.sleep(1)
                prepricetext = driver.find_element_by_xpath("/html/body/main[1]/div[2]/div[2]/div[4]/div[1]/div[2]/p[2]").text
                preprice1 = prepricetext.replace("£", "", 1)
                if int(packsizetemp) > 5:
                    preprice = float(preprice1) + 4.00
                else:
                    preprice = float(preprice1) + 1.00
            except:
                
                packsizetext = driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[2]/div[1]/div[1]/p[1]").text
                time.sleep(1)

                packsizetemp = packsizetext.replace("Pack size: Case of", "", 1)
                packsize = packsizetext.replace("Pack size: Case of", "Case Of", 1)
                time.sleep(1)
                prepricetext = driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[2]/div[1]/div[2]/p[2]").text
                preprice1 = prepricetext.replace("£", "", 1)
                if int(packsizetemp) > 5:
                    preprice =float(preprice1) + 4.00
                else:
                    preprice = float(preprice1) + 1.00
        
        
    try:
        
        driver.find_element(By.ID,"show-more-details").click()
        time.sleep(5)
        desctext = driver.find_element(By.ID,"product-details-show-more").text
        descupd = desctext.replace("\n", "")
        finalDesc = descupd.replace("Show less...", "")
        t2 = finalDesc.replace("à", "a")
        t3 = t2.replace("%", " percent")
        t4 = t3.replace("®", "")
        t5 = t4.replace("'", "")
        t6 = t5.replace("é", "e")
        t7 = t6.replace("d'", "d")
        t8 = t7.replace("&", "and")
        t9 = t8.replace("£", "pound ")
        t10 = t9.replace("É", "E")
        t11 = t10.replace("Â", "A")
        t12 = t11.replace("Â©", "")
        t13 = t12.replace("©", "")
        t14 = t13.replace("+", "")
        t15 = t14.replace("Booker ", "")
        t16 = t15.replace("*", "")
        t17 = t16.replace("-", "")
        t18 = t17.replace(",", "")
        t19 = t18.replace(":", "")
        t20 = t19.replace("â", "a")
        t21 = t20.replace("€", "E")
        t22 = t21.replace("€™", "E")
        t23 = t22.replace("â€™", "aE")
        t24 = t23.replace("€“", "E")
        t25 = t24.replace("“", "")
        t26 = t25.replace("#", "")
        t27 = t26.replace("!", "")
        t28 = t27.replace("~", "")
        t29 = t28.replace("$", "")
        t30 = t29.replace("@", "")
        t31 = t30.replace("`", "")
        t32 = t31.replace("^", "")
        t33 = t32.replace("+", "")
        t34 = t33.replace("=", "")
        t35 = t34.replace("|", "")
        t36 = t35.replace("\ ", "")
        t37 = t36.replace("?", "")
        t38 = t37.replace(";", "")
        t39 = t38.replace("â„¢", "")
        t40 = t39.replace("â„", "")
        t41 = t40.replace("¢", "")
        t42 = t41.replace("Â±", "")
        t43 = t42.replace("±", "")
        t44 = t43.replace("*", "")
        t45 = t44.replace("'", "")
        desc = t45
    except:
        desc = title
    imgscr = driver.find_element_by_xpath("/html/body/main[1]/div[2]/div[1]/div[1]/a/figure/figure/img").get_attribute("src")
    temp2 = title.split()
    image_name ="imagename"+random_char(5)+".jpg"
    urllib.request.urlretrieve(imgscr, image_name)
    
    newimgenamefinal = "https://theqlocal.com/assets/images/Images/"+image_name
    attb = '{"pack_size":{"values":["'+packsize+'"],"prices":["0"],"details_status":1},"weight":{"values":["'+weight+'"],"prices":["0"],"details_status":1}}'
    dump = ",GroceryCatering,Groceryuk,Cateringessex,Grocery Retail,Tinned Vegetables Retail,UnitedKingdom,Uk,Essex,Wholesalers,Grocery,Groceryuk,GroceryEssex,Convenientstore,Convenient"
   
    metadesc = title+dump
    temp2 = title.replace("&", "and", 1)
    temp2 = temp2.replace("£", "", 1)
    x = temp2.split()
    al = range(len(x))
    temp10 = ""
    for ac in al:
        if ac+1 < len(x):
            temp10 = temp10 +x[ac]+x[ac+1]+"," 

    tagsseo = temp2+dump
    skuprd.append(sku)
    main_category.append("Grocery  Retail")
    sub_category.append("Tinned Vegetables Retail")
    child_category.append("")
    product_name.append(title)
    product_feature_image.append(newimgenamefinal)
    product_description.append(desc)
    current_price.append(preprice)
    previous_price.append("")
    stock.append("")
    size.append("")
    size_quantity.append("")
    size_extra_price.append("")
    colors.append("")
    tags.append(tagsseo)
    youtube.append("")
    policy.append("Test policy")
    meta_tag.append(tagsseo)
    meta_description.append(metadesc)
    product_type.append("normal")
    affiliate_link.append("")
    attributes.append(attb)
    print(newimgenamefinal)

for i in range(1, 52):
    driver.get("https://www.booker.co.uk/products/product-list?categoryName=CS5_200990")
    try:
        
        w="/html/body/div[2]/section/main/div[7]/div[1]/div["+str(i)+"]/div[1]/div/div[3]/p"
        weight = driver.find_element_by_xpath(w).text
        time.sleep(1)
        j="/html/body/div[2]/section/main/div[7]/div[1]/div["+str(i)+"]/div[2]/div[1]/div[2]/p[1]"
        driver.find_element_by_xpath(j).click()
        time.sleep(1)
        sku = sku + 1
        getdata(weight,sku)
        print("done",i)
    except:
        w="/html/body/div[2]/section/main/div[8]/div[1]/div["+str(i)+"]/div[1]/div/div[3]/p"
        weight = driver.find_element_by_xpath(w).text
        time.sleep(1)
        j="/html/body/div[2]/section/main/div[8]/div[1]/div["+str(i)+"]/div[2]/div[1]/div[2]/p[1]"
        driver.find_element_by_xpath(j).click()
        time.sleep(1)
        sku = sku + 1
        getdata(weight,sku)
        print("done",i)
        

import pandas as pd
dict={
    'skuprd': skuprd,
    'main_category':main_category,
    'sub_category':sub_category,
    'child_category':child_category,
    'product_name':product_name,
    'product_feature_image':product_feature_image,
    'product_description':product_description,
    'current_price':current_price,
    'previous_price':previous_price,
    'stock':stock,
    'size':size,
    'size_quantity':size_quantity,
    'size_extra_price':size_extra_price,
    'colors':colors,
    'tags':tags,
    'youtube':youtube,
    'policy':policy,
    'meta_tag':meta_tag,
    'meta_description':meta_description,
    'product_type':product_type,
    'affiliate_link':affiliate_link,
    'attributes':attributes,
}
df=pd.DataFrame(dict)
df.to_csv('goecry retail.csv',index=False)
