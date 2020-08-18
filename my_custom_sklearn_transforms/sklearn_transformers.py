from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Substituindo os valores nulos para NOTA_GO pela média
        data['NOTA_GO'] = data['NOTA_GO'].fillna(round(data['NOTA_GO'].mean(),1))     

        # Preenchendo 0 os alunos que não apresentam dados sobre o ingles
        data["INGLES"] = data["INGLES"].fillna(0)
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
