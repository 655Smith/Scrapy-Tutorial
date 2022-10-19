enter credentials into credentials.json
call pipenv install/shell on \Scrapy Tutorial
cd crawlertutorial
rm test.csv
scrapy crawl cellar -o test.csv
wait, this will take 5 ish minutes
python3 csv_cleaner_scrapy.py
python3 pipe_csv_sheets.py
cd ../
exit

#! /usr/bin/bash
bash pipenv.sh
bash crawler.sh

cd
cd Scrapy-Tutorial
pipenv install
pipenv shell
cd crawlertutorial
rm test.csv
scrapy crawl cellar -o test.csv
python3 csv_cleaner_scrapy.py
python3 pipe_csv_sheets.py
cd ../
exit
