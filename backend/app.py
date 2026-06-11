import os
import uuid
import shutil

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException
)

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from inference import BrainTumorPredictor
from report_generator import ReportGenerator


# ======================================
# Initialize FastAPI
# ======================================

app = FastAPI(
    title="NeuroLens AI API",
    description="AI Powered Brain Tumor Segmentation",
    version="2.0"
)


# ======================================
# CORS Configuration
# ======================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ======================================
# Directories
# ======================================

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


# ======================================
# Serve generated images
# ======================================

app.mount(
    "/outputs",
    StaticFiles(directory=OUTPUT_DIR),
    name="outputs"
)


# ======================================
# Load AI Components
# ======================================

print("\nLoading NeuroLens AI...")

predictor = BrainTumorPredictor(
    model_path="model/model.pth"
)

report_generator = ReportGenerator()

print("NeuroLens AI Ready!\n")


# ======================================
# Health Check
# ======================================

@app.get("/")
def home():

    return {
        "message": "NeuroLens AI Backend Running",
        "status": "healthy"
    }


# ======================================
# Prediction API
# ======================================

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    filepath = None

    try:

        # Validate MRI file
        filename = file.filename.lower()

        if not (
            filename.endswith(".nii")
            or filename.endswith(".nii.gz")
        ):

            raise HTTPException(
                status_code=400,
                detail="Only NIfTI MRI files are supported"
            )


        # Create unique filename
        unique_name = (
            str(uuid.uuid4())
            + "_"
            + file.filename
        )


        filepath = os.path.join(
            UPLOAD_DIR,
            unique_name
        )


        # Save uploaded file
        with open(
            filepath,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )


        # Run AI prediction
        result = predictor.predict(
            filepath
        )


        # Remove heavy arrays
        result.pop(
            "mask",
            None
        )

        result.pop(
            "probability_map",
            None
        )


        # Convert image paths to URLs
        image_urls = {}

        for name, path in result[
            "images"
        ].items():

            image_urls[name] = (
                "/outputs/"
                + os.path.basename(path)
            )


        result["images"] = image_urls


        # =================================
        # Generate AI Medical Report
        # =================================

        result["report"] = (
            report_generator.generate(
                result
            )
        )


        # Final Response
        return {
            "success": True,
            "data": result
        }


    except HTTPException as e:

        raise e


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


    finally:

        # Delete uploaded MRI
        if (
            filepath
            and os.path.exists(filepath)
        ):

            os.remove(filepath)



# ======================================
# About API
# ======================================

@app.get("/about")
def about():

    return {

        "project":
            "NeuroLens AI",

        "version":
            "2.0",

        "model":
            "U-Net",

        "dataset":
            "BraTS 2020",

        "framework":
            "PyTorch + FastAPI + React",

        "features": [

            "Brain Tumor Segmentation",

            "MRI Visualization",

            "Tumor Area Analysis",

            "Confidence Estimation",

            "AI Medical Report",

            "Risk Assessment"
        ]
    }