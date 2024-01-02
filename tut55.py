# Multiprocessinng

import multiprocessing
import requests
import concurrent.futures

def downloadFile(url, name):
    print(f"started downloading {name}")
    res = requests.get(url)
    open(f"tut55/file{name}.jpg", "wb").write(res.content)
    print(f"finished downloading {name}")
    
url = "https://picsum.photos/200/300"
pros = []
for i in range(5):
    downloadFile(url, i)
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)
for p in pros:
    p.join()

with concurrent.futures.ProcessPoolExecutor() as executer:
    l1 = [url for i in range(5)]
    l2 = [i for i in range(5)]
    result = executer.map(downloadFile, l1, l2)
    for r in result:
        print(r)