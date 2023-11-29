# -*- coding: utf-8 -*-
"""Studi Kasus 1: Predictive Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M9mQcdB2mTuazDBluvzwSYYXSB3LRe9I
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

from google.colab import files

"""# Data Loading

Melakukan installasi untuk mengambil data dari Kaggle
"""

!pip install q kaggle

"""Meng-upload file kaggle.json yang berisi Kaggle API sehingga memungkinkan untuk mengambil data dari Kaggle"""

files.upload()

! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json

"""Mengunduh dataset **Travel Insurance Prediction Data** yang dapat diakses melalui link berikut: https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data"""

!kaggle datasets download -d tejashvi14/travel-insurance-prediction-data

! unzip /content/travel-insurance-prediction-data.zip

df = pd.read_csv("/content/TravelInsurancePrediction.csv")

df

"""Berdasarkan output di atas di dalam dataset ini terdapat:
* 10 kolom
* 1987 baris

# Exploratory Data Analysis (EDA)

Mengambil informasi mengenai deskripsi variabel yang terdapat di dalam dataset ini
"""

df.info()

"""Berdasarkan output di atas, terlihat bahwa dalam dataset ini terdapat 6 kolom dengan tipe int64 dan 4 kolom dengan tipe object"""

df.describe()

"""Memeriksa apakah terdapat data null di setiap kolom"""

df.isnull().sum()

"""Memeriksa apakah terdapat data duplicate"""

df.duplicated().sum()

"""## Menangani Outlier"""

sns.boxplot(x=df['Age'])

sns.boxplot(x=df['AnnualIncome'])

sns.boxplot(x=df['FamilyMembers'])

sns.boxplot(x=df['ChronicDiseases'])

sns.boxplot(x=df['TravelInsurance'])

"""Berdasarkan visualisasi Box Plot di atas, tidak terlihat adanya outliers di dalam dataset ini. Namun, untuk lebih pasti, saya menerapkan metode IQR untuk menghapus data yang memiliki outliers"""

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR=Q3-Q1

df=df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]

df.shape

"""# Univariate Analysis

Membagi fitur-fitur yang ada di dalam dataset menjadi dua fitur, yaitu numerical_features dan categorical_features
"""

numerical_features = ['Age', 'AnnualIncome', 'FamilyMembers', 'ChronicDiseases', 'TravelInsurance']
categorical_features = ['Employment Type', 'GraduateOrNot', 'FrequentFlyer', 'EverTravelledAbroad']

"""## Categorical features"""

feature = categorical_features[0]

count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)

df_feature = pd.DataFrame({'Jumlah Data':count, 'Persentase':percent.round(1)})

print(df_feature)
count.plot(kind='bar', title=feature);

"""Di dalam fitur 'Employment Type' terdapat dua kategori yaitu Private Sector/Self Employed dengan jumlah terbanyak dengan persentase 71.31% dan Goverment Sector dengan persentase 28.69%"""

feature = categorical_features[1]

count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)

df_feature = pd.DataFrame({'Jumlah Data':count, 'Persentase':percent.round(1)})
print(df_feature)

count.plot(kind='bar', title=feature);

"""Di dalam fitur 'GraduateOrNot' terdapat dua kategori yaitu Yes dengan persentase sebesar 85.2% dan No dengan persentase 14.8%"""

feature = categorical_features[2]

count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)

df_feature = pd.DataFrame({'Jumlah Data':count, 'Persentase':percent.round(1)})
print(df_feature)

count.plot(kind='bar', title=feature);

"""Di dalam fitur 'FrequentFlyer' terdapat dua kategori yaitu No dengan persentase sebesar 79% dan Yes dengan persentase 21%"""

feature = categorical_features[3]
count = df[feature].value_counts()
percent = 100*df[feature].value_counts(normalize=True)
df_feature = pd.DataFrame({'Jumlah Data':count, 'Persentase':percent.round(1)})
print(df_feature)
count.plot(kind='bar', title=feature);

"""Di dalam fitur 'EverTravelledAbroad' terdapat dua kategori yaitu No dengan persentase sebesar 80.9% dan Yes dengan persentase 19.1%

## Numerical features
"""

df.hist(bins=30, figsize=(30, 25))
plt.show()

"""Berdasarkan histogram di atas, dapat disimpulkan bahwa:
* Data didominasi oleh customer yang berusia 28 tahun
* Kategori jumlah anggota keluarga yang tinggal bersama customer terbanyak adalah 4 orang dan tersedikit adalah 9 orang
* Jumlah customer yang tidak memiliki chronic disease atau penyakit kronis lebih dari setengah jumlah customer yang memiliki penyakit kronis
* Jumlah customer yang tidak memiliki asuransi perjalanan lebih banyak daripada customer yang memiliki asuransi perjalanan

# Multivariate analysis

Memeriksa rata-rata fitur TravelInsurance terhadap setiap fitur kategori
"""

categorical_features = df.select_dtypes(include='object').columns.to_list()

for col in categorical_features:
  sns.catplot(x=col, y="TravelInsurance", kind="bar", dodge=False, height = 4, aspect = 2,  data=df, palette="pastel")
  plt.title("Rata-rata Travel Insurance Relatif terhadap - {}".format(col))

"""Berdasarkan diagram di atas, dapat disimpulkan bahwa:
* Pada fitur EmploymentType, kategori Private Sector/Private Employed memiliki pengaruh terhadap pembelian asuransi perjalanan
* Rata-rata pembelian asuransi perjalanan terhadap fitur GraduateOrNot cenderung mirip
* Fitur FrequentFlyer dengan kategori Yes memiliki pengaruh yang signifikan terhadap pembelian asuransi perjalanan
* Pada fitur EverTravelledAbroad, customer sudah pernah pergi ke luar negeri memiliki pengaruh yang tinggi terhadap pembelian asuransi perjalanan

Selanjutnya menampilkan visualisasi relasi antara fitur-fitur numerik dengan fitur 'TravelInsurance' menggunakan pairplot
"""

sns.pairplot(df, diag_kind = 'kde')

"""Selanjutnya menampilkan korelasi antar fitur numerik menggunakan correlation matrix"""

plt.figure(figsize=(10, 8))
correlation_matrix = df.corr().round(2)

sns.heatmap(data=correlation_matrix, annot=True, cmap='magma', linewidths=0.5, )
plt.title("Correlation Matrix antar Fitur Numerik ", size=20)

"""Berdasarkan correlation matrix di atas, korelasi antara fitur 'Unnamed: 0' dengan fitur lainnya memiliki korelasi yang sangat rendah sehingga fitur tersebut akan dihilangkan"""

df.drop(['Unnamed: 0'], inplace=True, axis=1)
df.head()

"""# Data Preparation

## Encoding Fitur Kategori

Melakukan encoding fitur kategori menggunakan teknik one-hot-encoding yang telah disediakan oleh library scikit-learn
"""

from sklearn.preprocessing import  OneHotEncoder

df = pd.concat([df, pd.get_dummies(df['Employment Type'], prefix='Employment Type')],axis=1)
df = pd.concat([df, pd.get_dummies(df['GraduateOrNot'], prefix='GraduateOrNot')],axis=1)
df = pd.concat([df, pd.get_dummies(df['FrequentFlyer'], prefix='FrequentFlyer')],axis=1)
df = pd.concat([df, pd.get_dummies(df['EverTravelledAbroad'], prefix='EverTravelledAbroad')],axis=1)

df.drop(['Employment Type','GraduateOrNot','FrequentFlyer', 'EverTravelledAbroad'], axis=1, inplace=True)
df.head()

"""## Train-Test-Split

Memecah dataset menjadi data training dan data testing dengan 'test_size = 0.2' atau proporsinya 80:20, 80% data training dan 20% data testing menggunakan library scikit-learn train_test_split
"""

from sklearn.model_selection import train_test_split

X = df.drop(["TravelInsurance"],axis =1)
y = df["TravelInsurance"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

print(f'Total jumlah seluruh data: {len(X)}')
print(f'Total data train: {len(X_train)}')
print(f'Total data test: {len(X_test)}')

"""## Standarisasi

Melakukan standarisasi pada fitur numerik menggunakan teknik StandardScaler yang telah disediakan oleh library scikit-learn
"""

from sklearn.preprocessing import StandardScaler

numerical_features = ['Age', 'AnnualIncome', 'FamilyMembers', 'ChronicDiseases']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

X_train[numerical_features].describe().round(2)

"""Nilai mean telah berubah menjadi 0 dan nilai standar deviasi menjadi 1

# Modelling

Menyiapkan dataframe untuk menyimpan hasil analisis model dengan kolom yang terdiri dari 'KNN', 'RandomForest', dan 'Boosting'
"""

models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

"""## Melatih data menggunakan algoritma KNN"""

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(n_neighbors=7)
knn.fit(X_train, y_train)

models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""## Melatih data menggunakan algoritma Random Forest"""

from sklearn.ensemble import RandomForestRegressor

RF = RandomForestRegressor(n_estimators=20, max_depth=15, random_state=123, n_jobs=-1)
RF.fit(X_train, y_train)

models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""## Melatih data menggunakan algoritma Boosting"""

from sklearn.ensemble import AdaBoostRegressor

boosting = AdaBoostRegressor(learning_rate=0.05, random_state=123)
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""# Evaluasi Model

Melakukan scaling terhadap fitur numerik yang terdapat dalam X_test sehingga memiliki rata-rata sebesar 0 dan varians sebesar 1
"""

X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])

model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}

for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3

mse

"""Melakukan plot hasil mse di atas menggunakan bar chart"""

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""Selanjutnya dilakukan prediksi pengujian menggunakan data testing"""

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(2)

pd.DataFrame(pred_dict)

"""Berdasarkan hasil pengujian, terlihat bahwa algoritma Random Forest memberikan hasil yang mendekati."""