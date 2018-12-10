import pandas as pd
import numpy as np
import mysql.connector
import sys


#讀取Model
#import tensorflow as tf
#model2 = tf.contrib.keras.models.load_model('model_cateAll_price.h5') 

import tensorflow as tf
model2 = tf.contrib.keras.models.load_model('2018_11_21_nn_model_for_webserver.h5') 

#先載入翻譯套件(中>俄文)
#from py_translator import Translator : 11/29更新測試py_translator套件出現異常錯誤，改用translate模組
from translate import Translator
translator= Translator(to_lang="ru", from_lang='zh')

#預先載入訓練好的tokenizer
import pickle
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    
with open('tokenizer1.pickle', 'rb') as handle:
    tokenizer1 = pickle.load(handle)

#import 文字相關套件  
from keras.preprocessing import text, sequence
from keras.preprocessing.sequence import pad_sequences


#大項預處理，將parent_category_name 轉成 Label
parent_category_name_map = {"Личные вещи" : 1, "Для дома и дачи" : 2, "Бытовая электроника" : 3, "Недвижимость" : 4, 
                            "Хобби и отдых" : 5, "Транспорт" : 6, "Услуги" : 7, "Животные" : 8, "Для бизнеса" : 9,
                           "個人物品" : 1, "家居與園藝" : 2, "消費類電子產品" : 3, 
                            "房地產" : 4, "愛好與休閒" : 5, "交通工具" : 6, "服務" : 7, 
                            "動物" : 8, "商業營運" : 9                                                  
                           }                                                                     

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


##圖片模型建構，上網載入權重
#"""
from PIL import Image
from keras.preprocessing import image
import keras.applications.inception_v3 as inception_v3
inception_model = inception_v3.InceptionV3(weights='imagenet')

def classify_inception(image_path):
#    Classify image and return top match.
    img = Image.open(image_path)
    target_size = (224, 224)
    if img.size != target_size:
        img = img.resize(target_size)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = inception_v3.preprocess_input(x)
    preds = inception_model.predict(x)
    return inception_v3.decode_predictions(preds, top=1)[0][0]
#"""

#評語
def comment(res):
    canyou = ''
    if res < 10:
        canyou = '幫你呼呼'
    elif 10 <= res < 20:
        canyou = '再接再厲～還可以再更好！'
    elif 20 <= res < 30:
        canyou = '再加把勁喔！甘巴答!'
    elif 30 <= res < 50:
        canyou = '哎唷不錯喔～厲害喔！'
    else:
        canyou = '您真是行銷高手！'
    return canyou


def get_keras_data(train, pad_sequence, pad_sequence1):
        X = {
        'seq_title': pad_sequence,
        'seq_description': pad_sequence1,
            
        'parent_category_name': np.array(train.parent_category_name),
        'category_name': np.array(train.category_name),
        'price': np.array(train[["price"]]),
        'image_confidence' : np.array(train[["image_confidence"]])
    }
        print("Data ready for Vectorization")    
        return X

###############node_python_IPC.py 程式碼如下:

from socketIO_client import SocketIO, LoggingNamespace
import sys,json;

def onConnect():
        print('Python process connected to socket.io Sever ...');

def onReceiveMessage(message):
        #message為dictionary如{'data':'xxx'}
        print("Message from node.js server:", message);
        #Put your code here.
        #連線mysql資料庫
        mydb = mysql.connector.connect(
        host = "127.0.0.1",      user = "root",      password = "password",
        database = "mydb",      charset='utf8',      use_unicode=True     
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM products ORDER BY upload_date DESC LIMIT 1")
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=['title','parent_category_name','category_name','price','description','image_path', 'upload_date'])ˊ
        
        
        ##1. 圖片模型----------------------------------------------------------------------------------
        #讀取SQL中的圖檔檔名後再串上絕對路徑
        image_path = df['image_path']
        image_path = './uploads/' + str(image_path[0])
        
        
        r = classify_inception(image_path)[2]
        image_confidence = format(r*100,".2f") + "%"
        #image_confidence = 'Testing...
        
        
        #2. 總機率模型----------------------------------------------------------------------------------   
        data = df[['parent_category_name','category_name','price', 'title', 'description']]
        data['image_confidence'] = r
        
        #資料處理        
        data['parent_category_name'] = data['parent_category_name'].apply(lambda x : parent_category_name_map[x])
        data['category_name'] = data['category_name'].apply(lambda x : category_name_map[x])
        #price預處理
        # 1台幣 = 2.12 盧布 (平均)
        data['price'] = data['price'].apply(lambda x: (float)(x)*2.12)
        #log1p就是求log(1+x), 以np.e為底. 
        data['price'] = np.log1p(data['price'])
        
        #文字預處理
        #11/29更新測試py_translator套件出現異常錯誤，改用translate模組
        #data['title'] = Translator().translate(text=data.title[0], dest='ru').text
        #data['description'] = Translator().translate(text=data.description[0], dest='ru').text
        
        #翻譯俄文
        data['title'] = translator.translate(data.title[0])
        data['description'] = translator.translate(data.description[0])
        
        #文字對應詞袋，轉換數值並截長補短
        sequence = tokenizer.texts_to_sequences(data.title.str.lower())
        sequence1 = tokenizer1.texts_to_sequences(data.description.str.lower())
        pad_sequence=pad_sequences(sequence, maxlen=15) 
        pad_sequence1=pad_sequences(sequence1, maxlen=50) 
        
        #預測結果 (大小項+數字)
        final_data = get_keras_data(data, pad_sequence, pad_sequence1)
        res = model2.predict(final_data)[0][0]*100
        result = format( res,".2f") + "%"

'

        
        #11/20  新增評語
        comm = comment(res)

        #回傳總機率p1+圖片識別度p2 + 評語s1, 建立仿json格式存入變數jsonstring
        jsonstring='{"p1":"'+result+'",'+'"p2":"'+image_confidence+'",'+'"s1":"'+comm+'" }'
 
        #
        #sys.stdout.buffer.write( jsonstring.encode('utf-8') );
        #sys.stderr.buffer.write( data2.encode('utf-8') );
        #print(jsonstring.encode('utf-8'));

        #發送訊息事件(python-message)給socket.io伺服器
        socketIO.emit( 'python-message', str(jsonstring) );
        #socketIO.emit( 'python-message', jsonstring.encode('utf-8') );

#與socket.io伺服器建立連線
socketIO = SocketIO( 'localhost', 1337, LoggingNamespace );

#註冊 當連線建立 之事件處理器
socketIO.on('connect', onConnect);

#註冊 當接到socket.io伺服器所發送的訊息事件(node-message)之處理器
socketIO.on('node-message', onReceiveMessage);
 
while True:
        print("socketIO_client wait...");
        socketIO.wait(); #Wait forever.
 

