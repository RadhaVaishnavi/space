import os
from PIL import Image
import pandas as pd
from torch.utils.data import Dataset
import random

class SatelliteDataset(Dataset):
    def __init__(self, img_dir, caption_file, transform=None):
        self.img_dir = img_dir
        self.captions = pd.read_csv(caption_file)
        self.transform = transform

    def __len__(self):
        return len(self.captions)

    def __getitem__(self, idx):
        img_name = os.path.join(self.img_dir, self.captions.iloc[idx, 0])
        image = Image.open(img_name)

        if self.transform:
            image = self.transform(image)

        # Randomly select one caption from the five available
        captions = self.captions.iloc[idx, 1:6].tolist()
        caption = random.choice(captions)

        return image, caption
