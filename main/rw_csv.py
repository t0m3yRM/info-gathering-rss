import feedparser
import csv
import os

def rss_parser(rss_url,v1,v2,v3):

    data = feedparser.parse(rss_url)

    res = []

    for entry in data.entries:        
        temp_dic = {}
        temp_dic["date"] = entry.updated
        temp_dic["title"] = entry.title

        if entry.title.find(v1):
            temp_dic["category"] = v1
        elif entry.title.find(v2) :
            temp_dic["category"] = v2
        elif entry.title.find(v3) :
            temp_dic["category"] = v3
        else:
            temp_dic["category"] = "その他"
        temp_dic["link"] = entry.link
        res.append(temp_dic)
    
    return res

def rw_csv(file_path,write_data):
    field_name = ['date','title','category','link']
    if os.path.isfile(file_path):
        with open(file_path,'a',encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = field_name)
            writer.writerows(write_data)
    else:
        with open(file_path,'a',encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = field_name)
            writer.writeheader()
            writer.writerows(write_data)

def main():
    RSS_URL = 'input_rss_url'
    
    data = rss_parser(RSS_URL,"input_category_name","input_category_name","input_category_name")
    file_path = ''

    rw_csv(file_path,data)

if __name__ == "__main__":
    main()
    




