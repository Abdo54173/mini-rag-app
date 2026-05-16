# Mini RAG App

## Setup Project

### 1) Install Python

Install Python 3.8 or later:

https://www.python.org/downloads/

Check installation:

```bash
python --version
```

---

### 2) Install Miniconda

Download Miniconda:

https://www.anaconda.com/download/success

Check installation:

```bash
conda --version
```

---

### 3) Clone Project

```bash
git clone https://github.com/Abdo54173/mini-rag-app.git
```

Enter project folder:

```bash
cd mini-rag-app
```

---

### 4) Create Conda Environment

```bash
conda create -n mini-rag-app python=3.11
```

Activate environment:

```bash
conda activate mini-rag-app
```

---

### 5) Install Requirements

```bash
pip install -r requirements.txt
```

---

### 6) Create .env File

Create `.env` file:

```bash
touch .env
```

Example:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 7) Run Project

```bash
python app.py
```

### run the fastapi server 

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```