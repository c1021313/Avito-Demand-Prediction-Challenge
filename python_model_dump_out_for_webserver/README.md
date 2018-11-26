## AWS雲端上LINUX的PYTHON MODEL

### 重點程序分析:
1. 連線LOCAL端的MYSQL，讀取SQL中存取的使用者輸入資料
2. 載入模型(1) 圖片模型 : 使用KERAS PRETRAINED INCEPTION MODEL圖片模型建構，載入權重並預測```diff - (@P2)圖片識別率```。
3. 特徵預處理   <br>

    * 文字特徵(title/description) :  <br>
      1. 從中文翻譯為俄文 <br>
      2. 載入事前訓練好的CountVectorizer以及TfidfVectorizer替文字特徵做轉換  <br>
    * 分類特徵(category_name/parent_category_name) :  <br>
      1. 使用map轉換為俄文類別  <br>
      2. 做label Encoding <br>
    * 數值特徵(price) : 
      1. 從台幣(NTD) 轉換為俄國盧布 (RUB)  <br>
      2. 並取log <br>
    * 圖片特徵(image_confidence) :  <br>
      1. 使用上方模型(1)預測出的機率 <br>        
              
4. 載入模型(2) 總機率模型 : 載入預先訓練好nn/lgbm的模型(請閱training_model訓練模型)，使用以上四類不同型態資料當作輸入並做預測。 <br>
5.

```diff
- this will be highlighted in green
+ this will be highlighted in green
- this will be highlighted in red
```
