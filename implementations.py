# -*- coding: utf-8 -*-
import numpy as np


def mean_squared_error_gd(y, tx, initial_w, max_iters, gamma):
    """The Gradient Descent (GD) algorithm using MSE loss.
    
    Args:
        y: numpy array of shape=(N, )
        tx: numpy array of shape=(N,D)
        initial_w: numpy array of shape=(D, ). The initial guess (or the initialization) for the model parameters
        max_iters: a scalar denoting the total number of iterations of GD
        gamma: a scalar denoting the stepsize
        
    Returns:
        w: model parameters as numpy arrays of shape (D, )
        loss: loss mse value (scalar) 
    """
    
    # Initialize weights
    w = initial_w
    
    for i in range(max_iters):
        
        # compute loss, gradient
        grad = compute_gradient(y, tx, w, "mse")
        loss = compute_loss(y, tx, w, "mse")
        
        # update w by gradient descent
        w = w - gamma*grad
        
        # Display loss
        print("GD iter. {bi}/{ti}: loss={l}, w0={w0}, w1={w1}".format(
            bi=i, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]))
    
    return w, loss


def mean_squared_error_sgd(y, tx, initial_w, max_iters, gamma):
    """The Stochastic Gradient Descent algorithm (SGD) using MSE loss.
    
    Args:
        y: numpy array of shape=(N, )
        tx: numpy array of shape=(N,D)
        initial_w: numpy array of shape=(D, ). The initial guess (or the initialization) for the model parameters
        max_iters: a scalar denoting the total number of iterations of SGD
        gamma: a scalar denoting the stepsize
        
    Returns:
        w: model parameters as numpy arrays of shape (D, )
        loss: loss mse value (scalar) 
    """
    
    # Initialize weights
    w = initial_w
    
    for n_iter in range(max_iters):
        for minibatch_y, minibatch_tx in batch_iter(y, tx, batch_size=1, num_batches=1):
            
            # compute a stochastic gradient and loss
            grad = compute_gradient(minibatch_y, minibatch_tx, w, "mse")
            
            # update w through the stochastic gradient update
            w = w - gamma*grad
            
            # calculate loss
            loss = compute_loss(y, tx, w, "mse")
            
        # Display loss
        print("SGD iter. {bi}/{ti}: loss={l}, w0={w0}, w1={w1}".format(
            bi=n_iter, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]))
    
    return w, loss


def least_squares(y, tx):
    """Calculate the least squares solution.
    returns mse, and optimal weights.
    
    Args:
        y: numpy array of shape (N,), N is the number of samples.
        tx: numpy array of shape (N,D), D is the number of features.
    
    Returns:
        w: model parameters as numpy arrays of shape (D, )
        loss: loss mse value (scalar) 
    
    """
    w = np.linalg.solve(tx.T @ tx, tx.T @ y)
    loss = compute_loss(y, tx, w, "mse")
    return w, loss


def ridge_regression(y, tx, lambda_):
    """implement ridge regression.
    
    Args:
        y: numpy array of shape (N,), N is the number of samples.
        tx: numpy array of shape (N,D), D is the number of features.
        lambda_: scalar.
    
    Returns:
        w: optimal weights, numpy array of shape(D,), D is the number of features.
        loss: loss mse value (scalar) 
    """
    
    l = 2*tx.shape[0]*lambda_*np.identity(tx.shape[1])
    w = np.linalg.solve(tx.T @ tx + l, tx.T @ y)
    loss = compute_loss(y, tx, w, "mse")
    return w, loss


def logistic_regression(y, tx, initial_w, max_iters, gamma):
    """Logistic regression using SGD 
    
    Args:
        y: numpy array of shape=(N, )
        tx: numpy array of shape=(N,D)
        initial_w: numpy array of shape=(D, ). The initial guess (or the initialization) for the model parameters
        max_iters: a scalar denoting the total number of iterations of SGD
        gamma: a scalar denoting the stepsize
        
    Returns:
        w: model parameters as numpy arrays of shape (D, )
        loss: log-loss value (scalar) 
    """
    
    # Initialize weights
    w = initial_w
    
    for n_iter in range(max_iters):
        for minibatch_y, minibatch_tx in batch_iter(y, tx, batch_size=1, num_batches=1):
            
            # compute a stochastic gradient and loss
            grad = compute_gradient(minibatch_y, minibatch_tx, w, "log")
            
            # update w through the stochastic gradient update
            w = w - gamma*grad
            
            # calculate loss
            loss = compute_loss(y, tx, w, "log")
            
        # Display loss
        print("SGD iter. {bi}/{ti}: loss={l}, w0={w0}, w1={w1}".format(
            bi=n_iter, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]))
    return w, loss


def reg_logistic_regression(y, tx, lamda_, initial_w, max_iters, gamma):
    """Regularized logistic regression using SGD 
    
    Args:
        y: numpy array of shape=(N, )
        tx: numpy array of shape=(N,D)
        lambda_: scalar.
        initial_w: numpy array of shape=(D, ). The initial guess (or the initialization) for the model parameters
        max_iters: a scalar denoting the total number of iterations of SGD
        gamma: a scalar denoting the stepsize
        
    Returns:
        w: model parameters as numpy arrays of shape (D, )
        loss: log-loss value (scalar) 
    """
    
    # Initialize weights
    w = initial_w
    
    for n_iter in range(max_iters):
        for minibatch_y, minibatch_tx in batch_iter(y, tx, batch_size=1, num_batches=1):
            
            # compute a stochastic gradient and loss
            grad = compute_gradient(minibatch_y, minibatch_tx, w, "log", lambda_=lamda_)
            
            # update w through the stochastic gradient update
            w = w - gamma*grad
            
            # calculate loss
            loss = compute_loss(y, tx, w, "log")
            
        # Display loss
        print("SGD iter. {bi}/{ti}: loss={l}, w0={w0}, w1={w1}".format(
            bi=n_iter, ti=max_iters - 1, l=loss, w0=w[0], w1=w[1]))
    return w, loss


def calculate_mse(e):
    """Calculate the mse for vector e."""
    return np.mean(e ** 2) / 2


def calculate_mae(e):
    """Calculate the mae for vector e."""
    return np.mean(np.abs(e))


def calculate_logloss(y_true, y_pred):
    """Calculate the logloss """
    return -np.mean(y_true*np.log(y_pred) + (1-y_true)*np.log(1-y_pred))


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def compute_loss(y, tx, w, loss_type):
    """Calculate the loss using either MSE or MAE.
    
    Args:
        y: shape=(N, )
        tx: shape=(N,2)
        w: shape=(2,). The vector of model parameters.
        loss_type: string in ["mae", "mse", "log"] specifying the type of loss to compute
    
    Returns:
        the value of the loss (a scalar), corresponding to the input parameters w.
    """
    
    e = y - tx @ w
    
    if loss_type == "mse":
        return calculate_mse(e)
    
    elif loss_type == "mae":
        return calculate_mae(e)
    
    elif loss_type == "log":
        y_pred = sigmoid(tx @ w)
        return calculate_logloss(y, y_pred)
    
    else:
        raise ValueError("Invalid value for argument 'loss_type' when calling compute_loss, 'type' must be in ['mse', 'mae', 'log'].")


def compute_gradient(y, tx, w, loss_type, lambda_=0):
    """Computes the gradient at w.
    
    Args:
        y: numpy array of shape=(N, )
        tx: numpy array of shape=(N,D)
        w: numpy array of shape=(D, ). The vector of model parameters.
        loss_type: string in ["mse", "log"] specifying the type of loss
    
    Returns:
        An numpy array of shape (D, ) (same shape as w), containing the gradient of the loss at w.
    """
    
    if loss_type == "mse":
        e = y - tx @ w
        grad = -(tx.transpose() @ e)/y.shape[0]
    
    elif loss_type == "log":
        D = tx.shape[1]
        err = sigmoid(tx @ w) - y 
        grad = np.mean(np.broadcast_to(err, (D, err.shape[0])).T * tx, axis=0)
        grad = grad + lambda_ * w
    
    return grad


def batch_iter(y, tx, batch_size=1, num_batches=1, shuffle=True):
    """
    Generate a minibatch iterator for a dataset.
    Takes as input two iterables (here the output desired values 'y' and the input data 'tx')
    Outputs an iterator which gives mini-batches of `batch_size` matching elements from `y` and `tx`.
    Data can be randomly shuffled to avoid ordering in the original data messing with the randomness of the minibatches.
    Example of use :
    for minibatch_y, minibatch_tx in batch_iter(y, tx, 32):
        <DO-SOMETHING>
    """
    data_size = len(y)
    
    if shuffle:
        shuffle_indices = np.random.permutation(np.arange(data_size))
        shuffled_y = y[shuffle_indices]
        shuffled_tx = tx[shuffle_indices]
    else:
        shuffled_y = y
        shuffled_tx = tx
    for batch_num in range(num_batches):
        start_index = batch_num * batch_size
        end_index = min((batch_num + 1) * batch_size, data_size)
        if start_index != end_index:
            yield shuffled_y[start_index:end_index], shuffled_tx[start_index:end_index]