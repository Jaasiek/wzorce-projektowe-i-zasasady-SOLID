from main import (
    ExecutionTimesBaseStatistics,
    WithMeanStatisticsLogger,
    WithSummaryStatisticsLogger,
    ExecutionTimesWithFunctionDecorators,
)


def test_base_statistics():
    data = [1.0, 2.0, 3.0]
    stats = ExecutionTimesBaseStatistics(data)
    assert stats.get_execution_times() == data


def test_object_decorators():
    data = [1.0, 2.0, 3.0]
    base = ExecutionTimesBaseStatistics(data)
    decorated = WithMeanStatisticsLogger(WithSummaryStatisticsLogger(base))
    assert decorated.get_execution_times() == data


def test_function_decorators():
    data = [2.0, 4.0]
    stats = ExecutionTimesWithFunctionDecorators(data)
    assert stats.get_execution_times() == data
