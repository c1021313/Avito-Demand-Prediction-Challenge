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

  1. UI       →   NODE.JS ：使用者輸入所需預測之商品資訊（商品圖片/標題/敘述/價格/商品所屬分類）
  2. NODE.JS  →   SQL          ：NODE.JS接收使用者輸入之資料，並存入SQL
  3. NODE.JS  →   PYTHON  ：NODE.JS啟動python檔案（模型）
  4. PYTHON   →  SQL           ：PYTHON讀取SQL資訊並進行前處理
  5. PYTHON   →  NODE.JS.   : PYTHON模型預測成交機率並回傳NODE.JS
  6. NODE.JS   →      UI           : NODE.JS將成交機率傳送至UI呈現給使用者
