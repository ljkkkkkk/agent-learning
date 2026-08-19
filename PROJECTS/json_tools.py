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

def find_by_key(data, key):
    """递归搜索：在嵌套的 dict/list 里找出所有指定 key 的值，返回列表"""
    results = []

    if isinstance(data, dict):                    # 情况 A：data 是字典
        for k, v in data.items():                 # 遍历每个 键k / 值v
            if k == key:                          # 这个键正好是我们要找的？
                results.append(v)                 # 是 → 把值收进结果
            results.extend(find_by_key(v, key))   # 不管是不是，都往「值」深处继续挖
    elif isinstance(data, list):                  # 情况 B：data 是列表
        for item in data:                         # 遍历每个元素
            results.extend(find_by_key(item, key))# 往每个元素深处挖
    # 情况 C：data 是数字/字符串等 → 什么都不做（这就是基线条件！）

    return results

if __name__ == "__main__":
    # 测试 load_json（读）
    data = load_json("example.json")

    # find_by_key 实战：从嵌套数据里挖出所有指定字段
    print("所有公司:", find_by_key(data, "company"))
    print("所有职位:", find_by_key(data, "role"))
    print("学历:", find_by_key(data, "degree"))
    print("所有编程技能:", find_by_key(data, "programming"))