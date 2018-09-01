
# coding: utf-8

# In[ ]:


url_dict = {
    # Anderson (9)
    "Anderson":[
        "http://www.gutenberg.org/cache/epub/41064/pg41064.txt",
        "http://www.gutenberg.org/cache/epub/32436/pg32436.txt",
        "http://www.gutenberg.org/cache/epub/30971/pg30971.txt",
        "http://www.gutenberg.org/cache/epub/51650/pg51650.txt",
        "http://www.gutenberg.org/cache/epub/51184/pg51184.txt",
        "http://www.gutenberg.org/cache/epub/22239/pg22239.txt",
        "http://www.gutenberg.org/cache/epub/31501/pg31501.txt",
        "http://www.gutenberg.org/cache/epub/37653/pg37653.txt",
        "http://www.gutenberg.org/cache/epub/29542/pg29542.txt"
    ],
    # Ashwell (1)
    "Ashwell":[
        "http://www.gutenberg.org/cache/epub/30427/pg30427.txt"
    ],
    # Beck (1)
    "Beck":[
        "http://www.gutenberg.org/cache/epub/23868/pg23868.txt"
    ],
    # Breuer (1)
    "Breuer":[
        "http://www.gutenberg.org/cache/epub/29060/pg29060.txt"
    ],
    # Buckner (1)
    "Buckner":[
        "http://www.gutenberg.org/cache/epub/27053/pg27053.txt"
    ],
    # Budrys (7)
    "Budrys":[
        "http://www.gutenberg.org/cache/epub/30828/pg30828.txt",
        "http://www.gutenberg.org/cache/epub/26191/pg26191.txt",
        "http://www.gutenberg.org/cache/epub/40968/pg40968.txt",
        "http://www.gutenberg.org/cache/epub/51589/pg51589.txt",
        "http://www.gutenberg.org/cache/epub/34420/pg34420.txt",
        "http://www.gutenberg.org/cache/epub/22967/pg22967.txt",
        "http://www.gutenberg.org/cache/epub/51726/pg51726.txt"
    ],
    # Clifton (8)
    "Clifton":[
        "http://www.gutenberg.org/cache/epub/32181/pg32181.txt",
        "https://www.gutenberg.org/files/27595/27595-0.txt",
        "http://www.gutenberg.org/cache/epub/32131/pg32131.txt",
        "http://www.gutenberg.org/cache/epub/36867/pg36867.txt",
        "http://www.gutenberg.org/cache/epub/22513/pg22513.txt",
        "http://www.gutenberg.org/cache/epub/50935/pg50935.txt",
        "https://www.gutenberg.org/files/38287/38287-0.txt",
        "http://www.gutenberg.org/cache/epub/32833/pg32833.txt"
    ],
    # Cogan (2)
    "Cogan":[
        "http://www.gutenberg.org/cache/epub/51081/pg51081.txt",
        "http://www.gutenberg.org/cache/epub/51136/pg51136.txt"
    ],
    # Del Rey (10)
    "Del Rey":[
        "http://www.gutenberg.org/cache/epub/51046/pg51046.txt",
        "http://www.gutenberg.org/cache/epub/19471/pg19471.txt",
        "http://www.gutenberg.org/cache/epub/30234/pg30234.txt",
        "https://www.gutenberg.org/files/50103/50103-0.txt",
        "http://www.gutenberg.org/cache/epub/50876/pg50876.txt",
        "http://www.gutenberg.org/cache/epub/31286/pg31286.txt",
        "http://www.gutenberg.org/cache/epub/32395/pg32395.txt",
        "http://www.gutenberg.org/cache/epub/51168/pg51168.txt",
        "http://www.gutenberg.org/cache/epub/20212/pg20212.txt",
        "http://www.gutenberg.org/cache/epub/51814/pg51814.txt"
    ],
   # Fyfe (10)
    "Fyfe":[
        "http://www.gutenberg.org/cache/epub/51866/pg51866.txt",
        "http://www.gutenberg.org/cache/epub/32637/pg32637.txt",
        "http://www.gutenberg.org/cache/epub/22346/pg22346.txt",
        "http://www.gutenberg.org/cache/epub/30901/pg30901.txt",
        "http://www.gutenberg.org/cache/epub/29936/pg29936.txt",
        "http://www.gutenberg.org/cache/epub/29994/pg29994.txt",
        "http://www.gutenberg.org/cache/epub/32592/pg32592.txt",
        "http://www.gutenberg.org/cache/epub/40961/pg40961.txt",
        "http://www.gutenberg.org/cache/epub/32764/pg32764.txt",
        "http://www.gutenberg.org/cache/epub/29989/pg29989.txt"
    ],
  # Garrett (10)
    "Garrett":[
        "http://www.gutenberg.org/cache/epub/23561/pg23561.txt",
        "http://www.gutenberg.org/cache/epub/24436/pg24436.txt",
        "http://www.gutenberg.org/cache/epub/30742/pg30742.txt",
        "http://www.gutenberg.org/cache/epub/30583/pg30583.txt",
        "http://www.gutenberg.org/cache/epub/28643/pg28643.txt",
        "http://www.gutenberg.org/cache/epub/23764/pg23764.txt",
        "http://www.gutenberg.org/cache/epub/24005/pg24005.txt",
        "http://www.gutenberg.org/cache/epub/24707/pg24707.txt",
        "http://www.gutenberg.org/cache/epub/25234/pg25234.txt",
        "http://www.gutenberg.org/cache/epub/24064/pg24064.txt"
    ],
  # Leiber (10)
    "Leiber":[
        "http://www.gutenberg.org/cache/epub/51152/pg51152.txt",
        "http://www.gutenberg.org/cache/epub/50819/pg50819.txt",
        "http://www.gutenberg.org/cache/epub/51549/pg51549.txt",
        "http://www.gutenberg.org/cache/epub/22579/pg22579.txt",
        "http://www.gutenberg.org/cache/epub/51436/pg51436.txt",
        "http://www.gutenberg.org/cache/epub/51082/pg51082.txt",
        "http://www.gutenberg.org/cache/epub/23164/pg23164.txt",
        "http://www.gutenberg.org/cache/epub/51353/pg51353.txt",
        "http://www.gutenberg.org/cache/epub/51493/pg51493.txt",
        "http://www.gutenberg.org/cache/epub/51530/pg51530.txt"
    ],
  # Reynolds (10)
    "Reynolds":[
        "http://www.gutenberg.org/cache/epub/24749/pg24749.txt",
        "http://www.gutenberg.org/cache/epub/23194/pg23194.txt",
        "http://www.gutenberg.org/cache/epub/29940/pg29940.txt",
        "http://www.gutenberg.org/cache/epub/51799/pg51799.txt",
        "http://www.gutenberg.org/cache/epub/30338/pg30338.txt",
        "http://www.gutenberg.org/cache/epub/24247/pg24247.txt",
        "http://www.gutenberg.org/cache/epub/29206/pg29206.txt",
        "http://www.gutenberg.org/cache/epub/26741/pg26741.txt",
        "http://www.gutenberg.org/cache/epub/27393/pg27393.txt",
        "http://www.gutenberg.org/cache/epub/24370/pg24370.txt"
    ],
  # Wells (10)
    "Wells":[
        "http://www.gutenberg.org/cache/epub/11870/pg11870.txt",
        "http://www.gutenberg.org/cache/epub/456/pg456.txt",
        "http://www.gutenberg.org/cache/epub/1013/pg1013.txt",
        "http://www.gutenberg.org/cache/epub/11696/pg11696.txt",
        "http://www.gutenberg.org/cache/epub/159/pg159.txt",
        "http://www.gutenberg.org/cache/epub/12750/pg12750.txt",
        "https://www.gutenberg.org/files/27365/27365-0.txt",
        "https://www.gutenberg.org/files/35/35-0.txt",
        "https://www.gutenberg.org/files/1743/1743-0.txt",
        "https://www.gutenberg.org/files/36/36-0.txt"
    ],
  # Williams (9)
    "Williams":[
        "http://www.gutenberg.org/cache/epub/29240/pg29240.txt",
        "http://www.gutenberg.org/cache/epub/50138/pg50138.txt",
        "http://www.gutenberg.org/cache/epub/32563/pg32563.txt",
        "http://www.gutenberg.org/cache/epub/52009/pg52009.txt",
        "http://www.gutenberg.org/cache/epub/32683/pg32683.txt",
        "http://www.gutenberg.org/cache/epub/32696/pg32696.txt",
        "http://www.gutenberg.org/cache/epub/49779/pg49779.txt",
        "http://www.gutenberg.org/cache/epub/32359/pg32359.txt",
        "http://www.gutenberg.org/cache/epub/31948/pg31948.txt"
    ],
  # Zagat (1)
    "Zagat":[
        "http://www.gutenberg.org/cache/epub/29322/pg29322.txt"
    ]
}

