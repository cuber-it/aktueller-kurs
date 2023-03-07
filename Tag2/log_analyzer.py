class LogReader:
    def __init__(self, file_path):
        """
        Initializes a LogReader object with the specified log file path.

        Args:
            file_path (str): The path to the log file to be read.
        """
        self.file_path = file_path
        self.log_data = None

        with open(self.file_path, 'r') as file:
            self.log_data = file.read().splitlines()

    def get_event_count(self, event):
        """
        Counts the number of occurrences of a specified log level event in the log data.

        Args:
            event (str): The log level event to count occurrences of.

        Returns:
            int: The number of occurrences of the specified log level event in the log data.
        """
        count = 0
        for line in self.log_data:
            if event in line:
                count += 1
        return count

    def get_event_lines(self, event):
        """
        Extracts all lines from the log data that contain a specified log level event.

        Args:
            event (str): The log level event to extract from the log data.

        Returns:
            list: A list of all lines that contain the specified log level event in the log data.
        """
        result = []
        for line in self.log_data:
            if event in line:
                result.append(line)
        return result

    def get_events(self):
        """
        Extracts a list of all unique log level events found in the log data.

        Returns:
            list: A list of all unique log level events found in the log data.
        """
        events = set()
        for line in self.log_data:
            event = line[14:22].strip()
            events.add(event)
        return list(events)

    def __str__(self):
        result = "<empty>"
        if len(self.log_data) != 0:
            result = "\n".join(self.log_data[:5])
        return result

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to input log file', required=True)
    args = parser.parse_args()

    log_reader = LogReader(args.input)
    print(log_reader)
    print(log_reader.get_events())
    print(log_reader.get_event_count("INFO"))
    print("\n".join(log_reader.get_event_lines("INFO")))
