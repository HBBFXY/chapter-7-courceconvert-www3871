# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
import keyword

# 1. 读取原文件
with open("random_int.py", "r", encoding="utf-8") as f:
    content = f.read()

# 2. 分割内容为单词（简单处理，实际可优化）
words = content.split()
processed_words = []
for word in words:
    # 判断是否为保留字
    if keyword.iskeyword(word):
        processed_words.append(word)
    else:
        # 非保留字转为大写
        processed_words.append(word.upper())

# 3. 重新拼接内容
processed_content = " ".join(processed_words)

# 4. 保存到新文件
with open("random_int_upper.py", "w", encoding="utf-8") as f:
    f.write(processed_content)