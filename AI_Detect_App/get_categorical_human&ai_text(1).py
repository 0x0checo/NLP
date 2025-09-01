import json
import os

# 输入输出文件
input_files = [
    r"D:\工作\dataset\中文数据集\对比数据\法学\法学.json",
    r"D:\工作\dataset\中文数据集\对比数据\工学\工学.json",
    r"D:\工作\dataset\中文数据集\对比数据\管理学\管理学.json",
    r"D:\工作\dataset\中文数据集\对比数据\教育学\教育学.json",
    r"D:\工作\dataset\中文数据集\对比数据\经济学\经济学.json",
    r"D:\工作\dataset\中文数据集\对比数据\军事学\军事学.json",
    r"D:\工作\dataset\中文数据集\对比数据\理学\理学.json",
    r"D:\工作\dataset\中文数据集\对比数据\历史学\历史学.json",
    r"D:\工作\dataset\中文数据集\对比数据\农学\农学.json",
    r"D:\工作\dataset\中文数据集\对比数据\文学\文学.json",
    r"D:\工作\dataset\中文数据集\对比数据\医学\医学.json",
    r"D:\工作\dataset\中文数据集\对比数据\艺术学\艺术学.json",
    r"D:\工作\dataset\中文数据集\对比数据\哲学\哲学.json",
    r"D:\工作\dataset\中文数据集\对比数据\政治学\政治学.json"
]
save_path = "D:\工作\dataset\中文数据集\原始数据\AI\ds1.5\deepseek各学科人类和ai文本.json"

# 初始化数据结构
datas = [
    {'human':[]},
    {'ai':[]},
]

# 遍历输入文件
for file in input_files:
    # 提取类别名称
    category = os.path.splitext(os.path.basename(file))[0]
    # 读取json文件
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # 提取人类和ai文本
    human = [item['original_text'] for item in data]
    ai = [item['rewritten_text'] for item in data]
    # 分类添加
    datas[0]['human'].append({category: human})
    datas[1]['ai'].append({category: ai})

# 写入新的json文件
with open(save_path, 'w', encoding='utf-8') as f:
    json.dump(datas, f, ensure_ascii=False, indent=4)