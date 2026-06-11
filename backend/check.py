import torch

try:
    weights = torch.load(
        "model/model.pth",
        map_location="cpu"
    )

    print("Model loaded successfully!")
    print(type(weights))

    print("\nSome keys:")
    print(list(weights.keys())[:5])

except Exception as e:
    print("Error:", e)