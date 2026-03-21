```markdown
# Python Hello World Exercises

## 📌 Overview
This project contains a collection of beginner-level Python exercises designed to build a strong foundation in:

- Printing output
- Using f-strings
- Working with integers and floats
- String manipulation (slicing, repetition, concatenation)

Each exercise includes a clear objective and a reference solution.

---

## 📂 Project Structure

```

.
├── 0-print.py
├── 1-print_integer.py
├── 2-print_float.py
├── 3-print_string.py
├── 4-play_with_strings.py
├── 5-copy_cut_paste.py
├── 6-create_sentence.py
└── 7-zen_of_python.py

````

---



---

## ▶️ How to Run

Make sure your file is executable:

```bash
chmod +x filename.py
````

Run the script:

```bash
./filename.py
```

Or:

```bash
python3 filename.py
```

Example:

```bash
python3 0-print.py
```

---

## Exercises

### 0. Hello, print

#### Objective

Print exactly:

```
"Programming is like building a multilingual puzzle
```

#### Solution

```python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```

---

### 1. Print integer

#### Objective

Print the integer stored in `number`, followed by `Battery street` using an f-string.

#### Solution

```python
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
```

---

### 2. Print float

#### Objective

Print a float with 2 decimal places using an f-string.

#### Solution

```python
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```

---

### 3. Print string

#### Objective

* Print a string 3 times
* Print its first 9 characters
  (No loops allowed)

#### Solution

```python
#!/usr/bin/python3
str = "Holberton School"
print(3 * str)
print(str[:9])
```

---

### 4. Play with strings

#### Objective

Print:

```
Welcome to Holberton School!
```

#### Solution

```python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
```

---

### 5. Copy - Cut - Paste

#### Objective

From the word `"Holberton"` extract:

* First 3 letters
* Last 2 letters
* Middle part (excluding first and last letters)

#### Solution

```python
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]

print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

---

### 6. Create a new sentence

#### Objective

Rearrange the string to output:

```
object-oriented programming with Python
```

(No new variables, no loops)

#### Solution

```python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[-22:-17] + str[:6]
print(str)
```

---

### 7. Easter Egg

#### Objective

Print:

```
The Zen of Python, by Tim Peters
```

#### Solution

```python
#!/usr/bin/python3
import this
```

#### Note

This will display the full Zen of Python in the terminal.



```
```
