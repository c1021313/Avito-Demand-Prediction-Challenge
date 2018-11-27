# Avito-Demand-Prediction-Challenge
Kaggle競賽-Avito-Demand-Prediction-Challenge演算法模型建構分享： <br> <br> <br>


## 一、 序言: <br>
由於在Avito拍賣網站上的訓練資料，包括四種格式的特徵值，見以下範例圖片：  <br>  <br>
    * 文字特徵(ex title/description) :  <br>
    * 分類特徵(ex. category_name/parent_category_name/user_type/image_top_1等等) :  <br>
    * 數值特徵(price) :   <br>
    * 圖片特徵(image) :  <br>
    
<p align="center"> 
<img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/Avito商品範例.png" width=80%/></p> <br>

  
------ 
<br> <br> <br>
  
  
## 二、 nn神經網路架構: <br>

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

<p align="center"> <img src="https://camo.githubusercontent.com/4120cfa3f075b4820e2c933f9baad490bef2c64e/687474703a2f2f69322e62616e6771752e636f6d2f6a2f6e6577732f32303138303630362f3734396132323135323832353736333231363653353137332e706e67" width=80%/> 
</p>

            2. title/description分別各經過兩層GRU層
            
                    > GRU介紹：
                      GRU（Gate Recurrent Unit）是循環神經網絡（Recurrent Neural Network, RNN）的一種。
                      和LSTM（Long-Short Term Memory）一樣，也是為了解決長期記憶和反向傳播中的梯度等問題而提出來的。
                      我們在我們的實驗中選擇GRU是因為它的實驗效果與LSTM相似，但是更易於計算。
                      GRU的輸入輸出結構GRU的輸入輸出結構與普通的RNN是一樣的。
                      有一個當前的輸入，和上一個節點傳遞下來的隱狀態（hidden state），這個隱狀態包含了之前節點的相關信息。
                      結合和，GRU會得到當前隱藏節點的輸出和傳遞給下一個節點的隱狀態
                      
                      圖：GRU的輸入輸出結構
<p align="center"> <img src="https://i1.read01.com/SIG=7je5e5/304932354d336f595442.jpg" width=50%/> 
</p>

            3. title/description各別經過一層dense層（dense = dense + dropout + Prelu）
            4. 將title/description做串連concatenate後加入一層dense層dense = dense + dropout + Prelu）
            
<br> <br>                     
### b. 分類特徵:  <br> 
            1. 將分類特徵個別填補空缺值
            2. 做label Encoding
            3. 使用keras Embedding將分類特徵轉做向量化
            
                      > 為什麼要將分類特徵轉換成embedding向量？
                      
                        a. 讓相似分類特徵在高維度向量空間中更能聚合緊密，比起lable encoding更能表達類別與類別之間的關係。
                        b. 可視為one-hot-encoding降維 
                        c. 參考paper資料：
                           https://arxiv.org/pdf/1604.06737.pdf
                           https://www.fast.ai/2018/04/29/categorical-embeddings/
                           https://medium.com/@satnalikamayank12/on-learning-embeddings-for-categorical-data-using-keras-165ff2773fc9
                           
            4. 將embedding之後的分類特徵做concatenate後加入一層dense層（dense = dense + dropout + Prelu）
<br> <br> 
### c. 數值特徵:   <br> 
            1. 將數值特徵個別填補空缺值   
            2. 取log           
            3. 與 d.圖片特徵 concatenate後一同經過一層dense層（dense = dense + dropout + Prelu）
<br> <br> 
### d. 圖片特徵:  <br>

            1. 使用keras提供的預訓練深度學習模型，預測圖片信心指數，將此作為模型的圖片特徵萃取（圖片辨識率/信心程度）
               我們在這邊使用的為其中的inception模型。               
            2. 與 c.數值特徵  concatenate後一同經過一層dense層 （dense = dense + dropout + Prelu）
               
 * keras提供以下幾種[Apretrained model](https://keras.io/applications/)：

<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/keras_pretrained_model.png" width=75%/> 
</p>

<br><br>

#### *  將Avito照片資料集套入inception模型中的效果以及預測結果：<br>      
#### 1. inception模型 "能夠" 準確預測舉例（圖片辨識率/信心程度 > 90%） <br>  
   可以看到清晰的圖片擁有較高的辯視率（光線/角度/是否涵蓋物件全貌） 
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/1.png" width=70%/> 
</p>
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/3.png" width=70%/> 
</p>
 <br>
 

#### 2. inception模型 "無法" 準確預測舉例（圖片辨識率/信心程度 < 10%） <br>  
   可以看到這些的圖片都相當不清晰，因此inception model也無法明確的判斷此圖片，辨識率程度相對低。 
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/2.png" width=70%/> 
</p>
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/4.png" width=70%/> 
</p>
 <br>


#### 3. inception模型對於 "同樣的類別" 的照片比較（圖片辨識率高 > 90% ＆ 圖片辨識率低 < 20%） <br>  
   針對同樣類別的照片(minivan)，可見上方的照片模型相當肯定的判斷為該類別，且**信心程度高**。(圖片辨識率 > 90%) <br>  
   但下方圖片由於拍攝角度. 光線等因素較不清晰，且無法涵蓋圖片全貌，雖然模型判斷得出為minivan類別，但相對**信心程度低**了很多。(圖片辨識率低 < 20%)
<p align="center"> <img src="https://github.com/c1021313/Avito-Demand-Prediction-Challenge/blob/master/img/5.png" width=70%/> 
</p>


