import os
from pathlib import Path
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "app": "flask app",
        "version": "1.0.0",
    }


@app.route("/user/")
def user_list():
    return {
        "app": "flask app",
        "version": "1.0.0",
        "name": "users",
    }


@app.route("/data_passing/")
def data_passing():
    headers = dict(request.headers)
    form = dict(request.form)

    files = request.files
    file = files.get("profile")

    if file:
        uploads = Path("uploads")
        os.makedirs(uploads, exist_ok=True)
        file.save(uploads / file.filename)
        file = {
            "name": file.name,
            "filename": file.filename,
            "mimetype": file.mimetype,
            "headers": dict(file.headers),
            "size": os.stat(uploads / file.filename).st_size,
            "content_type": file.content_type,
        }

    try:
        json = dict(request.json)
    except BaseException as e:
        json = str(e)

    data = request.get_data(as_text=True)
    args = dict(request.args)
    return {
        "app": "my flask app - users",
        "version": "1.0.0",
        "headers": headers,
        "src-Lang": request.headers.get("src-Lang"),
        "Src-Lang": request.headers.getlist("Src-Lang"),
        "form": form,
        "json": json,
        "data": data,
        "args": args,
        "file": file,
    }


"""
- - - line count
- - - word count (total & per line)
- - - unique words & occurrence
- - - unique chars & occurrence
"""


@app.route("/accept_file_process_data/")
def accept_file_process_data():
    data = request.files
    data_ = [line.decode() for line in data["filepath"]]
    no_of_lines = str(len(data_))
    unique_word_dict = {}
    total_word_count = 0
    lines_wordcount = []
    for no, line in enumerate(data_):
        wordlst = line.split()
        line_count = len(wordlst)
        total_word_count += line_count
        for word in wordlst:
            if word not in unique_word_dict:
                unique_word_dict[word] = 1
            else:
                unique_word_dict[word] += 1
        # print(f"Lines and its word count ::: {line}\t{line_count}")
        print(type(line))
        lines_wordcount.append(line_count)

    char_dict = {}
    for line in data_:
        for char in line:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

    print(f"No of lines in file ::: {no_of_lines}")
    print(f"Total No of words in file ::: {total_word_count}")
    print(f"Total No of Uniq words in file ::: {len(unique_word_dict)}")
    print(f"Total No of Uniq chars in file ::: {len(char_dict)}")

    return {
        "no_of_lines": no_of_lines,
        "total_word_count": total_word_count,
        "lines_wordcount": lines_wordcount,
        "unique_word_dict": unique_word_dict,
        "char_dict": char_dict,
    }


app.run(debug=True)
