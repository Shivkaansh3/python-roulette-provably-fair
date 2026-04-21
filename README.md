# 🎰 Python Roulette Game (Provably Fair System)

## 📌 Overview
This project is a Python-based roulette game that implements a **provably fair algorithm** using client seed, server seed, and SHA-256 hashing.

It ensures that every game outcome is **transparent, verifiable, and unbiased**, similar to real-world modern online gaming systems.

---

## 🚀 Features
- Provably fair system using SHA-256 hashing
- Client seed + server seed + nonce mechanism
- Adjustable betting system
- Balance tracking with real-time updates
- Free coin redemption feature
- CLI-based interactive gameplay

---

## 🛠️ Technologies Used
- Python 3
- hashlib (SHA-256)

---

## ⚙️ How It Works
1. User enters a client seed  
2. System combines:
   - Client seed  
   - Server seed  
   - Nonce  
3. Generates SHA-256 hash  
4. Converts hash → number (0–36)  
5. User places bet → result generated  
6. Balance updated accordingly  

---

## 🎯 Key Learning
- Cryptographic hashing (SHA-256)
- Randomization techniques
- Game logic implementation
- Fairness verification systems

---

## 📌 Future Improvements
- GUI version (Tkinter)
- Web app version (Flask/Django)
- Database integration
- Multiplayer support

---

## 👨‍💻 Author
Shreyash Maurya  
GitHub: https://github.com/Shivkaansh3
