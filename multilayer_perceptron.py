import numpy as np
import random as rd
import matplotlib.pyplot as plt

ENTRADAS = 1
class MultilayerPerceptron:

    def __init__(
        self,
        neurons: int,
        alpha: float,
        x_max: float,
        x_min: float,
        samples: int,
        tolerated_error: float,
        root
    ) -> None:
        self.alpha = alpha
        self.x_max = x_max
        self.x_min = x_min
        self.samples = samples
        self.neurons = neurons
        self.tolerated_error = tolerated_error
        self.listaciclo=[]
        self.listaerro=[]
        self.root = root

    def initialize(self, graph1, graph2, graph3):
        x1 = np.linspace(self.x_min, self.x_max, self.samples)
        x = np.zeros((self.samples, 1))
        for i in range(self.samples):
            x[i][0] = x1[i]
        (amostras, vsai) = np.shape(x)

        t1 = (np.cos(2*x))*(np.sin(x/2))
        t = np.zeros((1, amostras))
        for i in range(amostras):
            t[0][i] = t1[i]
        (vsai, amostras) = np.shape(t)

        vanterior = np.zeros((ENTRADAS, self.neurons))

        for i in range(ENTRADAS):
            for j in range(self.neurons):
                vanterior[i][j] = rd.uniform(-1, 1)
        v0anterior = np.zeros((1, self.neurons))
        for j in range(self.neurons):
            v0anterior[0][j] = rd.uniform(-1, 1)

        wanterior = np.zeros((self.neurons, vsai))
        for i in range(self.neurons):
            for j in range(vsai):
                wanterior[i][j] = rd.uniform(-0.2, 0.2)
        w0anterior = np.zeros((1, vsai))
        for j in range(vsai):
            w0anterior = np.zeros((1, vsai))

        vnovo = np.zeros((ENTRADAS, self.neurons))
        v0novo = np.zeros((1, self.neurons))
        wnovo = np.zeros((self.neurons, vsai))
        w0novo = np.zeros((1, vsai))
        zin = np.zeros((1, self.neurons))
        z = np.zeros((1, self.neurons))
        deltinhak = np.zeros((vsai, 1))
        deltaw0 = np.zeros((vsai, 1))
        deltinha = np.zeros((1, self.neurons))
        xaux = np.zeros((1, ENTRADAS))
        h = np.zeros((vsai, 1))
        target = np.zeros((vsai, 1))
        deltinha2 = np.zeros((self.neurons, 1))
        ciclo = 0
        errototal = 100000

        while self.tolerated_error < errototal:
            errototal = 0
            for padrao in range(amostras):
                for j in range(self.neurons):
                    zin[0][j] = np.dot(x[padrao, :], vanterior[:, j]) + v0anterior[0][j]
                z = np.tanh(zin)
                yin = np.dot(z, wanterior) + w0anterior
                y = np.tanh(yin)

                for m in range(vsai):
                    h[m][0] = y[0][m]
                for m in range(vsai):
                    target[m][0] = t[0][padrao]

                errototal = errototal + np.sum(0.5*((target-h)**2))

                deltinhak = (target-h)*(1+h)*(1-h)
                deltaw = self.alpha*(np.dot(deltinhak, z))
                deltaw0 = self.alpha*deltinhak
                deltinhain = np.dot(np.transpose(deltinhak),
                                    np.transpose(wanterior))
                deltinha = deltinhain*(1+z)*(1-z)

                for m in range(self.neurons):
                    deltinha2[m][0] = deltinha[0][m]
                for k in range(ENTRADAS):
                    xaux[0][k] = x[padrao][k]

                deltav = self.alpha*np.dot(deltinha2, xaux)
                deltav0 = self.alpha*deltinha

                vnovo = vanterior+np.transpose(deltav)
                v0novo = v0anterior+np.transpose(deltav0)
                wnovo = wanterior+np.transpose(deltaw)
                wonovo = w0anterior+np.transpose(deltaw0)
                vanterior = vnovo
                v0anterior = v0novo
                wanterior = wnovo
                w0anterior = w0novo

            ciclo = ciclo+1
            self.listaciclo.append(ciclo)
            self.listaerro.append(errototal)
            print('Ciclo\t Erro')
            print(ciclo,'\t',errototal)

            zin2 = np.zeros((1, self.neurons))
            z2 = np.zeros((1, self.neurons))
            t2 = np.zeros((amostras, 1))

            for i in range(amostras):
                for j in range(self.neurons):
                    zin2[0][j] = np.dot(
                        x[i, :], vanterior[:, j]) + v0anterior[0][j]
                    z2 = np.tanh(zin2)
                yin2 = np.dot(z2, wanterior) + w0anterior
                y2 = np.tanh(yin2)

                t2[i][0] = y2
            
                
            plt.clf()
            graph1[1].cla()
            graph1[1].plot(x, t2)
            graph1[1].set_title("Função Aproximada")
            graph1[0].draw()
            graph1[0].get_tk_widget().grid(row=0, column=2, rowspan=10, padx=(5, 0), pady=5, sticky='E')

            graph2[1].cla()
            graph2[1].plot(x, t2)
            graph2[1].plot(x, t1)
            graph2[1].set_title("Aproximação MLP x Real")
            graph2[0].draw()
            graph2[0].get_tk_widget().grid(row=0, column=0, padx=(0, 5), pady=5)

            graph3[1].cla()
            graph3[1].plot(self.listaciclo, self.listaerro)
            graph3[1].set_title("Erro por ciclo")
            graph3[0].draw()
            graph3[0].get_tk_widget().grid(row=0, column=1, padx=(5, 0), pady=5)

            self.root.update_idletasks()
            self.root.update()

            
