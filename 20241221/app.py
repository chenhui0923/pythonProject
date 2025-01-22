from flask import Flask, render_template, jsonify, request
import pandas as pd
import random
# 打包pyinstaller --onefile --windowed  --add-data "static/*;static" --add-data "templates/*;templates" app.py
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
    if len(unique_tables) < 10:
        return jsonify({'error': '剩余桌号不足，无法抽取10个桌号'})
    perfect_tables = random.sample(list(unique_tables), 10)
    # 分5次返回结果，每次2个桌号
    result = [perfect_tables[i:i+2] for i in range(0, 10, 2)]
    # 从数据集中移除已经抽取的桌号
    data = [item for item in data if item['桌号'] not in perfect_tables]
    return jsonify({'perfect_tables': result})

@app.route('/draw_perfect_number', methods=['POST'])
def draw_perfect_number():
    global data
    perfect_number = random.sample(data, 35)
    data = [item for item in data if item not in perfect_number]
    return jsonify({'perfect_number': [perfect_number[i:i+5] for i in range(0, 35, 5)]})

@app.route('/draw_healthy', methods=['POST'])
def draw_healthy():
    global data
    healthy_winners = random.sample(data, 20)
    data = [item for item in data if item not in healthy_winners]
    return jsonify({'healthy_winners': [healthy_winners[i:i+5] for i in range(0, 20, 5)]})

@app.route('/draw_happy', methods=['POST'])
def draw_happy():
    global data
    happy_winners = random.sample(data, 10)
    data = [item for item in data if item not in happy_winners]
    return jsonify({'happy_winners': [happy_winners[i:i+2] for i in range(0, 10, 2)]})

@app.route('/draw_joy', methods=['POST'])
def draw_joy():
    global data
    joy_winners = random.sample(data, 5)
    data = [item for item in data if item not in joy_winners]
    return jsonify({'joy_winners': [joy_winners[i:i+1] for i in range(0, 5, 1)]})

@app.route('/draw_first', methods=['POST'])
def draw_first():
    global data
    first_winners = random.sample(data, 3)
    data = [item for item in data if item not in first_winners]
    return jsonify({'first_winners': [first_winners[i:i+1] for i in range(0, 3, 1)]})

@app.route('/draw_special', methods=['POST'])
def draw_special():
    global data
    special_winner = random.choice(data)
    data = [item for item in data if item != special_winner]
    return jsonify({'special_winner': special_winner})

if __name__ == '__main__':
    app.run(debug=True)