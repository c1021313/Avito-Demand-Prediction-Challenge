## AWS雲端上LINUX的PYTHON MODEL

### 重點程序分析:
* 連線LOCAL端的MYSQL，讀取SQL中存取的使用者輸入資料
* 載入模型(1) 圖片模型 : 使用KERAS PRETRAINED INCEPTION MODEL圖片模型建構，載入權重並預測圖片識別率。
* 特徵預處理   <br>
a. 文字特徵(title/description) > 從中文翻譯為俄文，載入事前訓練好的CountVectorizer以及TfidfVectorizer(請閱training_model訓練模型)替文字特徵做轉換 <br>
b. 分類特徵(category_name/parent_category_name) > 使用map轉換為俄文類別並做label Encoding <br>
c. 數值特徵(price) > 從台幣(NTD) 轉換為俄國盧布 (RUB)，並取log <br>
d. 圖片特徵(image_confidence) > 使用上方模型(1)預測出的機率 <br>
              
              
* 載入模型(2) 總機率模型 : 載入預先訓練好nn/lgbm的模型(請閱training_model訓練模型)，使用以上四類不同型態資料當作輸入並做預測。
