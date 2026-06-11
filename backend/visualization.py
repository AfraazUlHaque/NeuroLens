import os
import numpy as np
import matplotlib.pyplot as plt


class MRIVisualizer:

    def __init__(self):
        self.output_dir = "outputs"

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )


    def save_results(
        self,
        image,
        mask
    ):
        """
        Save MRI, mask and overlay images.
        """

        # Convert tensors if needed
        if hasattr(image, "cpu"):
            image = image.cpu().numpy()

        if hasattr(mask, "cpu"):
            mask = mask.cpu().numpy()


        image = np.squeeze(image)
        mask = np.squeeze(mask)


        paths = {}


        # ----------------------
        # Original MRI
        # ----------------------

        mri_path = os.path.join(
            self.output_dir,
            "mri.png"
        )

        plt.figure(figsize=(5,5))
        plt.imshow(
            image,
            cmap="gray"
        )
        plt.axis("off")

        plt.savefig(
            mri_path,
            bbox_inches="tight",
            pad_inches=0
        )

        plt.close()

        paths["mri"] = mri_path


        # ----------------------
        # Tumor Mask
        # ----------------------

        mask_path = os.path.join(
            self.output_dir,
            "mask.png"
        )

        plt.figure(figsize=(5,5))

        plt.imshow(
            mask,
            cmap="hot"
        )

        plt.axis("off")

        plt.savefig(
            mask_path,
            bbox_inches="tight",
            pad_inches=0
        )

        plt.close()


        paths["mask"] = mask_path


        # ----------------------
        # Overlay
        # ----------------------

        overlay_path = os.path.join(
            self.output_dir,
            "overlay.png"
        )


        plt.figure(figsize=(5,5))


        plt.imshow(
            image,
            cmap="gray"
        )

        plt.imshow(
            mask,
            cmap="jet",
            alpha=0.45
        )


        plt.axis("off")


        plt.savefig(
            overlay_path,
            bbox_inches="tight",
            pad_inches=0
        )


        plt.close()


        paths["overlay"] = overlay_path


        return paths