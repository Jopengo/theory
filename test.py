import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('marketing_campaign.csv', sep='\t')

# Просмотр данных
print("\nПервые строки данных:\n")
print(df.head())
print("\nОбщая информация о данных:\n")
print(df.info())