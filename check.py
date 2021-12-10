import pickle
from sklearn.ensemble import RandomForestRegressor

model=pickle.load(open('Loan2.pkl','rb'))
print(model.predict([[5849,146.412162,1.0,0.0,360.0]]))