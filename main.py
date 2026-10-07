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

#restart button
button = Button(text="Re-start test")
button.pack()


start_time = 0

def start_test(event):
    global start_time

    if start_time == 0:
        start_time = time.time()



def finish_test(event):
    global start_time
    if start_time != 0:
        words_count = 0
        incorrect_words = 0
        end_time = time.time()

        elapsed_time = end_time - start_time
        minutes = elapsed_time / 60

        original = text_label["text"].split()
        typed = entry.get().split()
        print(original)
        print(typed)

        for i in range (min(len(original), len(typed))):
            if original[i] == typed[i]:
                words_count += 1
            else:
                incorrect_words +=1

        wpm = words_count / minutes

        result_label.config(text=f"Your speed is: {wpm:.0f} words per minute. "
                                 f"You had {words_count} correct words. "
                                 f"and {incorrect_words} incorrect words.")




entry.bind("<Key>", start_test)

entry.bind("<Return>", finish_test)

window.mainloop()