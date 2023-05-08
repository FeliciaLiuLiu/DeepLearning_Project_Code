'''
CS 598 Deep Learning for Healthcare, Spring 2023
Group ID: 143
Paper ID: 168

The code is either re-used or heavily based off the code from
https://github.com/danicaxiao/CONTENT.
'''

import sys
import os
import psutil
import time
import DataPrep as dp
from Configuration import Configuration
from PatientDataLoader import PatientDataLoader
import CONTENT as content
import CONTENT_FixedBatch as contentFixed


if __name__ == '__main__':
    fixed = "fixed" in sys.argv
    new = "new" in sys.argv
    train = "train" in sys.argv
    continue_training = "continued" in sys.argv
    test = "test" in sys.argv
    isEval = "eval" in sys.argv

    # Initial Directory Initializations:
    if not os.path.exists("CONTENT_results"):
        os.mkdir("CONTENT_results")

    if not os.path.exists("theta_with_rnnvec"):
        os.mkdir("theta_with_rnnvec")

    # This function is used to split new input files
    if new or not os.path.exists("data/X_train.pkl"):
        print("Setting Up and Preprocessing Data.")
        start = time.time()
        data = dp.retrieve_data(False) # Retrieves input data if it doesn't already exist
        dp.data_to_csv(data) # Writes vocab and stop files based on Input
        word2ind = dp.load_data_from_file() # Loads vocab from csv files into word2ind vector
        events = dp.extract_events() # Extracts events from input file
        data, labels = dp.convert_format(word2ind, events) # Converts data into more useful format
        dp.splits(data, labels) # Creates training, validation, and testing splits and writes them to pickled files
        end = time.time()

    # Leveraged the code from the original author: https://github.com/danicaxiao/CONTENT/blob/master/CONTENT.py
    FLAGS = Configuration()
    data_set = PatientDataLoader(FLAGS)
    iterator = data_set.iterator()

    if fixed:
        thetaPath = "theta/thetas1.npy"
        start = time.time()
        contentFixed.run(data_set, train=train, continued=continue_training)
        end = time.time()
        contentFixed.clustering(thetaPath, data_set)
        contentFixed.eval(1)
    elif train or test:
        thetaPath = "theta_with_rnnvec/thetas_train0.npy"
        start = time.time()
        content.run(data_set, isTrain=train, continued=continue_training)
        end = time.time()

    if (isEval):
        content.eval(2)
        content.clustering(thetaPath, data_set)

    print("Total GPU Time to Run Experiment: {}".format(end - start))
    process = psutil.Process(os.getpid())
    print("Total Memory Usage in Process: {} MB".format(process.memory_info().rss / 1024)) 
