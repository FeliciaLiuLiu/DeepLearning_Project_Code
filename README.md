# Deep Learning for Healthcare Final Project


## Citation to the original paper
This project aims at reproducing the paper 'Readmission prediction via deep contextual embedding of clinical concepts' and check if the reproducer can get similar results presented in the original paper:
https://pubmed.ncbi.nlm.nih.gov/29630604/


## Data Download Instruction:
The dataset in this repository can be downloaded directly from the paper:
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0195024

In the session 'Supporting information', we can download the 'S1_File.txt'

## Link to the original paper's repo:
The code in the repository is heavily based on the code provided by the author:
https://github.com/danicaxiao/CONTENT


## Guidance to run the code

The below instructions illustrate the methods to preprocess, train, test and evaluate the code in the command:

1. Clone the repository in the PyCharm as a whole project.
2. Open the terminal and access to the location of this repository folder. For instance, firstly enter 'cd "DeepLearning_Project_Code"', then enter 'cd "CONTENT code"' in the terminal. All the codes are saved in the folder "CONTENT code".
3. In the terminal, when we are in the path of "CONTENT code", run function 'make new' in the terminal (This step is preprocessing).
4. Run function 'make train' in the terminal, since the epoch is defaulted as 5, it will run 5 times (This step is training).
5. Run function 'make test' in the terminal, and observe the results (This step is testing).
6. Run function 'make eval' in the terminal, and record the values for 'PR-AUC', 'ROC-AUC', 'ACC' (This step is evaluating).


## Table of Results

Experiment results for the 10 times reruns:

![img_6.png](img_6.png)



- Average PR-AUC Achieved: 0.5906 ± 0.0117
- Average ROC-AUC Achieved: 0.7791 ± 0.0084
- Average Accuracy Achieved: 0.8244 ± 0.0062


Experiment results for changing hyperparameter 'Learning Rate' and running for 3 times:

![img_7.png](img_7.png)


- Average PR-AUC Achieved: 0.6447 ± 0.0019
- Average ROC-AUC Achieved: 0.7976 ± 0.0007
- Average Accuracy Achieved: 0.8410 ± 0.0011


Experiment results for changing hyperparameter 'Epoch Size' and running for 3 times:

![img_5.png](img_5.png)

- Average PR-AUC Achieved: 0.5942 ± 0.0048
- Average ROC-AUC Achieved: 0.7813 ± 0.0033
- Average Accuracy Achieved: 0.8251 ± 0.0008


Experiment results for changing hyperparameter 'Hidden Size' and running for 3 times:

![img_4.png](img_4.png)

- Average PR-AUC Achieved: 0.5127 ± 0.0117
- Average ROC-AUC Achieved: 0.7311 ± 0.0068
- Average Accuracy Achieved: 0.7918 ± 0.0053


## Dependencies

The dependencies required for this project can be found from the file 'dependencyConfirmation.txt':

| Package             |  Version   | 
| ------------------- | ---------- | 
| cycler              | 0.11.0     | 
| fonttools           | 4.32.0     | 
| joblib              | 1.1.0      | 
| kiwisolver          | 1.4.2      | 
| Lasagne             | 0.2.dev1   | 
| matplotlib          | 3.5.1      | 
| numpy               | 1.20.3     | 
| packaging           | 21.3       | 
| pandas              | 1.4.2      | 
| Pillow              | 9.1.0      | 
| pip                 | 20.0.2     | 
| pkg-resources       | 0.0.0      | 
| psutil              | 5.9.0      | 
| pyparsing           | 3.0.8      | 
| python-dateutil     | 2.8.2      | 
| pytz                | 2022.1     | 
| scikit-learn        | 1.0.2      | 
| scipy               | 1.8.0      | 
| setuptools          | 44.0.0     | 
| six                 | 1.16.0     | 
| sklearn             | 0.0        | 
| Theano              | 1.0.5+unknown | 
| threadpoolctl       | 3.1.0      | 
| urllib3             | 1.26.9     | 
| zipfile36           | 0.1.3      | 
