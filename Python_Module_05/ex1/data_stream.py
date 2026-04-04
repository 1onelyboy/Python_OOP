from abc import ABC, abstractmethod
from typing import Any, Union, Sequence


class DataProcessor(ABC):
    name: str
    _storage: list[tuple[int, str]]
    _rank: int

    @abstractmethod
    def validate(self: "DataProcessor", data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self: "DataProcessor", data: Any) -> None:
        pass

    def output(self: "DataProcessor") -> tuple[int, str]:
        rank, value = self._storage.pop(0)
        return (rank, value)


class NumericProcessor(DataProcessor):

    def __init__(self: "NumericProcessor") -> None:
        self.name = "Numeric Processor"
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

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
            self._storage.append((self._rank, str(item)))
            self._rank += 1


class TextProcessor(DataProcessor):

    def __init__(self: "TextProcessor") -> None:
        self.name = "Text Processor"
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

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
            self._storage.append((self._rank, item))
            self._rank += 1


class LogProcessor(DataProcessor):

    def __init__(self: "LogProcessor") -> None:
        self.name = "Log Processor"
        self._storage: list[tuple[int, str]] = []
        self._rank: int = 0

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
            self._storage.append((self._rank, f"{level}: {message}"))
            self._rank += 1


class DataStream:

    def __init__(self: "DataStream") -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(
        self: "DataStream",
        proc: DataProcessor
    ) -> None:
        self._processors.append(proc)

    def process_stream(
        self: "DataStream",
        stream: list[Any]
    ) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self: "DataStream") -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(
                f"{proc.name}: total {proc._rank} items processed, "
                f"remaining {len(proc._storage)} on processor"
            )
        print("")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("")

    ds = DataStream()
    print("Initialize Data Stream...")
    ds.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            },
        ],
        42,
        ['Hi', 'five'],
    ]

    print("")
    print("Registering Numeric Processor")
    print("")

    ds.register_processor(numeric)
    print(f"Send first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("Registering other data processors")
    ds.register_processor(text)
    ds.register_processor(log)
    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
