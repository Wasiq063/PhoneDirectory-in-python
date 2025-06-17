# 📱 Phone Directory

A **Tkinter**-based **Phone Directory** application built in **Python** for your Data Structures & Algorithms coursework. This project uses a **Trie** (prefix tree) to store and efficiently retrieve contacts by name, achieving average lookup and insertion time of **O(m)**, where *m* is the length of the name. It fully supports **prefix search**, auto‑suggesting matching contacts as you type.

---

## 📁 Project Structure


---

## 🧰 Features

- **Insert Contact**: Add new entries (name, phone number, email).  
- **Prefix Search**: As you type a name prefix, the Trie returns all matching contacts in real time.  
- **Auto‑Suggest**: Instant suggestions based on the current prefix.  
- **Delete Contact**: Remove contacts by exact name.  
- **List All Contacts**: Display all stored contacts in alphabetical order.  
- **GUI**: User‑friendly Tkinter windows, dialogs, and search field.

---

## 💾 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/Phone-Directory.git
   cd Phone-Directory
## 🔍 Why a Trie

A **Trie** (prefix tree) is ideal for contact lookup because:

- **Fast Prefix Queries**  
  Retrieves all keys sharing a prefix in **O(m + k)** time  
  (m = prefix length, k = number of matching contacts)

- **Space Efficiency**  
  Common prefixes are stored once, reducing memory when many names share beginnings

- **Auto‑Complete & Suggestions**  
  Naturally supports real‑time suggestion as you type each character

- **Predictable Performance**  
  Insert, search, and delete operations depend only on the key length, not the dataset size

---

## ⏱️ Time Complexity

Insert & Exact Search: O(m)
Prefix Search (lookup + collect): O(m + k)
Delete: O(m) to locate + O(d) to prune (d ≤ m)


- *m* = length of the name or prefix  
- *k* = number of matching contacts returned  
- *d* = depth of the tree nodes cleaned up during deletion  

