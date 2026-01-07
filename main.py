from abc import ABC, abstractmethod

# from typing import List


class StatisticsLogger(ABC):

    @abstractmethod
    def display_statistics(self) -> None:
        pass

    @abstractmethod
    def get_execution_times(self) -> list[float]:
        pass


class ExecutionTimesBaseStatistics(StatisticsLogger):

    def __init__(self, execution_times: list[float]) -> None:
        self._execution_times = execution_times

    def display_statistics(self) -> None:
        for t in self._execution_times:
            print(t)

    def get_execution_times(self) -> list[float]:
        return self._execution_times


class WithMeanStatisticsLogger(StatisticsLogger):

    def __init__(self, logger: StatisticsLogger) -> None:
        self._logger = logger

    def display_statistics(self) -> None:
        times = self._logger.get_execution_times()
        mean = sum(times) / len(times) if times else 0
        print(f"Średnia: {mean}")
        self._logger.display_statistics()

    def get_execution_times(self) -> list[float]:
        return self._logger.get_execution_times()


class WithSummaryStatisticsLogger(StatisticsLogger):

    def __init__(self, logger: StatisticsLogger) -> None:
        self._logger = logger

    def display_statistics(self) -> None:
        times = self._logger.get_execution_times()

        if times:
            print(f"Liczba rekordów: {len(times)}")
            print(f"Suma: {sum(times)}")
            print(f"Min: {min(times)}")
            print(f"Max: {max(times)}")

        self._logger.display_statistics()

    def get_execution_times(self) -> list[float]:
        return self._logger.get_execution_times()


def with_mean(func):
    def wrapper(self) -> None:
        times = self.get_execution_times()
        mean = sum(times) / len(times) if times else 0
        print(f"Średnia: {mean}")
        func(self)

    return wrapper


def with_summary(func):
    def wrapper(self) -> None:
        times = self.get_execution_times()
        if times:
            print(f"Liczba rekordów: {len(times)}")
            print(f"Suma: {sum(times)}")
            print(f"Min: {min(times)}")
            print(f"Max: {max(times)}")
        func(self)

    return wrapper


class ExecutionTimesWithFunctionDecorators(ExecutionTimesBaseStatistics):

    @with_summary
    @with_mean
    def display_statistics(self) -> None:
        super().display_statistics()


times = [1.2, 0.9, 1.5, 1.1]

logger = ExecutionTimesWithFunctionDecorators(times)
logger.display_statistics()
