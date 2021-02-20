import collections
from typing import Counter
from flask import Flask, request, jsonify
import re

app = Flask(__name__)



@app.route('/getnumbers', methods=['POST'])
def getfile():
    file = request.files['file']
    r= file.read()
    # Decoding bytes to utf-8
    r = r.decode("utf-8")
    # Remove the leading spaces and newline character
    line = r.strip()
    # Convert the characters in line to lowercase to avoid case mismatch 
    line = r.lower()
    words = r.split()

    there= sum(1 for match in re.finditer(r"\bthere\b", r))
    the = sum(1 for match in re.finditer(r"\bthe\b", r))
    this = sum(1 for match in re.finditer(r"\bthis\b", r))
    details = [
        {"there":there,"the":the,"this":this}
    ]
    

    return jsonify(details)

app.run(port=6000)
