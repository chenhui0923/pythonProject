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
    unique_tables = list(set(item['桌号'] for item in data))
    print(unique_tables)
    if len(unique_tables) < 2:
        return jsonify({'error': '剩余桌号不足，无法抽取2个桌号'})
    # 每次抽取2个桌号
    selected_tables = random.sample(unique_tables, 2)
    # 从数据集中移除已经抽取的桌号
    data = [item for item in data if item['桌号'] not in selected_tables]
    return jsonify({'perfect_tables': selected_tables})

    # 从数据集中移除已经抽取的桌号
    data = [item for item in data if item['桌号'] not in [table for pair in perfect_tables for table in pair]]
    return jsonify({'perfect_tables': perfect_tables})


@app.route('/draw_perfect_number', methods=['POST'])
def draw_perfect_number():
    global data

    # 检查 data 中是否还有足够的数据可供抽取
    if len(data) < 5:
        return jsonify({"error": "数据不足，无法继续抽取"}), 400

    # 随机抽取5个不重复的数
    perfect_number = random.sample(data, 5)
    # 从原始 data 中移除这5个数
    data = [item for item in data if item not in perfect_number]

    # 返回抽取的5个数
    return jsonify({'perfect_number': perfect_number})

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


# 20抽5
@app.route('/hongbao1', methods=['POST'])
def hongbao1():
    data = load_data()
    hongbao1 = random.sample(data, 20)
    data = [item for item in data if item not in hongbao1]
    return jsonify({'hongbao1': [hongbao1[i:i+5] for i in range(0, 20, 5)]})

# 25抽5
@app.route('/hongbao2', methods=['POST'])
def hongbao2():
    global data
    hongbao2 = random.sample(data, 25)
    data = [item for item in data if item not in hongbao2]
    return jsonify({'hongbao2': [hongbao2[i:i+5] for i in range(0, 25, 5)]})


# 10抽5
@app.route('/hongbao3', methods=['POST'])
def hongbao3():
    global data
    hongbao3 = random.sample(data, 10)
    data = [item for item in data if item not in hongbao3]
    return jsonify({'hongbao3': [hongbao3[i:i+5] for i in range(0, 10, 5)]})

# 12抽2
@app.route('/hongbao4', methods=['POST'])
def hongbao4():
    global data
    hongbao4 = random.sample(data, 12)
    data = [item for item in data if item not in hongbao4]
    return jsonify({'hongbao4': [hongbao4[i:i+2] for i in range(0, 12, 2)]})

# 10抽1
@app.route('/hongbao5', methods=['POST'])
def hongbao5():
    global data
    hongbao5 = random.sample(data, 10)
    data = [item for item in data if item not in hongbao5]
    return jsonify({'hongbao5': [hongbao5[i:i+1] for i in range(0, 10, 1)]})

# 12抽1
@app.route('/hongbao6', methods=['POST'])
def hongbao6():
    global data
    hongbao6 = random.sample(data, 12)
    data = [item for item in data if item not in hongbao6]
    return jsonify({'hongbao6': [hongbao6[i:i+1] for i in range(0, 12, 1)]})


# 20抽1
@app.route('/hongbao7', methods=['POST'])
def hongbao7():
    global data
    hongbao7 = random.sample(data, 20)
    data = [item for item in data if item not in hongbao7]
    return jsonify({'hongbao7': [hongbao7[i:i+1] for i in range(0, 20, 1)]})

if __name__ == '__main__':
    app.run(debug=True)