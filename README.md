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

