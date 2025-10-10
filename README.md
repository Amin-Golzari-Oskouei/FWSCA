# FWSCA: Feature-Weighted Soft Clustering Algorithms

**Authors:**  
Amin Golzari Oskouei¹˒⁴*, Negin Samadi², Asgarali Bouyer³˒⁴, and Bahman Arasteh⁴˒⁵˒⁶  
¹ Faculty of IT and Computer Engineering, Urmia University of Technology, Iran  
² Faculty of Electrical and Computer Engineering, University of Tabriz, Iran  
³ Azarbaijan Shahid Madani University, Tabriz, Iran  
⁴ Istinye University, Istanbul, Türkiye  
⁵ Khazar University, Baku, Azerbaijan  
⁶ Applied Science Private University, Amman, Jordan  

**Contact:** a.golzari@uut.ac.ir  
**License:** MIT License  

---

## 🧠 Overview

**FWSCA** (Feature-Weighted Soft Clustering Algorithms) is an open-source Python package that implements **26 feature-weighted fuzzy clustering algorithms**.  
It aims to bridge the gap between theoretical development and practical implementation of **feature-weighted soft clustering** methods.

This package is particularly valuable for **machine learning**, **data mining**, and **pattern recognition** researchers and practitioners.  
It supports various datasets, provides extensive **evaluation metrics**, and allows users to **modify or extend algorithms easily** through its modular structure.

---

## 🚀 Features

- Implementation of **26 feature-weighted fuzzy clustering algorithms**  
- Modular architecture with transparent and extensible code structure  
- Support for both **internal** and **external** evaluation metrics:
  - Accuracy, NMI, Precision, Recall, F1, Silhouette, and Davies–Bouldin  
- Includes **sample dataset** (e.g., Iris) and **demo scripts** for quick testing  
- Fully **reproducible** with fixed random seeds and logging

---

## 🧩 Software Architecture

The package follows a **modular and reusable design**:

| Module | Description |
|--------|--------------|
| `main.py` | Core implementation of the clustering algorithm, including optimization and convergence steps |
| `object_fun.py` | Defines the mathematical objective function of the algorithm |
| `parameters.py` | Contains configuration parameters (e.g., number of clusters, fuzzifier, iteration limits) |
| `calculateMetrics.py` | Provides performance metrics (Accuracy, NMI, F1, etc.) |
| `demo.py` | Demonstration script that loads datasets, runs algorithms, and displays results |
| `iris.mat` | Example dataset for testing |

---

## ⚙️ Installation

### Requirements
- Python ≥ 3.10  
- Dependencies:  
  ```bash
  pip install numpy scipy
Clone the Repository
bash
Copy code
git clone https://github.com/Amin-Golzari-Oskouei/FWSCA.git
cd FWSCA
▶️ Usage
You can quickly run any algorithm by executing the demo script:

bash
Copy code
python demo.py
This will:

Load the sample dataset (iris.mat)

Initialize the selected algorithm

Run the clustering process

Print and save evaluation metrics

Example: Running a Specific Algorithm
You can modify the algorithm selection or parameters in parameters.py:

python
Copy code
num_clusters = 3
fuzzifier = 2
max_iter = 100
epsilon = 1e-5
Then run:

bash
Copy code
python main.py
Results will be displayed in the console and optionally saved to output files.

💡 Example Output
makefile
Copy code
Algorithm: FWCW-FCM
Dataset: Iris
Clusters: 3
Accuracy: 0.923
NMI: 0.841
Silhouette: 0.712
Davies–Bouldin: 0.428
📚 Contribution Guidelines
We welcome contributions from the research and developer community!

To contribute:
Fork the repository

Create a new branch:

bash
Copy code
git checkout -b feature-name
Follow consistent coding standards:

Use clear variable names

Comment complex logic

Use modular design similar to existing algorithms

Submit a Pull Request (PR) with a detailed description of changes

Please ensure your contribution passes basic tests and follows the existing directory structure.

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.
You are free to use, modify, and distribute the code with attribution.

🧑‍💻 Contact & Support
For questions, issues, or feedback, please contact:

📧 Amin Golzari Oskouei
Faculty of IT and Computer Engineering, Urmia University of Technology
Email: a.golzari@uut.ac.ir

📈 Citation
If you use this package in your research, please cite:

A. G. Oskouei, N. Samadi, A. Bouyer, and B. Arasteh,
"FWSCA: An Open-Source Python Package for Feature-Weighted Soft Clustering Algorithms",
2025.

yaml
Copy code

---

Would you like me to include **example figures/screenshots** (e.g., directory structure or sample output visualization) in the README for better clarity? I can add them using Markdown image tags.







