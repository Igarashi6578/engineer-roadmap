with open( "study.txt", "w", encoding="utf-8") as f:
    text=f.write("Pythonのファイル操作を学習中")

with open( "study.txt", "r", encoding="utf-8") as f:
    text=f.read()
print(text)

with open("study.txt", "a", encoding="utf-8") as f:
    f.write("\n今日はwriteとreadを学んだ")
with open("study.txt", "r", encoding="utf-8") as f:
    text=f.read()
print(text)

def save_log(message):
    with open("learning_log.txt","a",encoding="utf-8") as f:
        f.write(f"\n{message}")
def read_log(f):
    with open("learning_log.txt","r",encoding="utf-8") as f:
        text=f.read()
        return text
logs = [
    "Day11：データのフィルタリング",
    "Day12：例外処理",
    "Day13：ファイル操作"
]
with open("learning_log.txt","w",encoding="utf-8") as g:
    pass
for message in logs:
    save_log(message)
d=read_log(g)
print(d)


def read_file(filename):
    with open(f"{filename}","r",encoding="utf-8") as f:
        a=f.read()
    return a
def main(filename):
    try:
        text=read_file(filename)
        print(text)
    except FileNotFoundError:
        return "ファイルが見つかりません"
        
filename="unknown.txt"
a=main(filename)
print(a)