# CloudLogFM

## AI-Powered Cloud Incident Intelligence Platform

CloudLogFM is a Machine Learning powered platform for intelligent cloud incident analysis. It is designed to assist cloud operations teams in detecting anomalies, retrieving similar incidents, assessing severity, and performing root cause analysis from large-scale cloud infrastructure logs.

The project addresses challenges commonly faced in cloud environments such as AWS, where millions of log events are generated daily and rapid incident resolution is critical for maintaining service reliability.

---

## Problem Statement

Modern cloud infrastructures generate enormous volumes of operational logs from distributed services, containers, virtual machines, databases, and networking systems.

Manual incident investigation often leads to:

* Increased Mean Time To Resolution (MTTR)
* Difficulty identifying root causes
* Delayed incident response
* Poor utilization of historical incident knowledge

CloudLogFM leverages Machine Learning and Retrieval-Augmented Intelligence to automate and accelerate incident analysis workflows.

---

## Key Features

### Incident Intelligence

* Automated incident analysis
* Severity assessment
* Root cause identification
* Anomaly detection

### LogBERT-Based Learning

* Semantic log understanding
* Event sequence representation
* Context-aware anomaly detection
* Log embedding generation

### Similar Incident Retrieval

* FAISS vector similarity search
* Historical incident matching
* Retrieval-augmented troubleshooting

### Analytics Dashboard

* Incident trend visualization
* Severity distribution analysis
* Repository statistics
* Operational monitoring

---

## System Architecture

```text
                    Cloud Infrastructure Logs
                                │
                                ▼
                       Log Parsing Pipeline
                                │
                                ▼
                       Event Sequence Creation
                                │
                                ▼
                         LogBERT Model
                                │
                                ▼
                     Embedding Generation
                                │
                                ▼
                     FAISS Vector Retrieval
                                │
                                ▼
                    Incident Intelligence Engine
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
       Severity Analysis   Similar Incidents   Root Cause Analysis
                │               │               │
                └───────────────┼───────────────┘
                                ▼
                      Analytics Dashboard
```

---

## Machine Learning Pipeline

### 1. Log Processing

Cloud logs are parsed and converted into structured event sequences.

### 2. Representation Learning

LogBERT learns semantic relationships between events and generates vector embeddings.

### 3. Anomaly Detection

The model identifies abnormal patterns within event sequences.

### 4. Incident Retrieval

FAISS retrieves historically similar incidents using vector similarity search.

### 5. Root Cause Analysis

The platform generates incident intelligence reports including severity and root cause recommendations.

---

## Technology Stack

### Machine Learning

* PyTorch
* LogBERT
* FAISS
* NumPy
* Pandas

### Backend

* FastAPI
* Python
* Uvicorn

### Frontend

* React
* Vite
* Material UI
* Axios
* Recharts

### Deployment

* Render
* Vercel
* GitHub

---

## Project Structure

```text
CloudLogFM
│
├── frontend/
├── api/
├── backend/
├── ml/
│   ├── checkpoints/
│   ├── tokenizer/
│   ├── incident_engine/
│   └── pretraining/
│
├── data/
├── scripts/
├── tests/
└── deployment/
```

---

## Business Impact

CloudLogFM helps cloud operations teams:

* Reduce Mean Time To Resolution (MTTR)
* Detect anomalies proactively
* Improve operational reliability
* Accelerate incident investigations
* Reuse historical incident knowledge

The platform is designed for cloud-scale environments similar to AWS infrastructure where rapid incident response is essential.

---

## Live Demo

**Frontend:**
https://cloud-logfm.vercel.app/

**Backend:**
https://cloudlogfm-api.onrender.com/

---

## Author

**Rishika Rajora**

Machine Learning | Cloud Intelligence | Incident Analytics | AI Systems





