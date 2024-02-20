import numpy as np
import matplotlib.pyplot as plt
import os
from random import randint, choice

operations = {
    0: lambda x, y: x + y,
    1: lambda x, y: x - y,
    2: lambda x, y: x * y    
}

def operate_terms(x, y, cross_term, c, function_list, x_terms=True, y_terms=True, cross_terms=True, multiply=True):
    mod = 1 if multiply else 0
    len_func_list = len(function_list)

    img1 = function_list[c % len_func_list](x) if x_terms else mod
    c += 1
    img2 = function_list[c % len_func_list](y) if y_terms else mod
    c += 1
    img3 = function_list[c % len_func_list](cross_term) if cross_terms else mod
    c += 1

    img = img1 * img2 * img3 if multiply else img1 + img2 + img3

    return img, c

def generate_image(x, y, nmax, operation, function_list, multiply=True, **kwargs):
    c = 0
    img, c = operate_terms(x, y, operations[operation](x, y), c, function_list, **kwargs, multiply=multiply)

    while c < len(function_list):
        new_img, c = operate_terms(x, y, operations[operation](x, y), c, function_list, **kwargs, multiply=multiply)
        img = img * new_img if multiply else img + new_img

    img = img / abs(img).max() * nmax
    return img

if __name__ == '__main__':
    data_folder = 'dataset'
    real_folder = 'unwrapped'
    wrapped_folder = 'wrapped'
    n_images = 4000
    start_number = 1
    img_size = 128
    size = complex(f'{img_size}j')

    os.makedirs(os.path.join(data_folder, real_folder), exist_ok=True)
    os.makedirs(os.path.join(data_folder, wrapped_folder), exist_ok=True)

    x, y = np.mgrid[-1:1:size, -1:1:size]
    nmax = 2 * np.pi

    function_list = [np.sin, np.cos, np.sinh, np.cosh, np.tan, np.tanh, np.exp]
    x_variations = [x, x ** 2, x ** 3, x ** 4]
    y_variations = [y, y ** 2, y ** 3, y ** 4]

    for n in range(n_images):
        x_factor = randint(-3, 3) or 1
        y_factor = randint(-3, 3) or 1
        nm = nmax

        f_list = [choice(function_list) for _ in range(randint(2, len(function_list)))]

        multiply = bool(randint(0, 1))
        x_terms = bool(randint(0, 1))
        y_terms = bool(randint(0, 1))
        cross_terms = bool(randint(0, 1))
        operation = randint(0, len(operations) - 1)

        while not x_terms and not y_terms and not cross_terms:
            x_terms = bool(randint(0, 1))
            y_terms = bool(randint(0, 1))
            cross_terms = bool(randint(0, 1))

        x_index = np.random.randint(len(x_variations))
        y_index = np.random.randint(len(y_variations))

        img = generate_image(x_variations[x_index] * x_factor, y_variations[y_index] * y_factor, nm, operation, f_list,
                             multiply=multiply, x_terms=x_terms, y_terms=y_terms, cross_terms=cross_terms)

        filename = f'{n + start_number}.png'
        plt.imsave(os.path.join(data_folder, real_folder, filename), img, cmap='gray')
        plt.close()

        wrapped_img = np.angle(np.exp(1j * img))
        plt.imsave(os.path.join(data_folder, wrapped_folder, filename), wrapped_img, cmap='gray')
        plt.close()
