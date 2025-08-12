from converter import markdown_to_html_node
import re
import os

def extract_title(markdown):
    match = re.search(r'<h1>(.*?)</h1>', markdown)
    if match:
        title = match.group(1)
        return title.strip()
    else:
        raise Exception("No Title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        file_data = f.read()
        f.close()
    
    with open(template_path, 'r') as f:
        template_data = f.read()
        f.close

    node = markdown_to_html_node(file_data)
    html_str = node.to_html()
    title = extract_title(html_str)
    
    final_html = template_data.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_str)

    dst_dir = os.path.dirname(dest_path)
    if dst_dir != '':
        os.makedirs(dst_dir, exist_ok=True)
    
    with open(dest_path, 'w') as f:
        f.write(final_html)
        f.close()
