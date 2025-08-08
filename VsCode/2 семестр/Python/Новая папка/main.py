from random import random


def initial_data():
    weights = []
    for i in range(784):
        weights.append(random())
    b = random()
    return weights, b

def predict(image, weights, b):
    sum_pxl = 0
    for i in range(len(image)):
        sum_pxl += image[i] * weights[i]
    sum_pxl += b
    return 1 if sum_pxl > 0 else 0


def learn(weights, b, x, y):
    weights_l, b_l = weights.copy(), b
    for _ in range(30):
        for img_idx in range(len(x)):
            answer_model = predict(x[img_idx], weights_l, b_l)
            d_loss = 2 * (answer_model - y[img_idx])
            for i in range(len(weights_l)):
                weights_l[i] = weights_l[i] - 0.001 * x[img_idx][i] * d_loss
    return weights_l, b_l

def read_image():
    list_letter = []
    for i in range(28):
        for j in input():
            list_letter.append(1 if j == "+" else 0)
    return list_letter

    
x, y = load_data()
weights, b = initial_data()
weights, b = learn(weights, b, x, y)
list_letters = read_image()
print(predict(list_letters, weights, b))