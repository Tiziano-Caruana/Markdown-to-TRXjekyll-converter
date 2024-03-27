import re

def extract_site_url_and_categories_and_title_from_md(filename):
    site_url = None
    categories = None
    title = None
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('categories:'):
                categories = line.strip().split(': ')[1].strip().split('ctf_')[1]
                break
            elif line.startswith('title:'):
                title = line.strip().split('- ')[-1].strip().replace(' ', '-')

    return categories, title

def transform_markdown_file(input_file, output_file):
    CTF, challenge = extract_site_url_and_categories_and_title_from_md(input_file)
    if not (CTF and challenge):
        print("Errore: impossibile estrarre le informazioni necessarie dal file markdown.")
        return
    
    with open(input_file, 'r', encoding='utf-8') as input_file:
        markdown_content = input_file.readlines()

    transformed_content = []
    for line in markdown_content:
        match = re.match(r'!\[(.*)\]\((.*)\)', line)
        if match:
            alt_text = match.group(1)
            image_path_parts = match.group(2).split("/")
            image_path = "/".join(image_path_parts[-2:])
            print("ctf: ", CTF)
            print("challenge: ", challenge)
            src = "{{ site-url }}/assets/" + CTF + "/" + challenge + "/" + image_path
            transformed_line = f'<img class="img-responsive" src="{src}" alt="{alt_text}">'
            transformed_content.append(transformed_line)
        else:
            transformed_content.append(line)

    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.writelines(transformed_content)

input_filename = '[INPUT_NAME].md'
output_filename = '[OUTPUT_NAME].md'
transform_markdown_file(input_filename, output_filename)
