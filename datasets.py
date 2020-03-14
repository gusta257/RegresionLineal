import numpy as np

TRAINING_ELEMENTS = 200
x = np.linspace(
    -10,
    30,
    TRAINING_ELEMENTS
)

X = np.vstack(
    (
        np.ones(TRAINING_ELEMENTS),
        x,
        # x ** 2,
        x ** 3,
    )
).T

# y = x ** 3 + 50 - 100 * np.random.rand(TRAINING_ELEMENTS)
y = 5 + 2 * x ** 3 + np.random.randint(-15, 15, TRAINING_ELEMENTS)
dataset_1 = (X, y.reshape(TRAINING_ELEMENTS, 1))
