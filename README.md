# 🔐 PyPassword Generator

A simple and interactive Python project that generates secure passwords based on user preferences. This project supports **randomized ordering** of letters, numbers, and symbols, with a clean **command-line interface** enhanced using the `colorama` module for colorful output.

## 🚀 Features

- Choose the number of **letters**, **symbols**, and **numbers** in your password  
- Password characters are **randomly shuffled** for extra security (Hard Level)  
- Clean and interactive **terminal UI** with colored prompts  
- Written as a **function**, ready for reuse and integration  

## 🖥️ Preview

```
Welcome to the PyPassword Generator!
How many letters would you like in your password? 5
How many symbols would you like? 2
How many numbers would you like? 3

Your password is: aT8$dF1)b
```

## 🛠️ Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/py-password-generator.git
cd py-password-generator
```

2. Install dependencies:

```bash
pip install colorama
```

3. Run the script:

```bash
python main.py
```

> ✅ Make sure you have Python 3.6 or higher installed.

## 🧠 How It Works

- User inputs how many letters, symbols, and numbers they want  
- The script picks random characters from each category  
- Characters are combined and shuffled to form a secure password  
- The result is displayed in a styled format using `colorama`  

## 📁 Project Structure

```
📦 py-password-generator
├── main.py
├── README.md
└── requirements.txt
```

## 📦 Dependencies

- [colorama](https://pypi.org/project/colorama/)

Install via:

```bash
pip install -r requirements.txt
```

## 📄 License

This project is licensed under the [MIT License](LICENSE)

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

**Made with ❤️ in Python**
