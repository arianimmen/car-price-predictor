import mysql.connector as connector
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
import joblib


def fetch_data_from_mysql():
    # Connect to your MySQL database
    cnx = connector.connect(user='', password='',
                            host='127.0.0.1', database='')
    cursor = cnx.cursor()

    query = "SELECT car_name, car_year, car_mileage, car_accident, car_owner, car_price FROM car_datas;"
    cursor.execute(query)
    data = cursor.fetchall()

    columns = ['car_name', 'car_year', 'car_mileage',
               'car_accident', 'car_owner', 'car_price']
    df = pd.DataFrame(data, columns=columns)

    cursor.close()
    cnx.close()

    return df


# Fetch data from MySQL
car_data_df = fetch_data_from_mysql()

# Encode categorical variables (car_name, car_color)
label_encoder = LabelEncoder()
car_data_df['car_name_encoded'] = label_encoder.fit_transform(
    car_data_df['car_name'])


# Define features (X) and target variable (y)
features = ['car_name_encoded', 'car_year',
            'car_mileage', 'car_accident', 'car_owner']
target = 'car_price'

X = car_data_df[features]
y = car_data_df[target]

# Create and train the decision tree regression model
regression_tree = DecisionTreeRegressor()
regression_tree.fit(X, y)
label_encoder.fit(car_data_df['car_name'])

joblib.dump(regression_tree, 'trained_model.joblib')
joblib.dump(label_encoder, 'label_encoder.joblib')
