import csv
import json

#获取aspect列表
with open('mydata.lexicon') as f1:
    line = f1.readline()
    total_list = []
    while line:
        raw_list = line.split()[1:-2]
        split_list = raw_list[-1].split('|')
        raw_list[-1] = split_list[0]
        raw_list.append(split_list[1])                   #ever made
        total_list = total_list + raw_list
        line = f1.readline()
    total_list = list(set(total_list))
print (len(total_list))

#获取item编号信息
csvFile = open("movielens_ItemDict.csv", "r")
reader = csv.reader(csvFile)
item_dict = {}
for item in reader:
    item_dict[item[0]] = item[1]
csvFile.close()

#获得字典
with open("movielens_vocab.json", 'r') as jsonfile:
    vocab_seq = json.load(jsonfile)

num = 0
for aspect in total_list:
    if (aspect in vocab_seq.keys()):
        num = num + 1
    else:
        print (aspect)
print (num)

max_length = 0
min_length = 100
total_length = 0
#抽取故事中的aspect
with open("movielens_abstract_cast.json", 'r') as jsonfile1:
    story_seq = json.load(jsonfile1)
story_list = story_seq['data']
story_dict = {}
for item in story_list:
    modified_story = ''
    for char in item['abstract']:
        if not ((char <= 'z' and char >= 'a') or (char <= 'Z' and char >= 'A')):
            char = ' '
        else:
            char = char.lower()
        modified_story = modified_story + char
    modified_words = modified_story.split()
    modified_words = list(set(modified_words))
    aspect_list = []
    for word in modified_words:
        if word in total_list and word in vocab_seq.keys():   #此处会排除那些不在原实验字典里的词
            aspect_list.append(word)
    if (len(aspect_list) > max_length): max_length = len(aspect_list)
    if (len(aspect_list) < min_length): min_length = len(aspect_list)
    total_length = total_length + len(aspect_list) 
    story_dict[item['item_id']] = aspect_list

average_length = total_length / len(story_list)
print ("max_length = ", max_length)
print ("min_length = ", min_length)
print ("average_length = ", average_length)

#获得新的数据集
with open("movielens_doc_cast.json", 'r') as jsonfile2:
    article_seq = json.load(jsonfile2)
for item in article_seq['doc_info']:
    article_seq['doc_info'][item]['sent'] = story_dict[item_dict[item]]
#f = open('myaspect.json', 'w+', encoding='utf-8')
#json_str = json.dumps(article_seq)
#print(json_str, file = f)
