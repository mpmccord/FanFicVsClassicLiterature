# FanFicVsClassicLiterature
- /data: includes the files that we used for our analysis.
        - fanfics_raw.csv: the raw fanfics, their ids and their label.
        - classics_raw.csv: the raw read in files from the classics
        - classics_clean.csv: the preprocessed classics files
        - /classic_literature: the text files, separated by id of the Project Gutenberg texts.
        - /fanfiction: the text files, separated by id of the Archive of Our Own texts.
- /resources:
- DC_Project_ClassicsVsFanfiction_Preprocessing.ipynb:
- DC_Project_ClassicsVsFanfiction_Sentiment.ipynb:
- DC_Project_ClassicsVsFanfiction_Sentiment_2.ipynb: Finds the Standardized Afinn Score for tone of the books, and classifies if the books are racist, sexist or neutral.
- DC_Project_ClassicsVsFanfiction_tfidf_pipeline.ipynb:
- proj_gutenberg_read-data.py: Reads all classic files within '\data\classic_literature' and generates a dataframe where each row is one book.
- proj_gutenberg_read-data.ipynb: Jupyter notebook version of 'proj_gutenberg_read-data.py'
- tfidf_pipeline.ipynb: Pipeline to compute and analyze TFIDF values. (set up to for google colab)
- evolution_pipeline.ipynb: Coming-of-age novels are defined by the evolution of the main character from a young girl to a grown woman. This pipeline explores whether we see this same progression in both the literary canon novels and the fanfiction texts.
- LDA Algorithm Spark.ipynb: looking at the full text of the classics file and understanding most frequent topics by count.
- LDA Algorithm.ipynb: looking at classics by lines and understanding most frequent topics by count.
- LDA Classics Algorithm.ipynb: looking at most frequent topics among classics by lines and term weights
- LDA FanFic Algorithm.ipynb: looking at most frequent topics by count among fanfics
- LDA FanFic Algorithm Spark.ipynb: looking at the full text of the fanfics file and understanding most frequent topics by count
- Removing Proper Nouns FanFic.ipynb: removing the proper nouns from fanfics file and looking at the algorithm results by term weights
- Removing Proper Nouns.ipynb: removing the proper nouns from classics file and looking at the algorithm results by term weights.
- Remove Proper Nouns.ipynb: prototype of the removing nouns algorithm
