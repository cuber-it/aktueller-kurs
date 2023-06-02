import argparse
import csv

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Counts the number of events in a log file.")
parser.add_argument("-i", "--input", help="Path to the input log file", required=True)
parser.add_argument("-o", "--output", help="Path to the output CSV file", required=True)
args = parser.parse_args()

# Define the start and end columns of the event type in each log message
event_type_start = 14
event_type_end = 22

# Initialize the event count dictionary
event_counts = {}

# Open the input log file and read each line
with open(args.input, "r") as file:
    lines = file.readlines()

    # Loop through each line, extracting the event from the log message
    for line in lines:
        event = line[event_type_start:event_type_end].strip()
        if event in event_counts:
            event_counts[event] += 1
        else:
            event_counts[event] = 1

# Output the event counts in a tabular format
print("Event\tCount")
for event, count in event_counts.items():
    print(f"{event}\t{count}")

# Write the event counts to the output CSV file
with open(args.output, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Event", "Count"])
    for event, count in event_counts.items():
        writer.writerow([event, count])
