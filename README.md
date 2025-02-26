# Learning a bit about Spark -> PySpark

#### Create virtual env to play 
```
$ python3 -m venv .pyspark-venv
```

### Activate virtual env 
```
$ source .pyspark-env/bin/activate
$ pip install --upgrade pip
```

### Install some packages 
```
$ pip install pyspark findspark jupyterlab
```

### Download Spark binary file
Go to [Spark Official Download Site](https://spark.apache.org/downloads.html) and download the last stable version.

```
$ tar xfz spark-<version>-bin-hadoop3.tgz
$ mkdir -p /usr/local/bin/spark
$ mv spark-<version>-bin-hadoop3 /usr/local/bin/spark
$ cd ~/.
$ vim .zshrc
$ export PATH="/usr/local/bin/spark-3.5.1-bin-hadoop3/bin:$PATH"
$ source .zshrc
```

### Run Jupyter

```
$ jupyter-lab
```

Note: All those steps were executed on Mac OS 


### Interactive Python NoteBook files

PySpark-Get-Started.ipynb - *First interactive Python Notebook* 

Alura-PySpark-I-Course-Intro.ipynb - *Create first session and says to computer to use all cpus available* 

Alura-PySpark-II-Course-Loading-Data.ipynb - *Create the first data frame of the course*

Alura-PySpark-III-DataFrame-Creation.ipynb - *Contains the necessary code to create three valid data frames and one invalid data frame*

Alura-PySpark-IV-Data-From-ReceitaFederal.ipynb - *Unzip file and load data from csv file*

Alura-PySpark-V-Data-Handler.ipynb - *Rename columns of the data frame*

Alura-PySpark-VI-Casting.ipynb - *Apply casting to DoubleType, StringType and DateType*

Alura-PySpark-VII-Select.ipynb - *Select columns from dataframe*

Alura-PySpark-VIII-IsNull-IsNaN.ipynb - *Handle null and not a number values*

Alura-PySpark-IX-OrderBy.ipynb - *Sorting dataframes by columns*

