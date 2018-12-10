# Avito-Demand-Prediction-Challenge
## 一、專案計畫概述	

### 1. 專案主軸 : [QUICK SELL - 商品預測成交機率系統](http://103-quicksell.iii.wpj.tw:1337/ "去預測看看")

<br>

   [Avito Demand Prediction Challenge](https://www.kaggle.com/c/avito-demand-prediction)為大數據競賽平台Kaggles的眾多題目之一。Avito為俄羅斯最大的分類廣告(產品)網站，該競賽希望能藉由該網站所提供之產品廣告相關訊息來預測廣告產品之需求

  其競賽方式為藉由平台所提供之資料集包含照片、文字敘述、產品名稱等眾多資料，加以訓練，用以預測該項產品之成交機率。

<br>

-------


### 2. 專案目標

  藉由該數據分析競賽所提供之相關數據資料集，經實際操作、演練大數據分析及架構各式深度學習演算法；撰寫一套網站架構式之分析及預測廣告產品成交機率系統。

  本專案預計將以各式深度學習演算法之集成締結模型來針對資料集提供訓練，並對日後網站使用者所給予之資料進行立即性的成交機率預測，該預測結果為該使用者所提供之網路商品資訊其所預測出該項廣告商品的網路成交機率。並可依不同參數供使用者自行調整，以達最佳化網路銷售成交機率。

-------

### 3. 專案流程

<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/6.png" width=70%/> 
</p>

<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/7.jpg" width=85%/> 
</p>


<br><br>


-------



<br><br><br>

## 二、演算法模型
### 1. 神經網路模型架構：
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/my_nn_structure.png" width=85%/> 
</p>

### 2. 模型架構構想：
<br>

  為了要同時將四種形式(文字text/分類categorical/數值numerical/圖片image)特徵合併至同一個深度學習神經網路模型之中，我將四種特徵分別做前處理後，並串連在一起，再使用如上圖中架構之神經網路模型以進行模型訓練，並輸出訓練完成的模型權重，以利為後續重新使用並讀取模型，供系統使用來預測商品成交機率。

詳細演算法流程，請參考[training_model/README.md](https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/training_model/README.md)檔案

<br><br>


-------



<br><br><br>

## 三、UI呈現 

### [QUICK SELL - 商品預測成交機率系統網站連結](http://103-quicksell.iii.wpj.tw:1337/ "去預測看看")


### 圖1. QUICK-SELL 成交機率系統網站首頁：
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/ui_1.png" width=85%/> 
</p>

<br><br>


### 圖2. 輸入頁面，使用者輸入其所需預測之商品資訊(商品標題/所屬分類/分類細項/價格/描述/圖片)
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/ui_2.png" width=85%/> 
</p>

<br><br>


### 圖3.  使用者輸入資訊傳入後端，經過上述之模型進行成交機率預測，並回傳至UI介面給使用者。
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/ui_3.png" width=85%/> 
</p>

