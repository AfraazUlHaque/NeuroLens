import torch
import torch.nn as nn


class DoubleConv(nn.Module):
    """
    Two consecutive convolution blocks:
    Conv -> BatchNorm -> ReLU
    """

    def __init__(self, in_channels, out_channels):
        super().__init__()

        self.conv = nn.Sequential(

            nn.Conv2d(
                in_channels,
                out_channels,
                kernel_size=3,
                padding=1,
                bias=False
            ),

            nn.BatchNorm2d(out_channels),

            nn.ReLU(inplace=True),

            nn.Conv2d(
                out_channels,
                out_channels,
                kernel_size=3,
                padding=1,
                bias=False
            ),

            nn.BatchNorm2d(out_channels),

            nn.ReLU(inplace=True)
        )


    def forward(self, x):
        return self.conv(x)


class UNet(nn.Module):

    def __init__(
        self,
        in_channels=1,
        out_channels=1,
        features=[64, 128, 256, 512]
    ):
        super().__init__()

        self.downs = nn.ModuleList()
        self.ups = nn.ModuleList()

        self.pool = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )


        # Encoder
        for feature in features:

            self.downs.append(
                DoubleConv(
                    in_channels,
                    feature
                )
            )

            in_channels = feature


        # Bottleneck
        self.bottleneck = DoubleConv(
            features[-1],
            features[-1] * 2
        )


        # Decoder
        for feature in reversed(features):

            # Upsampling
            self.ups.append(
                nn.ConvTranspose2d(
                    feature * 2,
                    feature,
                    kernel_size=2,
                    stride=2
                )
            )


            # Double convolution
            self.ups.append(
                DoubleConv(
                    feature * 2,
                    feature
                )
            )


        # Final 1x1 convolution
        self.final_conv = nn.Conv2d(
            features[0],
            out_channels,
            kernel_size=1
        )


    def forward(self, x):

        skip_connections = []


        # Encoder path
        for down in self.downs:

            x = down(x)

            skip_connections.append(x)

            x = self.pool(x)


        # Bottleneck
        x = self.bottleneck(x)


        # Reverse skip connections
        skip_connections = skip_connections[::-1]


        # Decoder path
        for idx in range(0, len(self.ups), 2):

            x = self.ups[idx](x)

            skip = skip_connections[idx // 2]


            # Handle size mismatch
            if x.shape != skip.shape:

                x = nn.functional.interpolate(
                    x,
                    size=skip.shape[2:]
                )


            # Skip connection
            x = torch.cat(
                [skip, x],
                dim=1
            )


            x = self.ups[idx + 1](x)


        # Return raw logits
        return self.final_conv(x)


# Test model
if __name__ == "__main__":

    model = UNet(
        in_channels=1,
        out_channels=1
    )


    sample = torch.randn(
        1,
        1,
        240,
        240
    )


    output = model(sample)


    print("Input Shape :", sample.shape)

    print("Output Shape:", output.shape)