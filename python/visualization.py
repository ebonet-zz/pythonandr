# encoding=utf8

import matplotlib, matplotlib.pyplot as plt, numpy as np

matplotlib.style.use('ggplot')

def plot_results(expected, received):
    """
    Displays the result of the computed model.

    :param expected the actual value of the rental price
    :param received the value estimated by the model
    """
    plt.figure()
    plt.subplot(211)
    plt.plot(expected, received, 'ro')
    plt.xlabel(u"Preço Real")
    plt.ylabel(u"Preço Estimado")
    plt.title(u"Resultados para set de teste")

    plt.subplot(212)
    plt.hist(np.abs(expected - received), bins=30)
    plt.xlabel(u"Número de casos")
    plt.ylabel(u"Erro absoluto")

    plt.xlabel(u"Erro")
    plt.ylabel(u"Quantidade")
    plt.title("Resultados para o para teste")

def plot_scater_map(data):
    """
    Plots a map and the location of each rental unit at their coordinates.
    The colormap represents the rental price. Size of the points is inversely
    proportional to the price.

    :param data: the rental units tho be shown in the map
    """
    plt.figure();
    im = matplotlib.image.imread('flnp2.png');
    im[:, :, -1] = 0.7;
    plt.imshow(im, extent=[-48.68, -48.3, -27.85, -27.35])
    plt.scatter(data.longitude,
                data.latitude,
                c=data.rentPrice,
                s = 2000/np.sqrt(data.rentPrice))

    plt.colorbar()
    plt.axis([-48.68, -48.3, -27.85, -27.35])
    plt.title(u"Distribução dos Imóveis")