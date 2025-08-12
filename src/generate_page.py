from converter import markdown_to_html_node
import re
import os
import pathlib

def extract_title(markdown):
    match = re.search(r'<h1>(.*?)</h1>', markdown)
    if match:
        title = match.group(1)
        return title.strip()
    else:
        raise Exception("No Title found")

def generate_html(from_path, template_path, basepath):
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

    final_html = final_html.replace('href="/', 'href="' + basepath)
    final_html = final_html.replace('src="/', 'src="' + basepath)

    return final_html

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    generate_html(from_path,template_path)

    dst_dir = os.path.dirname(dest_path)
    if dst_dir != '':
        os.makedirs(dst_dir, exist_ok=True)
    
    with open(dest_path, 'w') as f:
        f.write(final_html)
        f.close()

def generate_html_from_file(file_path, dst_path, template_path, basepath):
    public_path = dst_path.replace(".md", ".html")
        
    html = generate_html(file_path, template_path, basepath)
    with open(public_path, 'w') as f:
        f.write(html)
        f.close()

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath, content_root=''):
    if content_root == '':
        content_root = dir_path_content
    dir_files = os.listdir(dir_path_content)
    for file in dir_files:
        file_path = f"{dir_path_content}/{file}"
        rel = os.path.relpath(file_path, content_root)
        dst_path = f"{dest_dir_path}/{rel}"
        
        if os.path.isfile(file_path):
            generate_html_from_file(file_path, dst_path, template_path, basepath)
        else:
            os.makedirs(dst_path)
            generate_page_recursive(file_path, template_path, dest_dir_path, basepath, content_root)
