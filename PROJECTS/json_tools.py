import json

def load_json(path):
    """读取 JSON 文件，返回解析后的数据；出错返回 None"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"文件不存在：{path}")
        return None
    except json.JSONDecodeError:
        print(f"JSON 解码错误：{path}")
        return None

def save_json(path, data):
    """把数据（dict/list）保存为 JSON 文件"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def pretty(data):
    """格式化打印 JSON 数据"""
    print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    # 测试 load_json（读）
    data = load_json("example.json")
    print("读到的数据:", data)

    # 测试 save_json（写）
    test_data = {"name": "小明", "age": 18, "hobbies": ["篮球", "吉他"]}
    save_json("output.json", test_data)
    print("已保存 output.json")

    # 测试 pretty（格式化打印）
    pretty(test_data)