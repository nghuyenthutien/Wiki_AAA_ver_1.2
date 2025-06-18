import os

def generate_sidebar_markdown():
    # Lấy thư mục chứa file .py hiện tại
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    entries = []
    for filename in sorted(os.listdir(current_dir)):
        if filename.endswith(".md") and filename != "_sidebar.md":
            title = filename[:-3].replace("_", " ").title()
            entries.append(f"* [{title}]({filename})")
    
    return "\n".join(entries)

# In ra kết quả để bạn copy dán vào _sidebar.md
print(generate_sidebar_markdown())
