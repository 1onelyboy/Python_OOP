from abc import ABC, abstractmethod
from typing import Any, Union, Protocol, Sequence


class DataProcessor(ABC):
    name: str
    storage: list[tuple[int, str]]
    rank: int

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
        self.name = "Numeric Processor"
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
        self.name = "Text Processor"
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
        self.name = "Log Processor"
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


class ExportPlugin(Protocol):

    def process_output(
        self: "ExportPlugin",
        data: list[tuple[int, str]]
    ) -> None:
        ...


class CSVExportPlugin:

    def process_output(
        self: "CSVExportPlugin",
        data: list[tuple[int, str]]
    ) -> None:
        values = [value for (rank, value) in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:

    def process_output(
        self: "JSONExportPlugin",
        data: list[tuple[int, str]]
    ) -> None:
        pairs = [f'"item_{rank}": "{value}"' for (rank, value) in data]
        print("JSON Output:")
        print("{" + ", ".join(pairs) + "}")


class DataStream:

    def __init__(self: "DataStream") -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(
        self: "DataStream",
        proc: DataProcessor
    ) -> None:
        self.processors.append(proc)

    def process_stream(
        self: "DataStream",
        stream: list[Any]
    ) -> None:
        for element in stream:
            handled = False
            for proc in self.processors:
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
        if not self.processors:
            print("No processor found, no data")
            print("")
            return
        for proc in self.processors:
            print(
                f"{proc.name}: total {proc.rank} items processed, "
                f"remaining {len(proc.storage)} on processor"
            )
        print("")

    def output_pipeline(
        self: "DataStream",
        nb: int,
        plugin: ExportPlugin
    ) -> None:
        for proc in self.processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                if not proc.storage:
                    break
                collected.append(proc.output())
            plugin.process_output(collected)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("")

    ds = DataStream()
    print("Initialize Data Stream...")
    print("")
    ds.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Registering Processors")
    print("")
    ds.register_processor(numeric)
    ds.register_processor(text)
    ds.register_processor(log)
    print("")

    batch1 = [
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

    print(f"Send first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    print("")
    ds.print_processors_stats()
    print("")

    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExportPlugin())
    print("")
    ds.print_processors_stats()

    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            },
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ]

    print(f"Send another batch of data: {batch2}")
    ds.process_stream(batch2)
    print("")
    ds.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExportPlugin())
    print("")
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
