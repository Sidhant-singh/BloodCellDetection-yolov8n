from albumentations import (
    RandomCrop, HorizontalFlip, Rotate, Resize, Compose
)
from albumentations.pytorch import ToTensorV2

def augment_image(image):
    transform = Compose([
        Rotate(limit=30),
        HorizontalFlip(p=0.5),
        RandomCrop(height=512, width=512),
        Resize(height=640, width=640),
        ToTensorV2()
    ])
    return transform(image=image)['image']
