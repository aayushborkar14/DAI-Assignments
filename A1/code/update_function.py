def newMean(OldMean: float, NewDataValue: float, n: int, A: list[float]) -> float:
    oldSum = OldMean * n
    newSum = oldSum + NewDataValue
    return newSum / (n + 1)


def newMedian(OldMedian: float, NewDataValue: float, n: int, A: list[float]) -> float:
    # Assuming sorted list A
    if n % 2 == 0:
        if A[n // 2 - 1] <= NewDataValue <= A[n // 2]:
            return NewDataValue
        elif NewDataValue < A[n // 2 - 1]:
            return A[n // 2 - 1]
        else:
            return A[n // 2]
    else:
        if NewDataValue <= A[n // 2 - 1]:
            return (A[n // 2 - 1] + A[n // 2]) / 2
        elif NewDataValue >= A[n // 2 + 1]:
            return (A[n // 2] + A[n // 2 + 1]) / 2
        else:
            return (A[n // 2] + NewDataValue) / 2


def newStd(
    OldMean: float,
    OldStd: float,
    NewMean: float,
    NewDataValue: float,
    n: int,
    A: list[float],
) -> float:
    oldSquareSum = ((OldStd**2) * (n - 1)) + (n * (OldMean**2))
    newSquareSum = oldSquareSum + (NewDataValue**2)
    return ((newSquareSum - ((n + 1) * (NewMean) ** 2)) / n) ** 0.5

