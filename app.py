from flask import Flask, render_template
import random

app = Flask(__name__)

# 문제 데이터 리스트 (총 14개)
QUIZ_LIST = [
    {
        "code": 'print("3 + 2 =", 3 + 2)',
        "answer": '3 + 2 = 5'
    },
    {
        "code": 'print("Hello" + "World")',
        "answer": 'HelloWorld'
    },
    {
        "code": 'print(len("Python"))',
        "answer": '6'
    },
    {
        "code": 'print(10 // 3)',
        "answer": '3'
    },
    {
        "code": 'print("Python"[0])',
        "answer": 'P'
    },
    {
        "code": 'print("Python".lower())',
        "answer": 'python'
    },
    {
        "code": 'print([1, 2, 3][1])',
        "answer": '2'
    },
    {
        "code": 'print(2 ** 3)',
        "answer": '8'
    },
    {
        "code": 'print(bool(""))',
        "answer": 'False'
    },
    {
        "code": 'print(bool("0"))',
        "answer": 'True'
    },
    {
        "code": 'print(7 % 3)',
        "answer": '1'
    },
    {
        "code": 'print(",".join(["a", "b", "c"]))',
        "answer": 'a,b,c'
    },
    {
        "code": 'print(list("abc"))',
        "answer": "['a', 'b', 'c']"
    },
    {
        "code": 'print(type(3.14))',
        "answer": "<class 'float'>"
    }
]

@app.route("/")
def index():
    quiz = random.choice(QUIZ_LIST)  # 무작위 문제 선택
    return render_template("index.html", quiz=quiz)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

