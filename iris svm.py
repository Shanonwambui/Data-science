<<<<<<< HEAD
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris=datasets.load_iris()
# print type of iris which is bunch
print(type(iris))
#data used
print(iris.data)
#data label
print(iris.feature_names)
#what we are going to predict
#0=sotosa, 1= Versicolour, 2=Virginica
print(iris.target)
print(iris.target_names)
#independent data in a column
X=iris.data[:,2]
#dependent variable
Y=iris.target
#we want to split our data into train data and test data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=4)
#since we expect a 1D array we reshape our data using the function array.reshape(-1,1)
X_train_mod=X_train.reshape(-1,1)
X_test_mod=X_test.reshape(-1,1)
Y_train_mod=Y_train.reshape(-1,1)
Y_test_mod=Y_test.reshape(-1,1)

model=svm.SVC(kernel='linear')
#kernel enables us to use hyperplane to classify data
model.fit(X_train_mod,Y_train_mod)
accuracy=model.score(X_test_mod,Y_test_mod)
print(accuracy)
#A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
Y_pred_mod=model.predict(X_test_mod)
print(accuracy_score(Y_pred_mod,Y_test_mod))


=======
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris=datasets.load_iris()
# print type of iris which is bunch
print(type(iris))
#data used
print(iris.data)
#data label
print(iris.feature_names)
#what we are going to predict
#0=sotosa, 1= Versicolour, 2=Virginica
print(iris.target)
print(iris.target_names)
#independent data in a column
X=iris.data[:,2]
#dependent variable
Y=iris.target
#we want to split our data into train data and test data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=4)
#since we expect a 1D array we reshape our data using the function array.reshape(-1,1)
X_train_mod=X_train.reshape(-1,1)
X_test_mod=X_test.reshape(-1,1)
Y_train_mod=Y_train.reshape(-1,1)
Y_test_mod=Y_test.reshape(-1,1)

model=svm.SVC(kernel='linear')
#kernel enables us to use hyperplane to classify data
model.fit(X_train_mod,Y_train_mod)
accuracy=model.score(X_test_mod,Y_test_mod)
print(accuracy)
#A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
Y_pred_mod=model.predict(X_test_mod)
print(accuracy_score(Y_pred_mod,Y_test_mod))


>>>>>>> cb0442981804a4bd26308da9c81af8aa1405141f
