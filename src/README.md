# BPI 2017 Loan-Application Process Mining (PM4Py)

This project discovers, visualises, and analyses the **BPI Challenge 2017** loan-application process of a Dutch financial institution using **PM4Py**.  
It shows how different discovery algorithms (Inductive Miner, Alpha Miner, Heuristic Miner) and performance overlays can be applied to a real-life log.

---

## Dataset

> BPI Challenge. (2017). BPI Challenge 2017 dataset.  
> **BPI Challenge 2017 Event Log** (loan-application process).  
> *4TU.ResearchData.*  
> https://doi.org/10.4121/uuid:3926db30-f712-4394-aebc-75976070e91f

Download the `BPI_Challenge_2017.xes.gz` file from the DOI page and place it inside **`./DataSet/`** (keep the folder name).

---

## Repository structure
├── DataSet/
│ └── BPI_Challenge_2017.xes[.gz] ← raw event log
├── src/
│ ├── inductive_low_noise.py ← Inductive Miner (+ perf overlay)
│ ├── alpha_miner.py ← Alpha Miner example
│ └── heuristic_miner.py ← Heuristic Miner example
├── .gitignore
├── requirements.txt
└── README.md

---

## Quick start

```bash
# 1 Create & activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2 Install dependencies
pip install -r requirements.txt

# 3 Run Inductive Miner script
python src/inductive_low_noise.py
#   ▸ outputs:  inductive_low_noise_perf.png

# 4 Run Alpha- or Heuristic-Miner examples
python src/alpha_miner.py
python src/heuristic_miner.py 
```

---

Note: graphviz must be available on your system path for PNG/SVG export
```bash
# • macOS brew install graphviz
# • Ubuntu sudo apt install graphviz
# • Windows installer from graphviz.org.
```
---
## Scripts
Script	Description
inductive_low_noise.py	Inductive Miner – Infrequent (noise_threshold = 0.05) → Petri net → performance-decorated PNG
alpha_miner.py	Classic Alpha Miner → Petri net PNG + performance/frequency DFG
heuristic_miner.py	Heuristic Miner with default thresholds → Petri net PNG + performance/frequency DFG

Each script:

* Loads the XES log

* Orders events by timestamp

* Filters traces with ≥ 2 events

* Discovers a model

* Saves a visualisation to ./

---

### How to adjust noise / thresholds
Inductive Miner noise filter: change noise_threshold (0 = most detail, 1 = very coarse).

Heuristic Miner: tweak dependency_thresh, and_measure_thresh, etc. in heuristic_miner.py.

---
### License
This code is released under the MIT License.
The dataset remains under the terms specified by 4TU.ResearchData.
---
### Citation
If you use this code or visualisations in academic work, please cite both:

#### Dataset: BPI Challenge. (2017). BPI Challenge 2017 dataset.

#### PM4Py. (n.d.). PM4Py: Process mining for Python