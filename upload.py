import json


def upload_info(university, program, index, apply, language, other, recommend, start, end):
    data_path = "database/application.json"
    dictionary = get_info()
    pg = {
        'program': program,
        'index': index,
        'apply': apply,
        'language': language,
        'other': other,
        'recommend': recommend,
        'start': start,
        'end': end
    }
    if university not in dictionary.keys():
        dictionary[university] = []
    dictionary[university].append(pg)
    file = open(data_path, "w", encoding="utf-8")
    json.dump(dictionary, file, indent=4, ensure_ascii=False)


def get_info():
    data_path = "database/application.json"
    file = open(data_path, "r", encoding="utf-8")
    dictionary = json.load(file)
    file.close()
    return dictionary
