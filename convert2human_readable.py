import random
# trace_parser.py
def parse_trace_line(line, output_file):
    parts = line.strip().split()
    if len(parts) == 5:
        # 假設格式：Key (十六進位), Operation, Value Size, 其他欄位, Timestamp
        key = int(parts[0], 16)
        operation = "GET" if parts[1] == "0" else "UNKNOWN"
        value_size = int(parts[2])
        timestamp = int(parts[4])
        print(f"Operation: {operation}\nKey: {key}\nValue Size: {value_size}\nTimestamp: {timestamp}\n")

        value = random.getrandbits(64)
        
        # 將結果寫入檔案
        output_file.write(f"{operation} {key} {value}\n")


if __name__ == "__main__":
    with open("test-human_readable_trace.txt", "r") as file, open("workload.txt", "w") as output_file:
        for line in file:
            parse_trace_line(line, output_file)
