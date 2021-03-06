import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  
  num_train = float(X.shape[0])

  for i in range(int(num_train)):

    score = X[i].dot(W)
    score -= np.max(score)
    loss += - np.log(np.exp(score[y[i]]) / np.sum(np.exp(score)))

    for  j in range(W.shape[1]):
      if j == y[i]:
        dW[:, j] += (np.exp(score[j]) / np.sum(np.exp(score)) - 1) * X[i]
      else:
        dW[:, j] += np.exp(score[j]) / np.sum(np.exp(score)) * X[i]

  loss /= num_train
  loss += reg * np.sum(W * W)

  dW /= num_train
  dW += 2*reg*W 
  
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = float(X.shape[0])

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  
  score = X.dot(W)
  score = np.exp(score - np.max(score, axis = 1).reshape(-1,1))
  loss = np.sum(- np.log(score[np.arange(len(score)), y] / np.sum(score, axis = 1)))
  loss /= num_train
  loss += reg * np.sum(W * W)

  m_s = score/score.sum(axis=1, keepdims=True)
  m_s[np.arange(len(score)), y] -= 1
  dW = X.T.dot(m_s)
  dW /= num_train
  dW += 2*reg*W 

  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

