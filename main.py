from tkinter import *

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

window.mainloop()