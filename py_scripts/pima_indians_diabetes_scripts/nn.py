import numpy as np
import torch as tor
import torch.nn as nn
import torch.optim as optim

# load the dataset, split into input (X) and output (y) variables
dataset = np.loadtxt('train_data/pima-indians-diabetes.csv', delimiter=',', skiprows=1)

X = dataset[:,0:8]
y = dataset[:,8]

X = tor.tensor(X, dtype=tor.float32)
y = tor.tensor(y, dtype=tor.float32).reshape(-1, 1)

class PimaDiabetesModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.input = nn.Linear(8, 12)
        self.act_input = nn.ReLU()
        self.hidden1 = nn.Linear(12, 8)
        self.act1 = nn.ReLU()
        self.output = nn.Linear(8, 1)
        self.act_output = nn.Sigmoid()

    def forward(self, x):
        x = self.act_input(self.input(x))
        x = self.act1(self.hidden1(x))
        x = self.act_output(self.output(x))
        return x
    
model = PimaDiabetesModel()
# print(model)

loss_fn = nn.BCELoss()  # binary cross entropy
optimizer = optim.Adam(model.parameters(), lr=0.001)

n_epochs = 100
batch_size = 10

for epoch in range(n_epochs):
    for i in range(0, len(X), batch_size):
        Xbatch = X[i:i+batch_size]
        y_pred = model(Xbatch)
        ybatch = y[i:i+batch_size]
        loss = loss_fn(y_pred, ybatch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f'Finished epoch {epoch}, latest loss {loss}')

# compute accuracy (no_grad is optional)
with tor.no_grad():
    y_pred = model(X)

accuracy = (y_pred.round() == y).float().mean()
print(f"Accuracy {accuracy}")