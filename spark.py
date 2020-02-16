
import sys

def chart(numbers, height=10):
    bars = list("▁▂▃▄▅▆▇█")

    maxVal     = max(numbers)
    normalized = [max(0, n * height / maxVal) for n in numbers]
    result     = ""

    for row in range(height):
        rowString = ""
        for n in normalized:
            barHeight = n - row
            if barHeight <= 0:
                rowString += " " if row else "_"
            else:
                rowString += bars[min(7, round(barHeight * 7))]
        result = rowString + "\n" + result
    return result

if __name__ == "__main__":
    numbers = [float(n) for n in sys.argv[1:]]
    if numbers:
        print(chart(numbers))