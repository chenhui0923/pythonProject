from flask import Flask, render_template, jsonify, request
import pandas as pd
import random
import json

app = Flask(__name__)

# 读取Excel文件
def load_data():
    df = pd.read_excel('新建 Microsoft Excel 工作表(4).xlsx')
    return df.to_dict(orient='records')

# 初始化数据
data = load_data()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw_lucky', methods=['POST'])
def draw_lucky():
    global data
    lucky_number = random.randint(1, 12)
    return jsonify({'lucky_number': lucky_number})

@app.route('/draw_perfect', methods=['POST'])
def draw_perfect():
    global data
    unique_tables = set(item['桌号'] for item in data)
    perfect_tables = random.sample(list(unique_tables), 5)
    # 从数据集中移除这些桌号
    data = [item for item in data if item['桌号'] not in perfect_tables]
    return jsonify({'perfect_tables': perfect_tables})

@app.route('/draw_perfect_number', methods=['POST'])
def draw_perfect_number():
    global data
    perfect_number = random.randint(1, 12)
    data = [item for item in data if item['序号'] != perfect_number]
    return jsonify({'perfect_number': perfect_number})

@app.route('/draw_healthy', methods=['POST'])
def draw_healthy():
    global data
    healthy_winners = random.sample(data, 20)
    for winner in healthy_winners:
        data.remove(winner)
    return jsonify({'healthy_winners': healthy_winners})

@app.route('/draw_happy', methods=['POST'])
def draw_happy():
    global data
    happy_winners = random.sample(data, 10)
    for winner in happy_winners:
        data.remove(winner)
    return jsonify({'happy_winners': happy_winners})

@app.route('/draw_joy', methods=['POST'])
def draw_joy():
    global data
    joy_winners = random.sample(data, 5)
    for winner in joy_winners:
        data.remove(winner)
    return jsonify({'joy_winners': joy_winners})

@app.route('/draw_first', methods=['POST'])
def draw_first():
    global data
    first_winners = random.sample(data, 2)
    for winner in first_winners:
        data.remove(winner)
    return jsonify({'first_winners': first_winners})

@app.route('/draw_special', methods=['POST'])
def draw_special():
    global data
    special_winner = random.choice(data)
    data.remove(special_winner)
    return jsonify({'special_winner': special_winner})

if __name__ == '__main__':
    app.run(debug=True)