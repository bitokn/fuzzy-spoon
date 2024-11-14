import csv
from datetime import datetime


def get_solve_times(csTimer_file_path):
    solve_times = {}
    with open(csTimer_file_path, newline="") as csTimer_export:
        train_solves = csv.reader(csTimer_export, delimiter=";")
        for row in train_solves:
            if row[4] != "Date":
                # 2024-06-03 20:17:48
                solve_time = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
                solve_times[solve_time] = row[1]
    return solve_times


def get_startend_times(arcCard_file_path):
    start_times = []
    end_times = []
    with open(arcCard_file_path, newline="") as arcCard_export:
        train_rides = csv.reader(arcCard_export, delimiter=",")
        for ride in train_rides:
            if ride[6] == "ETS LRT":
                grandate = f"{ride[0]} {ride[1]}"
                time = datetime.strptime(grandate, "%b-%d-%Y %I:%M %p")
                if ride[3] == "Pass Use On Entry":
                    start_times.insert(0, time)
                elif ride[3] == "Pass Use On Exit":
                    end_times.insert(0, time)
    return start_times, end_times


def create_ride_solves_list(solve_times, start_time, end_time):
    solvesinride = []
    for solve in solve_times:
        if solve > start_time and solve < end_time:
            solvesinride.append(solve_times[solve])
    return solvesinride


def createdict(solve_times, start_times, end_times):
    ride_dict = {}
    for i in range(len(start_times)):
        key = (start_times[i], end_times[i])
        start_time = start_times[i]
        end_time = end_times[i]
        value = create_ride_solves_list(solve_times, start_time, end_time)
        ride_dict[key] = value
    return ride_dict


def main() -> None:
    csTimer_data = "../csTimerExport_20241114_093729.csv"
    solve_times = get_solve_times(csTimer_data)
    arc_data = "../transaction_export638671991223629994.csv"
    start_times, end_times = get_startend_times(arc_data)
    d = createdict(solve_times, start_times, end_times)
    for i in d:
        print(f"entered: {i[0]}, exited: {i[1]}.:")
        print(f"Solves: {d[i]}")


main()
