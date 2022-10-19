import os

os.system("cd")
os.system("cd Scrapy-Tutorial")
os.system("pipenv install")
os.system("pipenv shell")
os.system("cd crawlertutorial")
os.system("rm test.csv")
os.system("scrapy crawl cellar -o test.csv")
os.system("python3 csv_cleaner_scrapy.py")
os.system("python3 pipe_csv_sheets.py")
os.system("cd ../")

pipenv_subshell.py

scrapy_cmd.py