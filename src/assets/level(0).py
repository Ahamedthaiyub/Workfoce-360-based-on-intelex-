# -*- coding: utf-8 -*-
"""level(0).ipynb



Original file is located at
    https://colab.research.google.com/drive/1-ulbadChba9YQuQ1AU7Qtpr4qSAgugao
Author: Ahamed Thaiyub A 
# description about the project:
### work of HR  at the '0'th level

# PROJECT 1 DECRYPTORS

from google.colab import drive
drive.mount('/content/drive')
"""









import pandas as pd
import io
 
df = pd.read_csv(io.BytesIO(up['employee_data.csv']))
print(df)

df

df.head()

df.tail()

df.value_counts()

df['EmployeeID'].value_counts

df['Sex'].value_counts()

df['Designation'].value_counts()

df.isnull().sum().sum()

df.corr()

from google.colab import files
up1 = files.upload()

from google.colab import files
up2 = files.upload()

pip install chart-studio

from sklearn.impute import SimpleImputer
import numpy as np

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

from sklearnex import patch_sklearn
patch_sklearn()



pip install scikit-learn-intelex

from sklearnex import patch_sklearn
patch_sklearn()

import nltk
nltk.download()
nltk.download('stopwords')

from nltk.corpus import stopwo

rds

set(stopwords.words("english"))

import string
import csv
import re
import sys
import importlib
import os
import spacy
from pyresparser import ResumeParser
import pandas as pd
import nltk
from spacy.matcher import matcher
import multiprocessing as mp

def main():
    data = ResumeParser("D:\ALL PDF\Profile.pdf").get_extracted_data()
    print(data)

    # Added encoding utf-8 to prevent unicode error
    with open("C:/Users/infinitel88p/Downloads/resume.txt", "w", encoding='utf-8') as rf:
        rf.truncate()
        rf.write(str(data))

    print("Resume results are getting printed into resume.txt.")

    # Extracting skills
    resume_list = []
    skill_list = []

    data = pd.read_csv("skills.csv")
    skills = list(data.columns.values)

    resume_file = os.path.dirname(__file__) + "/resume.txt"
    with open(resume_file, 'r',  encoding='utf-8') as f: 
        for line in f: 
            resume_list.append(line.strip())
            for token  in resume_list:
                if token.lower() in skills:
                    skill_list.append(token)
    print(skill_list)

if __name__ == "__main__":
    main()

pip install nltk

import nltk
nltk.download('stopwords')

import nltk
nltk.download()

nltk.set_proxy('http://proxy.example.com:3128', ('USERNAME', 'PASSWORD'))
nltk.download()

import string
import csv
import re
import sys
import importlib
import os
import spacy
from pyresparser import ResumeParser
import pandas as pd
import nltk
from spacy.matcher import matcher
import multiprocessing as mp

def main():
    data = ResumeParser("/content/resume.pdf").get_extracted_data()
    print(data)

    # Added encoding utf-8 to prevent unicode error
    with open("/content/Profile.pdf", "w", encoding='utf-8') as rf:
        rf.truncate()
        rf.write(str(data))

    print("Resume results are getting printed into resume.txt.")

    # Extracting skills
    resume_list = []
    skill_list = []

    data = pd.read_csv("/content/skills.csv")
    skills = list(data.columns.values)

    resume_file ="/content/resume2.txt"
    with open(resume_file, 'r',  encoding='utf-8') as f: 
        for line in f:
            resume_list.append(line.strip())
            for token  in resume_list:
                if token.lower() in skills:
                    skill_list.append(token)
    print(skill_list)

if __name__ == "__main__":
    main()

"""# New Section"""

print(dir)

import spacy
nlp = spacy.load("en_core_web_sm")

# pip install nltk
# pip install spacy==2.3.5
# pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
# pip install pyresparser

pip install spacy==2.3.5

pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz

pip install wheel

