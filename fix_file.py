import os
import re

# Thư mục chứa các file Markdown
folder_path = './'  # hoặc './wiki_of_AAA' nếu trong thư mục con

# Regex để tìm [[...]]
link_pattern = re.compile(r'\[\[([^\[\]]+?)\]\]')

def convert_links(text):
    return link_pattern.sub(lambda m: f'[{m.group(1)}]({m.group(1)}.md)', text)

# Duyệt tất cả các file .md trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith('.md'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = convert_links(content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Đã chuyển đổi trong: {filename}')
