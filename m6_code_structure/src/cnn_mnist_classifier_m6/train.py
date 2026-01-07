from cnn_mnist_classifier_m6.model import Model
from cnn_mnist_classifier_m6.data import MyDataset

def train():
    dataset = MyDataset("data/raw")
    model = Model()
    # add rest of your training code here

if __name__ == "__main__":
    train()
