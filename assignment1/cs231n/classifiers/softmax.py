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
  
  for i_ex, ex in enumerate(X):
    scores = ex.dot(W) 
    scores = np.exp(scores)/float(np.sum(np.exp(scores)))
    correct_score = scores[y[i_ex]]
    loss -= np.log(correct_score)
    for k in xrange(dW.shape[1]):
      if y[i_ex] == k:
         dW[:,k] -= ex*(1-correct_score)
      else:
         dW[:,k] += ex*correct_score
  loss /= X.shape[0]
  dW /= X.shape[0]
  dW += reg*W
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
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
  scores = X.dot(W)
  scores = np.exp(scores)/np.reshape(np.sum(np.exp(scores), axis = 1), (X.shape[0], 1))
  correct_scores = scores[xrange(X.shape[0]),y]
  loss = np.mean(-np.log(correct_scores))

  mask = np.repeat(np.reshape(correct_scores, (-1,1)), W.shape[1], axis = 1)
  mask[xrange(mask.shape[0]), y] = correct_scores - 1
  dW = X.T.dot(mask)/X.shape[0] + reg*W
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  pass
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

