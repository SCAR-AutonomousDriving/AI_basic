from torch.utils.data import DataLoader, Dataset


class TrainDataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
    
    def len(self):
        return 0
    
    def forward(self,x):
        return x

class TestDataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
    
    def len(self):
        return 0
    
    def forward(self,x):
        return x