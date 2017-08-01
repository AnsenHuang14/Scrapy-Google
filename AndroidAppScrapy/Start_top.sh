 #!/bin/bash
date1=$(date +%Y%m%d) 
mkdir D:/Github/Scrapy-Google/AndroidAppScrapy/Output/${date1} 
mkdir D:/Github/Scrapy-Google/AndroidAppScrapy/Update/${date1} 
python GenerateURL.py D:/Github/Scrapy-Google/AndroidAppScrapy/PkgNameByNum/1000_.txt

scrapy crawl App_Spider -a path=./URL/ar.txt -o ./Output/${date1}/${date1}_ar.json & \
scrapy crawl App_Spider -a path=./URL/de.txt -o ./Output/${date1}/${date1}_de.json & \
scrapy crawl App_Spider -a path=./URL/en.txt -o ./Output/${date1}/${date1}_en.json & \
scrapy crawl App_Spider -a path=./URL/en_GB.txt -o ./Output/${date1}/${date1}_en_GB.json & \
scrapy crawl App_Spider -a path=./URL/es.txt -o ./Output/${date1}/${date1}_es.json & \
scrapy crawl App_Spider -a path=./URL/fi.txt -o ./Output/${date1}/${date1}_fi.json & \
scrapy crawl App_Spider -a path=./URL/fr.txt -o ./Output/${date1}/${date1}_fr.json & \
scrapy crawl App_Spider -a path=./URL/il.txt -o ./Output/${date1}/${date1}_il.json & \
scrapy crawl App_Spider -a path=./URL/in.txt -o ./Output/${date1}/${date1}_in.json & \
scrapy crawl App_Spider -a path=./URL/it.txt -o ./Output/${date1}/${date1}_it.json & \
scrapy crawl App_Spider -a path=./URL/ja.txt -o ./Output/${date1}/${date1}_ja.json & \
scrapy crawl App_Spider -a path=./URL/ko.txt -o ./Output/${date1}/${date1}_ko.json & \
scrapy crawl App_Spider -a path=./URL/ms.txt -o ./Output/${date1}/${date1}_ms.json & \
scrapy crawl App_Spider -a path=./URL/no.txt -o ./Output/${date1}/${date1}_no.json & \
scrapy crawl App_Spider -a path=./URL/pl.txt -o ./Output/${date1}/${date1}_pl.json & \
scrapy crawl App_Spider -a path=./URL/pt.txt -o ./Output/${date1}/${date1}_pt.json & \
scrapy crawl App_Spider -a path=./URL/ru.txt -o ./Output/${date1}/${date1}_ru.json & \
scrapy crawl App_Spider -a path=./URL/th.txt -o ./Output/${date1}/${date1}_th.json & \
scrapy crawl App_Spider -a path=./URL/tr.txt -o ./Output/${date1}/${date1}_tr.json & \
scrapy crawl App_Spider -a path=./URL/uk.txt -o ./Output/${date1}/${date1}_uk.json & \
scrapy crawl App_Spider -a path=./URL/vi.txt -o ./Output/${date1}/${date1}_vi.json & \
scrapy crawl App_Spider -a path=./URL/za.txt -o ./Output/${date1}/${date1}_za.json & \
scrapy crawl App_Spider -a path=./URL/zh_CN.txt -o ./Output/${date1}/${date1}_zh_CN.json & \
scrapy crawl App_Spider -a path=./URL/zh_TW.txt -o ./Output/${date1}/${date1}_zh_TW.json & 
