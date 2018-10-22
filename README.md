# spark
Sparkline ascii bar charts for Python

Based on https://github.com/holman/spark/blob/master/spark

Adds support for multi-row charts.
Unfortunately, doesn't support negative numbers, since [box drawing characters](https://en.wikipedia.org/wiki/Box-drawing_character) don't have top-aligned blocks.

**usage:**

`python
import spark

collatz = lambda n: if n <= 1 then [1] else [n] + collatz(3 * n + 1 if n % 2 else n / 2)
print(spark.chart(collatz(871, height=20)))