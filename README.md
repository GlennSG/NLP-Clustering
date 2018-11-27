# NLP-Clustering
An unsupervised learning approach to classifying authors from 100 different books using text. Extracted and manipulated the text into a sparse matrix using a tfidf vectorizer on a bag of words model created from the 100 different books downloaded from the Project Gutenberg webstie database. Used K-means and Hierarchical clustering to attempt to group the texts by common words, and then attempt to visualize if the clusters reveal a relationship between the chunks of texts and their respective authors. In order to visualize the clusters in 2D, used a couple of dimension reduction techinques, such as T-distributed stochastic neighbor embedding (TSNE) and Multidimensional Scaling (MDS), as well as optimization techniques (elbow method and silhouette score) to find the optimal number of clusters. 

The unsupervised learning models were able to cluster the texts into meaningful groups that could then be paired to a particular author. It's hard to see which author wrote a chunk of text in K-means cluster graphs, but K-means was still useful in figuring out which author was most likely to write a certain chunk of text using a DataFrame. The best visual that provided a more meaningful distinction between texts by author was the ward hierarchical model. You can clearly see how the authors are grouped by the clusters. 

Preprocessing Link:
Project Link:
