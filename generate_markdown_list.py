import os
import json
import csv
import yaml
import logging

# Configuración del logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_markdown_list(root_dir):
    markdown_list = []
    keys = [
        "track", "skill", "module", "title", "type", "lang", "sequence",
        "learning", "difficulty", "time", "path", "discord_URL", "slug"
    ]
    config_data = {}

    # Cargar archivos de configuración
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith("_CONFIG.json") and "activities" in subdir:
                file_path = os.path.join(subdir, file)
                config_prefix = os.path.splitext(file_path)[0].rsplit('_', 1)[0]
                config_data[config_prefix] = get_config_content(file_path)

    # Cargar archivos markdown
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(subdir, file)
                track, skill, module = get_levels(file_path, root_dir)
                file_type = get_file_type(file_path, subdir, file)
                config_prefix = os.path.splitext(file_path)[0].rsplit('_', 1)[0]
                additional_info = config_data.get(config_prefix, {
                    "difficulty": None,
                    "learning": None,
                    "time": None,
                    "discord_URL": None
                })

                lang = get_lang(file)
                sequence = get_sequence(subdir, file, file_type)
                title = get_title(file_path, file_type)

                if file_type == "container":
                    titles = get_container_titles(file_path)
                    for i, t in enumerate(titles):
                        lang_key = "ES" if i == 0 else "PT"
                        slug = f"{track}-{skill}-{module}-{t}-{file_type}-{lang_key}".lower().replace(' ', '-')
                        markdown_list.append(create_entry(
                            track, skill, module, t, file_type, lang_key, sequence, additional_info, file_path[2:], slug
                        ))
                else:
                    markdown_list.append(create_entry(
                        track, skill, module, title, file_type, lang, sequence, additional_info, file_path[2:], slug
                    ))

    # Ordenar la lista markdown_list
    markdown_list.sort(key=lambda x: (
        x['track'] or '', 
        x['skill'] or '', 
        x['module'] or '', 
        x['type'] or '', 
        x['sequence'] or ''
    ))


    # Asegurar llaves consistentes
    for entry in markdown_list:
        for key in keys:
            if key not in entry:
                entry[key] = None

    return markdown_list

def create_entry(track, skill, module, title, file_type, lang, sequence, additional_info, path):
    return {
        "track": track,
        "skill": skill,
        "module": module,
        "title": title,
        "type": file_type,
        "lang": lang,
        "sequence": sequence,
        "learning": additional_info.get("learning"),
        "difficulty": additional_info.get("difficulty"),
        "time": additional_info.get("time"),
        "path": path,
        "discord_URL": additional_info.get("discord_URL") if lang == "ES" else additional_info.get("discord_URL_PT")
    }

def get_title(file_path, file_type):
    if file_type in ["activity", "topic"]:
        return get_header(file_path)
    return None

def get_lang(file):
    if file.endswith("_ES.md"):
        return "ES"
    elif file.endswith("_PT.md"):
        return "PT"
    return None

def get_sequence(subdir, file, file_type):
    if file_type in ["activity", "topics", "topic"]:
        return file[:2]
    elif file_type == "container":
        if "activities" in subdir or "topics" in subdir:
            return "00"
        return os.path.basename(subdir)[:2]
    return None

def get_header(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
    return None

def get_container_titles(file_path):
    titles = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("## "):
                titles.append(line[3:].strip())
                if len(titles) == 2:
                    break
    return titles

def get_levels(file_path, root_dir):
    parts = os.path.relpath(file_path, root_dir).split(os.sep)
    if parts[-1].endswith((".md", "_CONFIG.json")):
        parts = parts[:-1]
    return (parts[0] if len(parts) > 0 else None,
            parts[1] if len(parts) > 1 else None,
            parts[2] if len(parts) > 2 else None)

def get_file_type(file_path, subdir, file):
    if file.endswith("_CONFIG.json"):
        return "config"
    if "activities" in subdir and file.endswith(".md") and not file.endswith("README.md"):
        return "activity"
    if "topics" in subdir and file.endswith(".md") and not file.endswith("README.md"):
        return "topic"
    if file.endswith("README.md"):
        return "container"
    return "container"

def get_config_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            logging.debug(f"Config content for {file_path}: {config}")
            return {
                "difficulty": config.get("difficulty"),
                "learning": config.get("learning"),
                "time": config.get("time"),
                "discord_URL": config.get("discord_URL", {}).get("ES"),
                "discord_URL_PT": config.get("discord_URL", {}).get("PT")
            }
    except (json.JSONDecodeError, Exception) as e:
        logging.error(f"Error reading JSON from {file_path}: {e}")
    return {}

def filter_programs(data):
    programs = [entry for entry in data if entry['type'] == 'container' and entry['track'] is not None and entry['skill'] is None and entry['module'] is None]
    logging.info(f"Programs filtered: {programs}")
    return programs

def filter_skills(data):
    skills = [entry for entry in data if entry['type'] == 'container' and entry['track'] is not None and entry['skill'] is not None and entry['module'] is None]
    logging.info(f"Skills filtered: {skills}")
    return skills

def filter_modules(data):
    modules = [
        entry for entry in data
        if entry['type'] == 'container' 
        and entry['track'] is not None 
        and entry['skill'] is not None 
        and entry['module'] is not None 
        and not ("activities" in entry['path'] or "topics" in entry['path'])
    ]
    logging.info(f"Modules filtered: {modules}")
    return modules

def filter_activities(data):
    activities = [
        entry for entry in data
        if entry['type'] == 'activity' 
    ]
    logging.info(f"Activities filtered: {activities}")
    return activities

def filter_topics(data):
    topics = [
        entry for entry in data
        if entry['type'] == 'topic' 
    ]
    logging.info(f"Topics filtered: {topics}")
    return topics

def save_to_csv(data, filename):
    if not data:
        logging.warning(f"No data to write to {filename}")
        return
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    logging.info(f"Data saved to {filename}")

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    logging.info(f"Data saved to {filename}")

def save_to_yaml(data, filename):
    with open(filename, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
    logging.info(f"Data saved to {filename}")

if __name__ == "__main__":
    root_dir = "."
    markdown_list = generate_markdown_list(root_dir)
    
    logging.info(f"Total markdown files: {len(markdown_list)}")
    
    save_to_csv(markdown_list, "markdown_files.csv")
    save_to_json(markdown_list, "markdown_files.json")
    save_to_yaml(markdown_list, "markdown_files.yaml")

    # Filtrar y guardar programas
    programs = filter_programs(markdown_list)
    save_to_csv(programs, "programs.csv")
    save_to_json(programs, "programs.json")
    save_to_yaml(programs, "programs.yml")

    # Filtrar y guardar skills
    skills = filter_skills(markdown_list)
    save_to_csv(skills, "skills.csv")
    save_to_json(skills, "skills.json")
    save_to_yaml(skills, "skills.yml")

    # Filtrar y guardar modulos
    modules = filter_modules(markdown_list)
    save_to_csv(modules, "modules.csv")
    save_to_json(modules, "modules.json")
    save_to_yaml(modules, "modules.yml")

    # Filtrar y guardar actividades
    activities = filter_activities(markdown_list)
    save_to_csv(activities, "activities.csv")
    save_to_json(activities, "activities.json")
    save_to_yaml(activities, "activities.yml")

    # Filtrar y guardar topics
    topics = filter_topics(markdown_list)
    save_to_csv(topics, "topics.csv")
    save_to_json(topics, "topics.json")
    save_to_yaml(topics, "topics.yml")

    logging.info("All files have been saved.")
