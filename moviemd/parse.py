import re
import sys

def parse_md(file_path):
    with open(file_path + "/main.md", 'r') as f:
        text = f.read()

    # extract image urls
    pattern = r'\((.*?)\)'
    matches = re.findall(pattern, text)
    img_urls = [match.split()[0] for match in matches]

    # extract texts for transcription
    pattern = r'"(.*?)"'
    matches = re.findall(pattern, text)
    text_list = matches
    
    temp = []
    for url in img_urls:
        temp.append(f'{file_path}/{url}')
    
    img_urls = temp

    # log process
    print(img_urls)
    print(text_list)

    return [img_urls, text_list]

if __name__ == "main":
    file_path = sys.argv[1]
    parse_md(file_path)