from tkinter import *
import time

window = Tk()
window.title("Typing speed test")
window.minsize(width=500, height=300)

wpm=0

#title
title_label = Label(text="Typing Speed Test")
title_label.pack()

#label of what the user will write
text_label = Label(text="The sun was out and we went to the park. My dog ran to the big tree "
                        "and back. We had a snack on the grass and then we went home. "
                        "It was a good day and we want to go again soon.")
text_label.pack()

#entry box to the user write
entry = Entry()
entry.pack()

#result
result_label = Label(text=f"Your speed is: {wpm}")
result_label.pack()


start_time = 0
def start_test(event):
    global start_time
    global wpm
    if start_time == 0:
        start_time = time.time()
    else:
        pass
    if entry.get() == text_label["text"]:
        end_time = time.time()

        elapsed_time = end_time - start_time
        minutes = elapsed_time / 60

        words = text_label["text"].split()
        words_count = len(words)

        wpm = words_count / minutes

        result_label.config(text=f"Your speed is: {wpm:.0f} words per minute")


entry.bind("<Key>", start_test)

window.mainloop()