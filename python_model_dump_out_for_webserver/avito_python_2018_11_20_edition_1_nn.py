import pandas as pd
import numpy as np
import mysql.connector

mydb = mysql.connector.connect(
  host = "127.0.0.1",
  user = "root",
  password = "password",
  database = "mydb",
  charset='utf8',
  use_unicode=True
  )
cursor=mydb.cursor()
cursor.execute("SELECT * FROM products ORDER BY upload_date DESC LIMIT 1")
result = cursor.fetchall()
df = pd.DataFrame(result, columns=['title','parent_category_name','category_name','price','description','image_path', 'upload_date'])


###

#讀取SQL中的圖檔檔名後再串上絕對路徑
image_path = df['image_path']
#test路徑image_path = "C://103103103BigData/_node.js/NodejsApps/NodejsWebApp1/uploads/" + str(image_path[0])
#image_path = "/var/www/html/uploads/" + str(image_path[0])
image_path = './uploads/' + str(image_path[0])


#import sys;
#sys.stdout.buffer.write( JSON.encode('utf-8') );
#sys.stderr.buffer.write( JSON.encode('utf-8') );

data = df[['parent_category_name','category_name','price']]


#大項預處理，將parent_category_name 轉成 Label
parent_category_name_map = {"Личные вещи" : 1, "Для дома и дачи" : 2, "Бытовая электроника" : 3, "Недвижимость" : 4, 
                            "Хобби и отдых" : 5, "Транспорт" : 6, "Услуги" : 7, "Животные" : 8, "Для бизнеса" : 9,
                           "個人物品" : 1, "家居與園藝" : 2, "消費類電子產品" : 3, 
                            "房地產" : 4, "愛好與休閒" : 5, "交通工具" : 6, "服務" : 7, 
                            "動物" : 8, "商業營運" : 9                                                  
                           }                                                                     
data['parent_category_name'] = data['parent_category_name'].apply(lambda x : parent_category_name_map[x])


#小項預處理，將category_name 轉成 Label
category_name_map = {
'Товары для детей и игрушки' : 1, 'Мебель и интерьер' : 2, 'Аудио и видео' : 3,
'兒童和玩具用品' : 1, '家具和室內裝飾' : 2, '音樂和視頻' : 3,
'Автомобили' : 4, 'Ремонт и строительство' : 5,
'汽車' : 4, '維修和施工' : 5, 
'Одежда, обувь, аксессуары' : 6, 'Детская одежда и обувь' : 7, 'Квартиры' : 8,
'衣服/鞋子/配飾' : 6, '兒童衣服和鞋子' : 7, '公寓' : 8,
'Товары для компьютера' : 9, 'Собаки' : 10, 'Дома, дачи, коттеджи' : 11,
'電腦產品' : 9, '狗' : 10, '房屋/別墅' : 11,
'Товары для животных' : 12, 'Другие животные' : 13, 'Комнаты' : 14,
'寵物用品' : 12, '其牠動物' : 13, '房間' : 14,
'Коллекционирование' : 15, 'Коммерческая недвижимость' : 16,
 '收藏品' : 15, '商業用地' : 16,
'Посуда и товары для кухни' : 17, 'Красота и здоровье' : 18, 'Аквариум' : 19,
 '廚房用具' : 17, '美容與健康' : 18, '水族館' : 19,
'Телефоны' : 20, 'Часы и украшения' : 21, 'Предложение услуг' : 22, 'Птицы' : 23,
'電話' : 20, '手錶和珠寶' : 21, '服務提供' : 22, '鳥' : 23,
'Спорт и отдых' : 24, 'Музыкальные инструменты' : 25, 'Бытовая техника' : 26,
'運動與休閒' : 24, '樂器' : 25, '家用電器' : 26,
'Игры, приставки и программы' : 27, 'Земельные участки' : 28,
'遊戲/遊戲機/軟體' : 27, '土地' : 28,
'Продукты питания' : 29, 'Кошки' : 30, 'Билеты и путешествия' : 31,
 '食品' : 29, '貓' : 30, '門票與旅行' : 31,
'Книги и журналы' : 32, 'Растения' : 33, 'Гаражи и машиноместа' : 34,
 '書籍和雜誌' : 32, '植物' : 33, '車庫和停車位' : 34,
'Мотоциклы и мототехника' : 35, 'Планшеты и электронные книги' : 36,
   '機車' : 35, '平板電腦和電子書' : 36,
'Оборудование для бизнеса' : 37, 'Настольные компьютеры' : 38, 'Ноутбуки' : 39,
 '商業設備' : 37, '桌上型電腦' : 38, '筆記型電腦' : 39, 
'Велосипеды' : 40, 'Грузовики и спецтехника' : 41, 'Готовый бизнес' : 42,
'自行車' : 40, '卡車和特殊設備' : 41, '已備好之商業模式' : 42,
'Фототехника' : 43, 'Водный транспорт' : 44, 'Охота и рыбалка' : 45,
 '照相設備' : 43, '水上運輸' : 44, '狩獵和捕魚' : 45,
'Оргтехника и расходники' : 46, 'Недвижимость за рубежом' : 47,
'辦公室設備和消耗品' : 46, '海外房地產' : 47
}
data['category_name'] = data['category_name'].apply(lambda x : category_name_map[x])

#price預處理
# 1台幣 = 2.12 盧布 (平均)
data['price'] = data['price'].apply(lambda x: (float)(x)*2.12)
#log1p就是求log(1+x), 以np.e為底. 
data['price'] = np.log1p(data['price'])


###
#將各項數值轉成np.array型別
def get_keras_data(train):
    X = {     
        'parent_category_name': np.array(train.parent_category_name),
        'category_name': np.array(train.category_name),
        'price': np.array(train[["price"]]) #array([[5.9939613],[8.0067005],...[7.3138866]], dtype=float32)
    }  
    return X

final_data = get_keras_data(data)
###

#读取Model
#import tensorflow as tf
#model2 = tf.contrib.keras.models.load_model('model_cateAll_price.h5') 

from keras.models import load_model
model2 = load_model('model_cateAll_price.h5')


res = model2.predict(final_data)[0][0]*100
result = format( res,".2f") + "%"


##圖片模型建構，上網載入權重
from PIL import Image
from keras.preprocessing import image
import keras.applications.inception_v3 as inception_v3
inception_model = inception_v3.InceptionV3(weights='imagenet')

def classify_inception(image_path):
    """Classify image and return top match."""
    img = Image.open(image_path)
    target_size = (224, 224)
    if img.size != target_size:
        img = img.resize(target_size)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = inception_v3.preprocess_input(x)
    preds = inception_model.predict(x)
    return inception_v3.decode_predictions(preds, top=1)[0][0]

#image_confidence = format(classify_inception("C:/Users/iii/OneDrive/Avito/data/models_dump_out/images15.jpg")[2]*100,".2f") + "%"
image_confidence = format(classify_inception(image_path)[2]*100,".2f") + "%"


#11/20  新增評語
canyou = ''
if res <= 20:
    canyou = '加油捏!?'
elif 21 <= res <= 40:
    canyou = '吃飽沒!?'
else:
    canyou = '很行是吧!?'

#目前先回傳總機率p1+圖片識別度p2 + 評語s1
#建立仿json格式存入變數jsonstring
jsonstring='{"p1":"'+result+'",'+'"p2":"'+image_confidence+'",'+'"s1":"'+canyou+'" }'



import sys

sys.stdout.buffer.write( jsonstring.encode('utf-8') );
#sys.stderr.buffer.write( data2.encode('utf-8') );

