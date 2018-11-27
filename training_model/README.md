# Avito-Demand-Prediction-Challenge
Kaggle競賽-Avito-Demand-Prediction-Challenge演算法模型建構分享： <br> <br> <br>


## 1. 序言: <br>
由於在Avito拍賣網站上的訓練資料，包括四種格式的特徵值，見以下範例圖片：  <br>  <br>
    * 文字特徵(ex title/description) :  <br>
    * 分類特徵(ex. category_name/parent_category_name/user_type/image_top_1等等) :  <br>
    * 數值特徵(price) :   <br>
    * 圖片特徵(image) :  <br>

<img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/Avito商品範例.png" width=120%/> <br>

  
------ 
<br> <br> <br>
  
  
## 2. nn神經網路架構:
 vectors.html
為了要同時將四種形式特徵合併至同一個深度學習神經網路模型之中，我將四種特徵分別做前處理後，使用以下架構構建神經網路模型以進行模型訓練，詳細特徵前處理方式請參考以下內容： <br>

![image](https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/my_nn_structure.png)
  <br>
### a.文字特徵:  <br>

           1. 經由Fasttext預訓練的詞向量做Embedding
              [Fasttext提供的預先訓練好的詞向量連結](https://fasttext.cc/docs/en/crawl-vectors.html)
           
                    > Facebook FAIR實驗室開源了fastText。 Facebook聲稱fastText比其他學習方法要快得多，
                      能夠訓練模型「在使用標準多核CPU的情況下10分鐘內處理超過10億個詞彙」，fastText能將訓練時間由數天縮短到幾秒鐘。

                      我們使用一個標準多核 CPU，得到了在10分鐘內訓練完超過10億詞彙量模型的結果。
                      此外，fastText還能在五分鐘內將50萬個句子分成超過30萬個類別。
                 
                      fastText對於許多語言都通用，除了文本分類以外，fastText也能被用來學習詞彙向量表徵。利用其語言形態結構，
                      fastText能夠被設計用來支持包括英語、德語、西班牙語、法語以及捷克語等多種語言。
                 
                      FastText引入了subword n-gram的概念來解決詞形變化(morphology)的問題。直觀上，它將一個單詞打散到字符級別，
                      並且利用字符級別的n-gram信息來捕捉字符間的順序關係，希望能夠以此豐富單詞內部更細微的語義。我們知道，
                      西方語言文字常常通過前綴、後綴、字根來構詞，漢語也有單字表義的傳統，所以這樣的做法聽起來還是有一定的道理。
                      举个例子。对于一个单词“google”，为了表达单词前后边界，我们加入<>两个字符，即变形为“詞袋模型不能考慮詞之間的順序，
                      因此 fastText 還加入了 N-gram 特徵。“我 愛 她” 這句話中的詞袋模型特徵是 “我”，“愛”, “她”。這些特徵和句子 
                      “她 愛 我” 的特徵是一樣的。如果加入 2-Ngram，第一句話的特徵還有 “我-愛” 和 “愛-她”，這兩句話 “我 愛 她” 和 
                      “她 愛 我” 就能區別開來了。當然啦，為了提高效率，我們需要過濾掉低頻的 N-gram。

<div style="text-align: center"> <img src="https://camo.githubusercontent.com/4120cfa3f075b4820e2c933f9baad490bef2c64e/687474703a2f2f69322e62616e6771752e636f6d2f6a2f6e6577732f32303138303630362f3734396132323135323832353736333231363653353137332e706e67" width=80%/> 
</div>

            2. 分別各經過兩層GRU層
            
                    > GRU介紹：
                      GRU（Gate Recurrent Unit）是循環神經網絡（Recurrent Neural Network, RNN）的一種。
                      和LSTM（Long-Short Term Memory）一樣，也是為了解決長期記憶和反向傳播中的梯度等問題而提出來的。
                      我們在我們的實驗中選擇GRU是因為它的實驗效果與LSTM相似，但是更易於計算。
                      GRU淺析2.1 GRU的輸入輸出結構GRU的輸入輸出結構與普通的RNN是一樣的。
                      有一個當前的輸入，和上一個節點傳遞下來的隱狀態（hidden state），這個隱狀態包含了之前節點的相關信息。
                      結合和，GRU會得到當前隱藏節點的輸出和傳遞給下一個節點的隱狀態
<div style="text-align: center"> <img src="https://i1.read01.com/SIG=7je5e5/304932354d336f595442.jpg" width=80%/> 
</div>



                    
### b. 分類特徵:  <br> 
            1. 使用map轉換為俄文類別 
            2. 做label Encoding 
### c. 數值特徵:   <br> 
            1. 從台幣(NTD) 轉換為俄國盧布 (RUB) 
            2. 並取log 
### d. 圖片特徵:  <br>
            1. 使用上方模型(1)預測出的機率 
