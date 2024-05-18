# Japanese Hiragana Handwriting Recognition
AI Keywords: computer vision, recognition, LSTM, CNN, RNN

We want to realize sentence recognition on the handwriting of 71 basic Japanese Hiraganas. The ETL database contains character classes with diacritical marks  - ゛and ゜only for Hiraganas. The diacritical marks are crucial for forming a Japanese sentence, such as ち vs ぢ, in order to form a sentence like はちみつがすきです (“I like honey”). The character recognition model will be majorly built with CNN. For sentence recognition, we would like to train 1) an LSTM model based on the Tesseract 2) Transformer model 3) Object detection to box single characters and infer the classes using the single character model.

Data source: ETL8, ETL9 from ETL Database (http://etlcdb.db.aist.go.jp/)
We cannot distribute our data due to the database's requirement. You can, however, download the data freely from the official source.
