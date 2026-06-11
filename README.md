# 🧠 NeuroLens AI

### AI-Powered Brain Tumor MRI Analysis System

NeuroLens AI is a full-stack deep learning web application that performs automated brain tumor detection and segmentation from MRI scans using a U-Net model trained on the BraTS 2020 dataset.

The system allows users to upload MRI scans in `.nii` / `.nii.gz` format, processes them through a trained AI model, generates tumor segmentation masks, calculates tumor statistics, and provides a complete AI-assisted medical report through an interactive cyber-themed dashboard.

---

## 🚀 Features

### 🧠 AI MRI Analysis
- Brain tumor detection using Deep Learning
- U-Net based medical image segmentation
- MRI slice preprocessing and normalization
- Tumor mask generation
- Tumor overlay visualization

### 📊 Tumor Analytics
- Tumor detected / not detected status
- Tumor area calculation
- Affected brain percentage estimation
- AI confidence score
- Risk level assessment

### 📄 AI Medical Report
- Unique scan ID generation
- Automated analysis summary
- Scan date and report details
- PDF report download

### 🎨 Modern AI Dashboard
- Cyber-inspired black grid interface
- Glassmorphism cards
- Interactive MRI visualization
- Drag & drop MRI upload
- Responsive design

---

# 🏗 System Architecture

```
                   MRI Scan (.nii.gz)
                           |
                           ▼
                   MRI Preprocessing
                           |
                           ▼
                  U-Net Deep Learning Model
                           |
                           ▼
                  Tumor Segmentation Mask
                           |
                           ▼
                Visualization & Analytics
                           |
                           ▼
             FastAPI Backend REST API
                           |
                           ▼
              React Cyber Dashboard
```

---

# 🧠 Deep Learning Model

### Architecture
- U-Net Convolutional Neural Network

### Dataset
- BraTS 2020 Brain MRI Dataset

### Model Output
- Binary tumor segmentation mask
- Tumor region statistics
- Confidence estimation

---

# 🛠 Technology Stack

## AI & Machine Learning
- Python
- PyTorch
- U-Net Architecture
- NumPy

## Medical Image Processing
- NiBabel
- OpenCV
- Pillow

## Backend
- FastAPI
- Uvicorn

## Frontend
- React.js
- Vite
- Tailwind CSS
- Axios
- jsPDF

---

# 📂 Project Structure

```
NeuroLens/
│
├── backend/
│   ├── app.py                 # FastAPI API
│   ├── inference.py           # AI prediction pipeline
│   ├── model.py               # U-Net architecture
│   ├── preprocessing.py       # MRI preprocessing
│   ├── visualization.py       # MRI mask visualization
│   ├── model.pth              # Trained AI model
│   ├── outputs/               # Generated MRI images
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# ⚙ Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/NeuroLens.git

cd NeuroLens
```

---

## 2. Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```

Start Backend:

```bash
uvicorn app:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## 3. Frontend Setup

Open a new terminal:

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# 📷 Usage

1. Open the NeuroLens dashboard
2. Upload a `.nii` or `.nii.gz` MRI scan
3. Click **Analyze with AI**
4. View:
   - Tumor prediction
   - MRI image
   - Tumor mask
   - AI overlay
   - Statistics
   - Medical summary
5. Download PDF report

---

# ⚠ Disclaimer

NeuroLens AI is developed for educational and research purposes only.

The generated results are AI-assisted predictions and must not be considered a substitute for professional medical diagnosis, treatment, or clinical decision-making.

---

# 🔮 Future Improvements

- Multi-class tumor segmentation
- 3D MRI volume visualization
- Patient history management
- Cloud model inference
- Improved AI explainability
- User authentication

---

# 👨‍💻 Author

Developed by **AfraazUl** **Haque**

Built with Deep Learning, FastAPI, React, and Medical Imaging Technologies.

---

## ⭐ If you like this project, consider giving it a star!
