from abc import ABC, abstractmethod
from typing import Any, Union, Sequence


class DataProcessor(ABC):
    storage: list[tuple[int, str]]

    @abstractmethod
    def validate(self: "DataProcessor", data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self: "DataProcessor", data: Any) -> None:
        pass

    def output(self: "DataProcessor") -> tuple[int, str]:
        rank, value = self.storage.pop(0)
        return (rank, value)


class NumericProcessor(DataProcessor):

    def __init__(self: "NumericProcessor") -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank: int = 0

    def validate(self: "NumericProcessor", data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, (int, float)) for item in data)

        return False

    def ingest(self: "NumericProcessor", data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")

        items: list[Union[int, float]] = (
            list(data)
            if isinstance(data, Sequence) and not isinstance(data, str)
            else [data]
        )

        for item in items:
            self.storage.append((self.rank, str(item)))
            self.rank += 1


class TextProcessor(DataProcessor):

    def __init__(self: "TextProcessor") -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank: int = 0

    def validate(self: "TextProcessor", data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self: "TextProcessor", data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")

        items: list[str] = (
            list(data)
            if isinstance(data, Sequence) and not isinstance(data, str)
            else [data]
        )

        for item in items:
            self.storage.append((self.rank, item))
            self.rank += 1


class LogProcessor(DataProcessor):

    def __init__(self: "LogProcessor") -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank: int = 0

    def validate(self: "LogProcessor", data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )

        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(item, dict) and
                all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )

        return False

    def ingest(self: "LogProcessor", data: Any) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")

        items: list[dict[str, str]] = (
            list(data)
            if isinstance(data, Sequence) and not isinstance(data, str)
            else [data]
        )

        for item in items:
            level = item.get("log_level", "")
            message = item.get("log_message", "")
            self.storage.append((self.rank, f"{level}: {message}"))
            self.rank += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest('foo')
    except TypeError as e:
        print(f"Got exception: {e}")

    data_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_num}")
    numeric.ingest(data_num)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    print("")
    print("Testing Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")

    data_text = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {data_text}")
    text.ingest(data_text)
    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    print("")
    print("Testing Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")

    data_log = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {data_log}")
    log.ingest(data_log)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
