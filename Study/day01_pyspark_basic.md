# Day1 - PySpark 기본 정리

## 1. Spark란?

Spark는 **대용량 데이터를 빠르게 처리하기 위한 분산 데이터 처리 엔진**이다.

기존 Python이나 Pandas는 한 컴퓨터에서 데이터를 처리하지만
Spark는 여러 노드에서 데이터를 **병렬로 처리**할 수 있다.

### Spark 구조

Driver → Executor → Worker

* **Driver**

  * 프로그램 실행
  * 작업 분배

* **Executor**

  * 실제 데이터 처리

즉

Driver가 작업을 나누고 Executor들이 병렬로 계산한다.

---

# 2. PySpark

Spark는 원래 **Scala 기반**이다.

하지만 Python에서도 사용할 수 있도록 만든 것이 **PySpark**이다.

구조

Python 코드
↓
PySpark API
↓
Spark Engine 실행

그래서 Python 코드처럼 보이지만 실제 계산은 Spark가 수행한다.

---

# 3. SparkSession

Spark 프로그램을 시작할 때 사용하는 객체이다.

```python
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
os.environ["SPARK_LOCAL_IP"] = "127.0.0.1"

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("PySparkDay1") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()
```

SparkSession은 **Spark 작업을 시작하는 진입점(entry point)** 이다.

---

# 4. DataFrame

Spark에서 데이터를 다루는 가장 중요한 구조는 **DataFrame**이다.

Pandas DataFrame과 비슷하지만 **분산 데이터 처리**가 가능하다.

### DataFrame 생성

```python
data = [
    ("2024-01-01", 72000, 100000),
    ("2024-01-02", 73000, 120000),
    ("2024-01-03", 71000, 90000),
]

columns = ["date", "close", "volume"]

df = spark.createDataFrame(data, columns)

df.show()
```

출력 예시

```
+----------+-----+------+
|date      |close|volume|
+----------+-----+------+
|2024-01-01|72000|100000|
|2024-01-02|73000|120000|
|2024-01-03|71000|90000 |
+----------+-----+------+
```

---

# 5. select

특정 컬럼을 선택할 때 사용한다.

```python
df.select("date","close").show()
```

결과

```
+----------+-----+
|date      |close|
+----------+-----+
|2024-01-01|72000|
|2024-01-02|73000|
|2024-01-03|71000|
```

---

# 6. filter

조건을 이용하여 데이터를 필터링할 수 있다.

```python
df.filter(df.close > 72000).show()
```

결과

```
+----------+-----+------+
|date      |close|volume|
+----------+-----+------+
|2024-01-02|73000|120000|
```

---

# 7. withColumn

새로운 컬럼을 추가할 때 사용한다.

```python
from pyspark.sql.functions import col

df2 = df.withColumn("value", col("close") * col("volume"))
df2.show()
```

결과

```
+----------+-----+------+-----------+
|date      |close|volume|value      |
+----------+-----+------+-----------+
|2024-01-01|72000|100000|7200000000 |
|2024-01-02|73000|120000|8760000000 |
```

---

# 8. Spark 특징 (Lazy Evaluation)

Spark는 **Lazy Evaluation** 방식을 사용한다.

즉 연산을 바로 실행하지 않는다.

예

```
select
filter
withColumn
```

이 연산들은 바로 실행되지 않는다.

하지만 다음과 같은 **Action**이 실행되면 실제 계산이 수행된다.

```
show()
collect()
count()
```

---

# 9. 오늘 배운 것

* Spark 구조
* PySpark 개념
* SparkSession
* DataFrame
* select
* filter
* withColumn

---

# 다음 학습

Day2에서는 다음 내용을 학습할 예정이다.

* groupBy
* aggregation
* orderBy
* Window function
* 주가 데이터 분석
