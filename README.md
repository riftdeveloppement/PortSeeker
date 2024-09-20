Voici un exemple de fichier `README.md` avec des émojis pour rendre la présentation plus visuelle et attrayante sur GitHub :

---

# 🔍 PortSeeker

**PortSeeker** is a fast and simple port scanner with a modern graphical interface. It allows you to scan for open ports on any IP address, showing results in an efficient way. Perfect for network security analysis and testing. 🚀

## ✨ Features
- ⚡ **Multithreaded port scanning** for faster results.
- 💻 **User-friendly graphical interface** built with PyQt5.
- 🎯 **Custom IP addresses and port ranges** support.
- ⏳ **Real-time results** and feedback on scan duration.
- 🌈 **Colorful animated title** for a modern look and feel.

## 📸 Preview
![PortSeeker Screenshot]([https://cdn.discordapp.com/attachments/1284442715211431948/1286774120343670856/Capture.PNG?ex=66ef2149&is=66edcfc9&hm=fd1c3673c830c6dd92ee660b55fceb38a403507881bf69e0a4a12ff4ad73bb09&])

## 🛠️ Installation

Follow these steps to set up **PortSeeker** on your machine:

### 📋 Requirements
- 🐍 Python 3.6 or higher.
- 📦 `pip` package manager.

### ⚙️ Step-by-Step Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/riftdeveloppement/PortSeeker.git
   cd PortSeeker
   ```

2. **Install the required dependencies:**

   You can use the `setup.bat` script to automatically install all the required Python libraries:

   ```bash
   setup.bat
   ```

   This will install:
   - 🎨 `PyQt5` for the graphical interface.
   - 🔧 Other necessary libraries.

3. **Run the application:**

   Once everything is installed, you can launch **PortSeeker** with the following command:

   ```bash
   start.bat
   ```

   or manually via:

   ```bash
   python PortSeeker.py
   ```

## 🚀 Usage

1. Enter the **IP address** of the target (e.g., `192.168.1.1`).
2. Specify the **range of ports** you want to scan (e.g., `1` to `65535`).
3. Click the **🔍 Scan** button to start scanning.

### 📝 Important Notes:
- ⚠️ The larger the port range, the longer the scan will take. Be patient!
- 🔄 If the program shows "Not Responding," it's still running — just give it time to complete the scan.

## 💡 Example

Here's a simple example of how you can use **PortSeeker**:

1. **IP Address:** `192.168.1.100`
2. **Port Range:** `20` to `1000`
3. **Result:** List of open ports on the target machine.

```plaintext
Open ports: [22, 80, 443]
```

## 🤝 Contribution

Contributions are welcome! 🎉

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature` 🎨
3. Commit your changes: `git commit -am 'Add a new feature'` 📝
4. Push to the branch: `git push origin feature/YourFeature` 🚀
5. Submit a pull request. 🔧

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any questions or suggestions, feel free to open an issue on GitHub or contact me directly via email at `your-email@example.com`.

---

### 🎉 Enjoy using PortSeeker and happy scanning! 🔍
