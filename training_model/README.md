# Avito-Demand-Prediction-Challenge
Kaggle競賽-Avito-Demand-Prediction-Challenge演算法模型建構分享


## 1. 序言: <br>
由於在Avito拍賣網站上的訓練資料，包括四種格式的特徵值，見以下範例圖片：  <br>  <br>
    * 文字特徵(ex title/description) :  <br>
    * 分類特徵(ex. category_name/parent_category_name/user_type/image_top_1等等) :  <br>
    * 數值特徵(price) :   <br>
    * 圖片特徵(image) :  <br>

![image](https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/Avito商品範例.png)

------
 <br>
## 1. nn神經網路架構:
 
為了要同時將四種形式特徵合併至同一個深度學習神經網路模型之中，我將四種特徵分別做前處理後，使用以下架構構建神經網路架構： <br>

![image](https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/my_nn_structure.png)



