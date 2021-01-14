# Text-Search-engine
Based on Hadoop and Django

Project name: Text search Engine based on Hadoop 

Goal: Retrive text context related to the query and order them according to the relavence.

Major components:
1.Text files collection: uses a static crawler to 62329 books’ data. Then split the text into small files. Also, we downloaded the daily financial news for 6000+ stocks from kaggle.

2.Index and Rank:Using local code, hadoop and lucene to index the crawled text. And use hadoop to calculate the value of TF-IDF. Then use python to sort the TF-IDF values ​​and output the results.

The implement of indexing is used command line. The process is  shown in the report.

3.Web server and interface: to implement web server and interface though djongo


Topics covered： Hadoop, web crawling, text processing, python rank, map-reduce, web frontend and django.

Main language: python, java,command line
group member:     
黄嘉滢 1830026047
宁大智 1830026092
谭腾洋 1830026104

