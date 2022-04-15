# FanFicVsClassicLiterature
- /data: includes the files that we used for our analysis.  
        - fanfics_raw.csv: the raw fanfics, their ids and their label.  
        - classics_raw.csv: the raw read in files from the classics. 
        - classics_clean.csv: the preprocessed classics files. 
        - /classic_literature: the text files, separated by id of the Project Gutenberg texts.  
        - /fanfiction: the text files, separated by id of the Archive of Our Own texts.  
        
- /resources: Useful code/examples

- DC_Project_ClassicsVsFanfiction_Preprocessing.ipynb: Read corpus of Fanfictions and Classics from .txt files and preprocess them with Spark NLP Models to get the cleaned tokens.

- DC_Project_ClassicsVsFanfiction_ProtagonistDevelopment_pipeline.ipynb: In classic coming of age literature we expect to see the protagonist evolve throughout the book. This pipeline uses technical approaches to determine whether we observe this trend in classic literature and whether this same protagonist development is present in fanfictions. 

- DC_Project_ClassicsVsFanfiction_Sentiment.ipynb: Sentiment Analysis for Fanfictions and Classics with Spark NLP pre-trained models. The predominant sentiment (joy, anger, surprise, etc.) is obtained for each of the books and the overall sentiments present in Fanfictions and Classics are compared.

- DC_Project_ClassicsVsFanfiction_Sentiment_2.ipynb: Finds the Standardized Afinn Score for tone of the books, and classifies if the books are racist, sexist or neutral.

- DC_Project_ClassicsVsFanfiction_TFIDF_pipeline.ipynb: This pipeline applies map-reduce approaches to compute the TF-IDF values for the texts. These values are then analyzed to study how the representation of women differs between classic literature and modern fanfictions.

- LDA Algorithm Spark.ipynb: looking at the full text of the classics file and understanding most frequent topics by count.

- LDA Algorithm.ipynb: looking at classics by lines and understanding most frequent topics by count.

- LDA Classics Algorithm.ipynb: looking at most frequent topics among classics by lines and term weights

- LDA FanFic Algorithm.ipynb: looking at most frequent topics by count among fanfics

- LDA FanFic Algorithm Spark.ipynb: looking at the full text of the fanfics file and understanding most frequent topics by count

- Removing Proper Nouns FanFic.ipynb: removing the proper nouns from fanfics file and looking at the algorithm results by term weights

- Removing Proper Nouns.ipynb: removing the proper nouns from classics file and looking at the algorithm results by term weights.

- Remove Proper Nouns.ipynb: prototype of the removing nouns algorithm
