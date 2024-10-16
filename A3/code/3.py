import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange
import pickle



#using custom OLS

#augmenting the data with powers of x

def fit(DegreeofFit = 1 , plot = True, validate = 0.8):

    validate = 1- validate
    # Load the data
    
    data = np.genfromtxt('train.csv', delimiter=',', skip_header=1, usecols=(1,2))
    

    # Split the data into training and validation sets
    
    np.random.shuffle(data)

    split_index = int(validate * len(data))

    data_x = data[:, 0]
    data_y = data[:, 1]

    data_x = data_x.reshape(-1,1)
    data_y = data_y.reshape(-1,1)
    
    #augmenting the data with powers of x
    data_x = np.hstack((np.ones((data_x.shape[0],1)),data_x))
    for i in range(2,DegreeofFit+1):
        data_x = np.hstack((data_x,data_x[:,1].reshape(-1,1)**i))


    #split data into training and validation
    train_data_x = data_x[:split_index]
    train_data_y = data_y[:split_index]

    validate_data_x = data_x[split_index:]
    validate_data_y = data_y[split_index:]


    #calculate the parameters
    params_calulated = np.linalg.inv(np.transpose(train_data_x) @ (train_data_x)) @ np.transpose(train_data_x) @ train_data_y




    # Plot the data and the polynomial fit
    if plot:
        # Generate polynomial fit line
        x_fit = np.linspace(min(train_data_x[:, 1]), max(train_data_x[:, 1]), 100)
        x_fit_poly = np.vstack([x_fit**i for i in range(DegreeofFit + 1)]).T
        y_fit = x_fit_poly @ params_calulated
        plt.scatter(train_data_x[:, 1], train_data_y, color='blue', label='Training data',s=10)
        plt.plot(x_fit, y_fit, color='red', label='Polynomial fit')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Polynomial Fit of Degree {}'.format(DegreeofFit))
        plt.legend()
        plt.savefig('Degree{}.png'.format(DegreeofFit) , dpi = 300)

    error_calculated = np.mean((validate_data_y - (validate_data_x @ params_calulated)) ** 2)
    
    # Calculate the sum of squared differences from the mean
    y_avg = np.mean(train_data_y)
    sum_squared_diff = np.sum((train_data_y - y_avg) ** 2)

    # Calculate the sum of squared residuals (SSR)
    ssr = np.sum((train_data_y - (train_data_x @ params_calulated)) ** 2)

    # Calculate the coefficient of determination (R)
    R = (1 - (ssr / sum_squared_diff))**0.5
    
    return error_calculated,params_calulated,R

def run(params_calculated):
    # Load the test data
    
    with open('test.csv', 'r') as file:
        test_id = [line.split(',')[0] for line in file.readlines()[1:]]
    
    test_data = np.genfromtxt('test.csv', delimiter=',', skip_header=1, usecols=(0,1))
    
    print(test_data[:5])
    test_x = test_data[:, 1].reshape(-1, 1)

    # Augment the test data with powers of x
    test_x = np.hstack((np.ones((test_x.shape[0], 1)), test_x))
    for i in range(2, params_calculated.shape[0]):
        test_x = np.hstack((test_x, test_x[:, 1].reshape(-1, 1) ** i))

    # Predict the values using the calculated parameters
    predicted_y = test_x @ params_calculated


    # Save the predicted values to result.csv
    print(test_id[:5])
    with open('result.csv', 'w') as f:
        f.write('id,x,y\n')
        for i in range(len(predicted_y)):
            f.write(f"{test_id[i]},{test_x[i, 1]},{predicted_y[i, 0]}\n")
            
    return predicted_y




n = 100
val = 0.1
FIND_BEST_DEGREE = False

if FIND_BEST_DEGREE:
    min_error_degree = []
    for j in trange(100):
        np.random.seed(j)
        errors = []
        for i in range(1, n):
            errors.append(fit(i,False,val)[0])

        min_error_index = np.argmin(errors) + 1
        min_error_degree.append(min_error_index)
        
        
    mode_degree = max(set(min_error_degree), key=min_error_degree.count)
    print(f"The mode of degree which gives minimum error is: {mode_degree}")


#finding coefficient of determination for different degrees and also plotting the fit
print(fit(2, True, 0)[2])
plt.show()
plt.clf()
print(fit(5, True, 0)[2])
plt.show()
plt.clf()
print(fit(20, True, 0)[2])
plt.show()

#saving params and running on test data
params = fit(5, False, 0)[1]
with open('3_weights.pkl', 'wb') as f:
    pickle.dump(params, f)
run(params)
