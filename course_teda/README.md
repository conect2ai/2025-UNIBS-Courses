# 🧠 TEDA Unibs Course

This repository contains the practical material of the **TEDA Course** delivered to the students of the **University of Brescia (UNIBS)**.  
The goal is to present, in a practical and didactic way, the use of the **TEDA** for outlier detection and TEDA-RLS for anomaly correction in energy consumption time series.

## 📂 Repository Structure

```
.
├── TEDA_TEDARLS.ipynb         # Main notebook with explanations and code
├── teda.py                    # TEDA algorithm implementation
├── lead1.0-small.csv          # Energy consumption dataset
├── README.md                  # This file
├── RLSFilter.py               # RLS filter algorithm implementation
├── PowerWithOutliers.xlsx     # Power dataset with outliers
```

## 📋 Prerequisites

- Python 3.8+
- Packages listed in `requirements.txt`:
  ```bash
  pip install pandas numpy matplotlib scikit-learn
  ```

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/conect2ai/2025-UNIBS-Courses.git
   cd 2025-UNIBS-Courses/course_teda
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main notebook:
   ```bash
   jupyter notebook TEDA_Demo_Bootcamp.ipynb
   ```

4.	**Run the cells sequentially** to:
    -	Load and preprocess the data
    -	Apply TEDA
    -	Visualize anomalies
    -	Evaluate metrics and sensitivity of parameter `m`

## ☁️ Running on Google Colaboratory

1.	Access: [Google Colaboratory](https://colab.research.google.com/)
2.	Click on **File → Upload notebook**
3.	Upload the file `TEDA.ipynb`
4.	Also upload the files `teda.py` and `lead1.0-small.csv` to the Colab file area (left panel).
5.	Run the cells in order.

💡 Tip: You can also open the notebook directly from GitHub in Colab by clicking the link:
```
https://colab.research.google.com/github/conect2ai/TEDA-Bootcamp/blob/main/TEDA_Demo_Bootcamp.ipynb
```

## 📊 Dataset

The dataset used in this course is the `lead1.0-small.csv`, which contains energy consumption time series data. The data is structured with the following columns:

- `building_id`: The unique identifier for each observation
- `timestamp`: The time of the observation
- `meter_reading`: The energy consumption value
- `anomaly`: Indicates if the observation is an anomaly (1) or not (0)

### Dataset Reference

- **LEAD1.0: A Large-scale Annotated Dataset for Energy Anomaly Detection in Commercial Buildings**, Manoj Gulati & Pandarasamy Arjunan, arXiv preprint, 30 de março de 2022. Disponível em: [arXiv](https://arxiv.org/abs/2203.17256)

## 🧩 TEDA Algorithm

TEDA (Typicality and Eccentricity Data Analytics) is an incremental method for anomaly detection that requires no prior training and is suitable for execution on embedded devices (TinyML).

## 🧩 TEDA-RLS Algorithm

TEDA-RLS (Typicality and Eccentricity Data Analytics with Recursive Least Squares) extends the TEDA framework by integrating it with the **Recursive Least Squares (RLS)** filter.  
While TEDA is responsible for identifying whether new samples are **typical** or **eccentric** (potential outliers), RLS performs **parameter estimation** in real time.  

By combining both, TEDA-RLS is able not only to detect anomalies but also to **correct the effect of outliers** during online model updates.

### 🔑 How it works

1. TEDA computes the **eccentricity** and **typicality** of the incoming sample.  
2. If the sample is typical, RLS updates its parameters normally.  
3. If the sample is eccentric:
   - The update can be weighted by the **typicality** (reducing its influence), or  
   - The sample can be discarded to avoid contaminating the model.  

### 📊 Evaluation

- **TEDA part (classification):** evaluated through confusion matrix, precision, recall, and F1-score.  
- **RLS part (regression):** evaluated through error metrics such as Mean Squared Error (MSE) and Mean Absolute Error (MAE).  

### ⚡ Applications

- Noisy time series  
- Fault detection  
- Real-time vehicular data (OBD-II)  
- Energy consumption anomaly correction  

### 📓 Notebook

See the notebook [`TEDA_TEDARLS.ipynb`](./TEDA_TEDARLS.ipynb) for a complete demo including:
- Data loading and preprocessing  
- TEDA-RLS algorithm step by step  
- Visualization of anomalies and corrections  
- Metric reports for TEDA (classification) and RLS (regression)  

### Key References

- Angelov, P. **"Anomaly detection based on eccentricity analysis"**, apresentação do framework TEDA em *IEEE Symposium on Evolving and Autonomous Learning Systems (EALS)*, Orlando, FL, EUA, dezembro de 2014. Introduz os conceitos de *typicality* e *eccentricity*, calculados de forma recursiva e sem assumir distribuições paramétricas.  [IEEE Xplore](https://ieeexplore.ieee.org/document/7009497) 

- Angelov também publicou o artigo **"Outside the Box: An Alternative Data Analytics Framework"**, *Journal of Automation, Mobile Robotics and Intelligent Systems*, vol. 8, n.º 2, 2014, p. 29-35, que fundamenta o TEDA como uma metodologia sistemática que dispensa suposições prévias sobre os dados e é adequada para processos reais complexos.  [JAMRIS](https://www.jamris.org/index.php/JAMRIS/article/view/299)


- **TEDA-RLS: A TinyML Incremental Learning Approach for Outlier Detection and Correction**, Pedro Andrade et al., *IEEE Sensors Journal*, novembro de 2024. Proposta de um algoritmo incremental baseado em RLS para detecção e correção de outliers em tempo real, implementado em um scanner OBD-II como prova de conceito. Disponível em: [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10682534)

- **TEDA-Forecasting: An Unsupervised TinyML Incremental Learning Approach for Outlier Processing and Forecasting**, Pedro Andrade et al., *Computing*, vol. 107, artigo 162, publicado em 2 de julho de 2025, DOI: 10.1007/s00607-025-01490-3. Apresenta uma versão do TEDA adaptada para previsão de séries temporais e correção de outliers, com execução em dispositivo real de edge computing (TinyML)  [Springer Nature - Computing](https://link.springer.com/article/10.1007/s00607-025-01490-3)

## 🏆 Activities

The notebook includes:
- Step-by-step demonstrations
- Practical exercises to explore different values of m
- Performance comparison among buildings