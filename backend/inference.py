import os
import torch
import numpy as np

from model.architecture import UNet
from preprocessing import MRIProcessor
from visualization import MRIVisualizer


class BrainTumorPredictor:
    """
    U-Net Brain Tumor Segmentation Inference Engine
    """

    def __init__(
        self,
        model_path="model/model.pth"
    ):

        # Device selection
        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        print(f"Running on {self.device}")


        # Initialize model
        self.model = UNet(
            in_channels=1,
            out_channels=1
        ).to(self.device)


        # Load trained weights
        self.load_model(model_path)


        # Initialize preprocessing
        self.processor = MRIProcessor()


        # Initialize visualizer
        self.visualizer = MRIVisualizer()


    def load_model(
        self,
        model_path
    ):
        """
        Load trained U-Net weights
        """

        if not os.path.exists(model_path):

            raise FileNotFoundError(
                f"Model not found: {model_path}"
            )


        weights = torch.load(
            model_path,
            map_location=self.device
        )


        self.model.load_state_dict(
            weights
        )


        self.model.eval()


        print(
            "Model loaded successfully"
        )


    def predict(
        self,
        file_path,
        threshold=0.5
    ):
        """
        Complete MRI prediction pipeline
        """


        # Preprocess MRI
        image_tensor = self.processor.preprocess(
            file_path
        )


        # Save original image for visualization
        original_image = image_tensor.clone()


        # Add batch dimension
        image_tensor = (
            image_tensor
            .unsqueeze(0)
            .to(self.device)
        )


        with torch.no_grad():

            logits = self.model(
                image_tensor
            )


            probabilities = torch.sigmoid(
                logits
            )


        # Convert to numpy
        probability_map = (
            probabilities
            .cpu()
            .squeeze()
            .numpy()
        )


        # Create binary mask
        binary_mask = (
            probability_map > threshold
        ).astype(
            np.uint8
        )


        # Calculate tumor area
        tumor_pixels = np.sum(
            binary_mask
        )


        total_pixels = (
            binary_mask.shape[0]
            *
            binary_mask.shape[1]
        )


        tumor_percentage = (
            tumor_pixels / total_pixels
        ) * 100


        # Calculate confidence
        if tumor_pixels > 0:

            confidence = np.mean(
                probability_map[
                    binary_mask == 1
                ]
            )

        else:

            confidence = 0


        # Generate visualization images
        image_paths = (
            self.visualizer.save_results(
                original_image,
                binary_mask
            )
        )


        # Final AI report
        return {

            "tumor_detected":
                bool(tumor_pixels > 0),


            "tumor_area_pixels":
                int(tumor_pixels),


            "tumor_percentage":
                round(
                    float(tumor_percentage),
                    3
                ),


            "confidence":
                round(
                    float(confidence * 100),
                    2
                ),


            "mask":
                binary_mask,


            "probability_map":
                probability_map,


            "images":
                image_paths
        }


# -------------------------------
# Testing
# -------------------------------

if __name__ == "__main__":

    predictor = BrainTumorPredictor(
        model_path="model/model.pth"
    )


    result = predictor.predict(
        "sample.nii"
    )


    print(
        "\n===== NeuroLens AI Report ====="
    )


    print(
        "Tumor Detected:",
        result["tumor_detected"]
    )


    print(
        "Tumor Area:",
        result["tumor_area_pixels"],
        "pixels"
    )


    print(
        "Affected Region:",
        result["tumor_percentage"],
        "%"
    )


    print(
        "Confidence:",
        result["confidence"],
        "%"
    )


    print(
        "\nGenerated Visualizations:"
    )


    for name, path in result[
        "images"
    ].items():

        print(
            f"{name}: {path}"
        )