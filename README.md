
## 💬 Real-Time Chatbot using Python (Terminal + GUI)

This project is a simple yet powerful real-time chat application built using **Python's socket programming** and **threading**. It supports both **terminal-based clients** and a **desktop GUI** made with **Tkinter**. The server can handle multiple clients chatting simultaneously in real time.

---

## 🧾 YAML Summary

```yaml
project:
  name: Real-Time Chatbot
  tech_stack:
    - Python
    - Socket Programming
    - Threading
    - Tkinter
  interfaces:
    - Terminal-based chat client
    - GUI-based chat client
  communication: TCP sockets
  concurrency: Multithreaded server & client
  version: 1.0
  license: MIT
````

---

## 📁 Project Structure

```
real_time_chatbot/
│
├── realtime_chatbot/
│   ├── __init__.py
│   ├── server.py               # Core server code
│   ├── clients.py              # Terminal-based client
│   └── gui_client.py           # GUI-based client using Tkinter
├── screenshots/                # Images of terminal and GUI chat
├── pyproject.toml              # Poetry dependency manager config
└── README.md                   # Project documentation
```

---

## ⚙️ Prerequisites

* Python 3.x
* [Poetry](https://python-poetry.org/docs/#installation) (for managing dependencies)

### 📦 Install Poetry

```bash
pip install poetry
```

### 📥 Install Project Dependencies

```bash
poetry install
```

---

## 🛠️ Libraries Used

| Library      | Purpose                                          |
| ------------ | ------------------------------------------------ |
| socket       | Real-time communication between server & clients |
| threading    | Handles multiple clients concurrently            |
| tkinter      | GUI interface for chat client                    |
| scrolledtext | Scrollable chat window in GUI                    |
| simpledialog | Prompt for username in GUI client                |
| poetry       | Dependency and virtual environment management    |

---

## 🚀 How to Run

### 1️⃣ Start the Server

```bash
poetry run python -m realtime_chatbot.server
```

Expected output:

```
Server started on port 5555
```

### 2️⃣ Start a Terminal Chat Client

Open a new terminal and run:

```bash
poetry run python -m realtime_chatbot.clients
```

### 3️⃣ Start a GUI Chat Client (Optional)

In another terminal, run:

```bash
poetry run python -m realtime_chatbot.gui_client
```

> Each client will be prompted to enter a **username** upon joining.

---

## 🖼️ Screenshots

### 🧑‍💻 Terminal Clients

**Durga’s Chat:**

![Durga Terminal](screenshots/durga_terminal.png)

**Akanksha’s Chat:**

![Akanksha Terminal](screenshots/akanksha_terminal.png)

### 🪟 GUI Client (Tkinter)

**Desktop Chat Window:**

![GUI Chat](screenshots/gui_client.png)

> 📁 Make sure to store these images in the `screenshots/` folder inside your GitHub repository.

---

## 📊 Features

* 💬 Real-time chat communication
* 👩‍💻 Terminal and desktop (GUI) chat options
* 🧑‍🤝‍🧑 Multi-client support with threads
* 🪟 Scrollable chat window in GUI
* 🧾 Clean and readable messages with usernames

---

## 💡 Highlights

* 🔗 Uses `socket` and `threading` for efficient real-time communication
* 🧱 Clean folder structure for CLI and GUI components
* 🧪 Easy to extend into a production-grade chat server
* 🎯 Great learning project for Python networking and GUI design

---

## 🚧 Future Enhancements

* 🕒 Add timestamps to messages
* 🔐 Add encrypted messaging (SSL/TLS)
* 🌐 Build a web version (FastAPI + WebSockets)
* 🤖 Integrate ChatGPT or LLM chatbot
* 📊 Save chat history in SQLite or MongoDB
* 📦 Dockerize the full application

---

## 👩‍💻 Author

**Durga Rani**
*M.Tech in Data Science & AI | Passionate about Python, Analytics, and Communication Systems*

---

## 📜 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for details.

---

## 🙌 Acknowledgment

* 💾 Inspired by real-world chat systems and client-server architecture
* 🧠 Built as a hands-on networking + GUI programming project

---

## 📌 Summary

This project provides a solid foundation in:

* Python network programming
* Multithreaded client-server architecture
* GUI interface design using Tkinter

Whether you're building a collaborative tool or learning real-time systems, this is a great starting point!

> 💬 “Code is like humor. When you have to explain it, it’s bad.” – *Cory House*

---

## ✅ What to Do Next

1. **Save this file as `README.md` in your root project folder**
2. **Create a `screenshots/` folder**
3. **Add the 3 images you captured and rename them to:**

   * `durga_terminal.png`
   * `akanksha_terminal.png`
   * `gui_client.png`
4. **Commit and push everything to GitHub!**

---

## 📦 Optional Extras

Would you like the following files added to complete your project setup?

* ✅ `LICENSE` file (MIT)
* ✅ `.gitignore` file (Python + Poetry support)

Let me know and I’ll generate them for you!

```

---

Let me know if you’d like this exported as a downloadable file or if you need me to generate the `LICENSE`, `.gitignore`, or `requirements.txt` as well!
```
