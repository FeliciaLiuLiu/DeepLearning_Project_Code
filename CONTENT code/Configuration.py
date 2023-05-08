'''
CS 598 Deep Learning for Healthcare, Spring 2023
Group ID: 143
Paper ID: 168

The code is either re-used or heavily based off the code from
https://github.com/danicaxiao/CONTENT.
'''

#!/usr/bin/env python
# coding: utf-8

class Configuration:
    # feel free to play with these hyperparameters during training
    dataset = "data" # change this to the right data name
    data_path = "./%s" % dataset
    # checkpoint_dir = "checkpoint"
    # decay_rate = 0.95
    # decay_step = 1000
    n_topics = 50
    learning_rate = 0.00002
    vocab_size = 619
    n_stops = 22 
    lda_vocab_size = vocab_size - n_stops
    n_hidden = 200
    # n_layers = 2
    projector_embed_dim = 100
    # generator_embed_dim = n_hidden
    # dropout = 1.0
    # max_grad_norm = 1.0 #for gradient clipping
    grad_clip = 100
    total_epoch = 5
    epoch_size = 100
    batch_size = 1
    # init_scale = 0.075
    threshold = 0.5 #probability cut-off for predicting label to be 1
    # forward_only = False #indicates whether we are in testing or training mode
    # log_dir = './logs'

