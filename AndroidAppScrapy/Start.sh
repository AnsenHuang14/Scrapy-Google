 #!/bin/bash
date1=$(date +%Y%m%d) 
python GenerateURL.py 
scrapy crawl App_Spider -a path=./URL/en.txt -o ./Output/${date1}_en.json

