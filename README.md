
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

**FWSCA (Feature-Weighted Soft Clustering Algorithms)** is an open-source Python package that implements **26 feature-weighted fuzzy clustering algorithms**.  
It bridges the gap between theoretical development and practical application of **feature-weighted soft clustering** techniques.

The package is highly useful for **machine learning**, **data mining**, and **pattern recognition** researchers and practitioners.  
It supports multiple datasets, provides extensive evaluation metrics, and allows users to easily extend or modify the algorithms.

---

## 🚀 Features

- Implementation of **26 feature-weighted fuzzy clustering algorithms**
- Modular and transparent code structure
- Internal and external evaluation metrics:
  - Accuracy, NMI, Precision, Recall, F1, Silhouette, Davies–Bouldin
- Sample dataset included (e.g., *Iris*)
- Reproducible experiments with fixed random seeds

---

## 🧩 Software Architecture

| Module | Description |
|--------|--------------|
| `main.py` | Core algorithm implementation: optimization, membership updates, convergence checks |
| `object_fun.py` | Mathematical objective function of the clustering algorithm |
| `parameters.py` | Default configuration parameters (clusters, fuzzifier, iterations, thresholds) |
| `calculateMetrics.py` | Performance evaluation module with internal/external metrics |
| `demo.py` | Demonstration script: runs the algorithm, loads data, prints results |
| `iris.mat` | Sample dataset for initial testing |

---

## ⚙️ Installation

### Requirements
- Python ≥ 3.10  
- Dependencies:
  ```bash
  pip install numpy scipy


### Clone the Repository

```bash
git clone https://github.com/Amin-Golzari-Oskouei/FWSCA.git
cd FWSCA
```

---

## ▶️ Usage

To quickly test the package, simply run the demo script:

```bash
python demo.py
```

This will:

1. Load the sample dataset (`iris.mat`)
2. Initialize and run the selected algorithm
3. Display evaluation metrics in the console

### Example: Running a Specific Algorithm

You can change the parameters in `parameters.py`:

```python
num_clusters = 3
fuzzifier = 2
max_iter = 100
epsilon = 1e-5
```

Then execute:

```bash
python main.py
```

Results will appear in the terminal and can be saved automatically.

---

## 💡 Example Output

```
Algorithm: FWCW-FCM
Dataset: Iris
Clusters: 3
Accuracy: 0.923
NMI: 0.841
Silhouette: 0.712
Davies–Bouldin: 0.428
```

---

## 📚 Contribution Guidelines

We welcome contributions from the community!

### To contribute:

1. Fork the repository
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```
3. Follow these rules:

   * Use clear variable names
   * Add comments for complex code
   * Keep the modular design structure
4. Submit a Pull Request (PR) with a detailed description of your updates.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
You are free to use, modify, and distribute this software with proper attribution.

---

## 🧑‍💻 Contact & Support

For questions, issues, or collaboration requests, please contact:

📧 **Amin Golzari Oskouei**
Faculty of IT and Computer Engineering, Urmia University of Technology
Email: [a.golzari@uut.ac.ir](mailto:a.golzari@uut.ac.ir)

---

## 📈 Citation

If you use this package in your research, please cite:

> A. G. Oskouei, N. Samadi, A. Bouyer, and B. Arasteh,
> **"FWSCA: An Open-Source Python Package for Feature-Weighted Soft Clustering Algorithms"**,
> 2025.

---

```

