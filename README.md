

# Typing Speed Test

A desktop typing speed test built with Python and Tkinter. The application measures typing speed in words per minute (WPM) and tracks correct and incorrect words.

<img width="1107" height="328" alt="Screenshot 2026-10-07 at 9 10 08 PM" src="https://github.com/user-attachments/assets/d4e4f481-f3b2-4412-a953-b7f1b9bc643c" />

<img width="1107" height="327" alt="Screenshot 2026-10-07 at 9 11 57 PM" src="https://github.com/user-attachments/assets/d36b37f4-ad6b-45cd-ad82-bad8d46a11ff" />


## Features

* Starts the timer when the user begins typing
* Calculates typing speed in words per minute (WPM)
* Compares typed words with the original text
* Counts correct and incorrect words
* Stops the test when the user presses Enter
* Disables the text field after the test is completed
* Allows the user to restart the test

## Technologies

* Python
* Tkinter
* `Time`

## How It Works

The timer starts when the user types the first character. When the user presses Enter, the application compares the typed text with the original text word by word.

The application then calculates WPM based on the number of correctly typed words and the elapsed time.

The user can press **Re-start test** to clear the previous result and begin a new test.

## What I Practiced

This project was built as part of my Python learning journey and provided practice with:

* Tkinter GUI development
* Event handling with `bind()`
* Functions and callbacks
* Working with lists and strings
* Measuring elapsed time with `time.time()`
* Updating widgets with `.config()`
* Managing widget state with `normal` and `disabled`

## How to Run

Clone the repository and run:

```bash
python main.py
```

No external dependencies are required because the project uses Python's built-in `tkinter` and `time` modules.
