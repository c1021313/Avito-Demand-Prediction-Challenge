# QUICK SELL - 商品預測成交機率系統
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
<br><br><br>


-------


## 二、演算法模型
### 1. 神經網路模型架構：
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/my_nn_structure.png" width=85%/> 
</p>

### 2. 模型架構構想：
<br>

  為了要同時將四種形式(文字text/分類categorical/數值numerical/圖片image)特徵合併至同一個深度學習神經網路模型之中，我將四種特徵分別做前處理後，並串連在一起，再使用如上圖中架構之神經網路模型以進行模型訓練，並輸出訓練完成的模型權重，以利為後續重新使用並讀取模型，供系統使用來預測商品成交機率。

詳細演算法流程，請參考[training_model/README.md](https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/training_model/README.md)檔案

<br><br>
<br><br><br>


-------


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

<br><br><br>

-------


## 四、網頁伺服器整合架構分析

<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/前端架構.png" width=85%/> 
</p>

### 1. 前端網頁

#### · 網頁呈現
 
主要以HTML5 ,CSS ,JavaScript ,Jquery,等程式語言建構前端網頁；而當中又以兩大主要功能為主要目標，其一為運算成果呈現、二為使用者體驗。


#### · 運算成果呈現
   

內含兩個項目，一為輸入圖像呈現，即使用者上傳之商品圖像；另一為總體成果分析，內含商品預測之成交機率及圖像辨識率；預測之成交機率可供使用者參考是否需精進或更改其文字端輸入資料，圖像辨識率之功能亦同。

 

#### · 使用者體驗

內含兩個項目，一為文字辨識，即非圖像資料之輸入，用以提供後台模型進行總體結果預測，其中包含以下項目: 商品名稱、商品種類、商品價格、商品描述。另一為靜態圖像辨識，即圖像資料之輸入，用以提供後台模型進行圖像辨識度之計算。


<br><br>

### 2. 後端網頁伺服器

後端伺服器 : 主要以Node.js程式語言撰寫後端伺服器之功能，其中包含三大功能，分別為:


#### · 網頁呈現

  接收前端網頁資料並回傳該預測結果


#### · 資料庫系統

銜接MySQL資料庫系統，將使用者輸入之資料儲存，以供日後精進模型之預備 資料  

#### · 模型運算

  啟動模型運算之Python程式，用以計算總體預測結果及圖像辨識度

<br><br><br>

-------

## 五、Aws雲端大數據平台架設
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/雲端系統架構.png" width=85%/> 
</p>

本專案伺服器的選擇，我們針對各個面向，考量了各種不同的因素，最後使用了目前的AWS雲端伺服器，茲分別說明如下:
#### 1. 伺服器架設:本地端或雲端
架設在雲端上可避免如果未來需要更大量的運算或是空間，可以直接線上升級租賃的伺服器設備之等級，而不用再額外購入機台或是設備，如此一來可以節省人力資源與設備維護的成本。
我們可以隨時依據使用的流量或需求，來調整伺服器等級，避免成本的浪費。
<br>

#### 2. 作業系統選擇:Windows或Linux
由於架設在雲端上的伺服器，主要處理為網頁回應與程式運算，並不需要圖形化的顯示與操作介面，因此我們採用Linux系統以節省伺服器的硬碟容量與增進運算效能。
<br>

#### 3. 雲端伺服器供應商選擇:Amazon/Microsoft/Google
目前市面上主要提供雲端機台架設的供應商，主要為Amazon的AWS，Microsoft的Azure與Google的GCP，經過我們逐一試用後，發現在穩定性、操作彈性、安全性、使用經驗上，AWS皆較為突出，因此最後我們決定採用AWS來架設雲端伺服器。

<br><br>

<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/8.png" width=85%/> 
</p>
