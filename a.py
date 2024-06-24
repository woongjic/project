import tkinter as tk
from tkinter import scrolledtext

def count_words():
    text = text_area.get('1.0', tk.END)
    words = text.split()
    word_count = len(words)
    result_label.config(text=f"단어 수: {word_count}")

# 메인 윈도우 생성
root = tk.Tk()
root.title("단어 수 세기 도구")
root.geometry("500x400")

# 텍스트 입력 영역 생성
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
text_area.pack(padx=10, pady=10)

# 단어 수 계산 버튼 생성
count_button = tk.Button(root, text="단어 수 세기", command=count_words)
count_button.pack(pady=10)

# 결과 레이블 생성
result_label = tk.Label(root, text="단어 수: 0")
result_label.pack(pady=10)

# 메인 이벤트 루프 시작
root.mainloop()
