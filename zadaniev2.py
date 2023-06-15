import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Info:
    def __init__(self, url):
        self.data = pd.read_csv(url)
    '''
    metoda główna
    '''
    def getAllInfo(self):
        a, b = self.getCountCollAndRows()
        ret = f'Liczba kolumn: {a}\n, Liczba wierszy: {b}\n'
        ret += "\n========================\n"
        ret += f'Wartość średniej: {self.getMean()}\n'
        ret += "\n========================\n"
        ret += f'Wartość odchylenia standardowego: {self.getStd()}\n'
        ret += "\n========================\n"
        ret += f'Warotość mediany: {self.getMedian()}\n'
        ret += "\n========================\n"
        ret += f'Wartość maksymalna\n: {self.getMax()}\n'
        ret += "\n========================\n"
        ret += f'Wartość minimalna\n: {self.getMin()}\n'
        return ret


    def getCountCollAndRows(self):
        '''
        zwrócenie informacji o liczbie kolumn i wierszy
        '''
        return self.data.shape[1], self.data.shape[0]


    def getMean(self):
        '''
        wartość średniej
        '''
        return self.data.mean()


    def getStd(self):
        '''
        Odchylenie standardowe
        '''
        return self.data.std()

    def getMedian(self):
        '''
        Wartość medioany
        :return: mediana
        '''
        return self.data.median()

    def getMax(self):
        '''
        zwraca wartość maksymalną dla każdej kolumny
        :return:
        '''
        return self.data.max()

    def getMin(self):
        '''
        zwraca wartość minimalną dla każdej kolumny
        :return:
        '''
        return self.data.min()

    def getMatrixCorrelation(self):
        '''
        :return: macirz koleracji zbioru danych
        '''
        return self.data.corr().round(2)


    def showCorelationValue(self):
        '''
        :return:
        '''
        sns.heatmap(self.getMatrixCorrelation(), annot=True, cmap="RdYlBu")
        plt.title("Macierz korelacji")
        plt.show()

    def showHistValue(self):
        '''

        :return:
        '''
        for column in self.data.columns:
            plt.hist(self.data[column])
            plt.xlabel(column)
            plt.ylabel("Liczba wystąpień")
            plt.title(f"Histogram rozkładu wartości - {column}")
            plt.show()


obj = Info("dane.csv")
print(obj.getAllInfo())
obj.showCorelationValue()
obj.showHistValue()