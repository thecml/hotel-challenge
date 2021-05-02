import os
import torch
from torch.utils.data import Dataset
from skimage import io, transform
from PIL import Image

class HotelImagesDataset(Dataset):
    """Hotel images dataset."""

    def __init__(self, label_df, root_dir, transform=None):
        """
        Args:
            csv_file (string): Path to the csv file with annotations.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.label_df = label_df
        self.root_dir = root_dir
        self.transform = transform
        self.classes = list(self.label_df['hotel_id'].unique())


    def __len__(self):
        return 1;#len(self.label_df)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        #img_name = os.path.join(self.root_dir,
                                #self.label_df.iloc[idx, 0])

        img_name = os.path.join(self.root_dir, '800a4a6b6f6d2df6.jpg')
        image = io.imread(img_name)
        pil_image = Image.fromarray(image)
        
        y = int(self.label_df.loc[self.label_df['image'] == '800a4a6b6f6d2df6.jpg']['label']) # for testing yo
        # y = self.label_df.iloc[idx, 4] # for reals yo
        if self.transform:
            X = self.transform(pil_image)

        return X, y

    # def class_to_index(self, class_name):
    #     """Returns the index of a given class."""
    #     return self.classes.index(class_name)
    
    # def index_to_class(self, class_index):
    #     """Returns the class of a given index."""
    #     return self.classes[class_index] 