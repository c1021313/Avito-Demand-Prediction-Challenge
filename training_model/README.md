# Avito-Demand-Prediction-Challenge
Kaggle競賽-Avito-Demand-Prediction-Challenge演算法模型建構分享：


## 1. 序言: <br>
由於在Avito拍賣網站上的訓練資料，包括四種格式的特徵值，見以下範例圖片：  <br>  <br>
    * 文字特徵(ex title/description) :  <br>
    * 分類特徵(ex. category_name/parent_category_name/user_type/image_top_1等等) :  <br>
    * 數值特徵(price) :   <br>
    * 圖片特徵(image) :  <br>

![image](https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/Avito商品範例.png)

------

## 2. nn神經網路架構:
 vectors.html
為了要同時將四種形式特徵合併至同一個深度學習神經網路模型之中，我將四種特徵分別做前處理後，使用以下架構構建神經網路架構： <br>

![image](https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/my_nn_structure.png)
  <br>
   * **文字特徵:**  <br>
           1. 經由Fasttext預訓練的詞向量做Embedding <br>
           [Fasttext提供的預先訓練好的詞向量連結](https://fasttext.cc/docs/en/crawl-vectors.html) <br>
           
   >> Facebook FAIR實驗室開源了fastText。 Facebook聲稱fastText比其他學習方法要快得多，能夠訓練模型「在使用標準多核CPU的情況下10分鐘內處理超過10億個詞彙」，fastText能將訓練時間由數天縮短到幾秒鐘。FastText 專註於文本分類。這使得在特別大型的數據集上，它能夠被快速訓練。我們使用一個標準多核 CPU，得到了在10分鐘內訓練完超過10億詞彙量模型的結果。此外， fastText還能在五分鐘內將50萬個句子分成超過30萬個類別。fastText對於許多語言都通用，除了文本分類以外，fastText也能被用來學習詞彙向量表徵。利用其語言形態結構，fastText能夠被設計用來支持包括英語、德語、西班牙語、法語以及捷克語等多種語言 <br>
            2. 載入事前訓練好的CountVectorizer以及TfidfVectorizer替文字特徵做轉換  <br>  <br>
   * **分類特徵:**  <br> 
            1. 使用map轉換為俄文類別  <br>
            2. 做label Encoding <br>  <br>
   * **數值特徵:**   <br> 
            1. 從台幣(NTD) 轉換為俄國盧布 (RUB)  <br>
            2. 並取log <br>  <br>
   * **圖片特徵:**  <br>
            1. 使用上方模型(1)預測出的機率 <br>  
