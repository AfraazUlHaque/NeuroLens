import os
import torch
import nibabel as nib
import numpy as np


class MRIProcessor:
    """
    MRI preprocessing for NeuroVision AI.
    Matches BraTS training pipeline.
    """

    def __init__(
        self,
        image_size=240,
        slice_index=75
    ):

        self.image_size = image_size
        self.slice_index = slice_index


    def load_nifti(self, file_path):
        """
        Load MRI NIfTI file.
        Supports .nii and .nii.gz
        """

        if not os.path.exists(file_path):

            raise FileNotFoundError(
                f"File not found: {file_path}"
            )


        image = (
            nib.load(file_path)
            .get_fdata()
        )

        return image


    def extract_slice(self, volume):
        """
        Extract same slice used in training.
        """

        if self.slice_index >= volume.shape[2]:

            raise ValueError(
                "Slice index exceeds MRI depth"
            )


        return volume[:, :, self.slice_index]


    def normalize(self, image):
        """
        Min-max normalization.
        """

        image = image.astype(
            np.float32
        )


        minimum = image.min()
        maximum = image.max()


        return (
            image - minimum
        ) / (
            maximum - minimum + 1e-8
        )


    def to_tensor(self, image):
        """
        Convert image to PyTorch tensor.

        H x W
          ↓
        1 x H x W
        """

        tensor = torch.tensor(
            image,
            dtype=torch.float32
        )


        tensor = tensor.unsqueeze(0)


        return tensor


    def preprocess(self, file_path):
        """
        Complete preprocessing pipeline.

        Output:
        (1, 240, 240)
        """

        # Load MRI volume
        volume = self.load_nifti(
            file_path
        )


        # Extract FLAIR slice 75
        image = self.extract_slice(
            volume
        )


        # Normalize
        image = self.normalize(
            image
        )


        # Convert to tensor
        tensor = self.to_tensor(
            image
        )


        return tensor



if __name__ == "__main__":

    processor = MRIProcessor()


    sample_file = (
        "sample_flair.nii"
    )


    try:

        output = processor.preprocess(
            sample_file
        )


        print(
            "Preprocessing successful"
        )

        print(
            "Tensor shape:",
            output.shape
        )


    except Exception as error:

        print(
            "Error:",
            error
        )