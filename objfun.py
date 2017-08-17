'''
# Function:         S_MSE= objfun(FVr_temp, S_struct)
# Author:           Rainer Storn
# Description:      Implements the cost function to be minimized.
# Parameters:       FVr_temp     (I)    Paramter vector
#                   S_Struct     (I)    Contains a variety of parameters.
#                                       For details see Rundeopt.m
# Return value:     S_MSE.I_nc   (O)    Number of constraints
#                   S_MSE.FVr_ca (O)    Constraint values. 0 means the constraints
#                                       are met. Values > 0 measure the distance
%                                       to a particular constraint.
%                   S_MSE.I_no   (O)    Number of objectives.
%                   S_MSE.FVr_oa (O)    Objective function values.
# Worth investigating https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html
'''
import numpy as np

def objfun(FVr_temp, S_struct):
	load reg
	y = shape(regressorX)
	# y(2) is the number of features
	theta = np.zeros(y[2], 1);
	for i in range(1, y[2]):
		theta[i] = FVr_temp[i];

	theta0 = FVr_temp[y[2] + 1]
	F_cost = np.linalg.norm((regressorY.T - (regressorX * theta + theta0)))

	# %---Peaks function----------------------------------------------
	# F_cost = peaks(FVr_temp(1),FVr_temp(2));
	#----strategy to put everything into a cost function------------
	S_MSE.I_nc = 0; # no constraints
	S_MSE.FVr_ca = 0; # no constraint array
	S_MSE.I_no = 1; # number of objectives (costs)
	S_MSE.FVr_oa[1] = F_cost;

	return S_MSE