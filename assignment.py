class FlightTable:
    def __init__(self, data):
        self.data = data

    def sort_by_p_id(self):
        self.data.sort(key=lambda x: x["P_ID"])

    def sort_by_start_time(self):
        self.data.sort(key=lambda x: x["Start Time (ms)"])

    def sort_by_priority(self):
        priority_order = {"Low": 1, "MID": 2, "High": 3}
        self.data.sort(key=lambda x: priority_order[x["Priority"]])

    def print_table(self):
        print("{:<5} {:<10} {:<18} {}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
        print("=" * 50)
        for row in self.data:
            print("{:<5} {:<10} {:<18} {}".format(row["P_ID"], row["Process"], row["Start Time (ms)"], row["Priority"]))

if __name__ == "__main__":
    data = [
        {"P_ID": "P1", "Process": "VSCode", "Start Time (ms)": 100, "Priority": "MID"},
        {"P_ID": "P23", "Process": "Eclipse", "Start Time (ms)": 234, "Priority": "MID"},
        {"P_ID": "P93", "Process": "Chrome", "Start Time (ms)": 189, "Priority": "High"},
        {"P_ID": "P42", "Process": "JDK", "Start Time (ms)": 9, "Priority": "High"},
        {"P_ID": "P9", "Process": "CMD", "Start Time (ms)": 7, "Priority": "High"},
        {"P_ID": "P87", "Process": "NotePad", "Start Time (ms)": 23, "Priority": "Low"}
    ]

    flight_table = FlightTable(data)

    while True:
        print("\nSelect sorting parameter:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            flight_table.sort_by_p_id()
        elif choice == 2:
            flight_table.sort_by_start_time()
        elif choice == 3:
            flight_table.sort_by_priority()
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

        flight_table.print_table()
