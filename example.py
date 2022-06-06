from tkinter import*

root = Tk()

def returnEntry(arg=None):
    result=mEntry.get()
    resultLabel.config(text=result)
    mEntry.delete(0, END)

#텍스트
label = Label(root, text="Hello World")
label.pack()

#사용자 입력
mEntry = Entry(root, width=20)
mEntry.focus()
mEntry.bind("<Return>", returnEntry) #이건 좀 알아 봐야 겠네
mEntry.pack()

#버튼 클릭 - 함수 실행
button = Button(root, text="Click me", command=returnEntry)
button.pack()

#result
resultLabel = Label(root, text="")
resultLabel.pack(fill=X)

#윈도우 사이즈 설정
root.geometry("500x300")

#기본 루프
root.mainloop()