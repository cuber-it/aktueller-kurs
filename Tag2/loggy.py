import log_analyzer as la
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Path to input log file', required=True)
args = parser.parse_args()

log_reader = la.LogReader(args.input)
print(log_reader)
print(log_reader.get_events())
print(log_reader.get_event_count("INFO"))
print("\n".join(log_reader.get_event_lines("INFO")))
