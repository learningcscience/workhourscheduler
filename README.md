```mermaid
classDiagram
    class DatabaseManager {
        <<Singleton>>
        - conn
        - cur
        + get_instance()
        + execute(query, params)
        + fetchall()
    }
    class TimeEntry {
        - id
        - date
        - clock_in
        - clock_out
        - duration
        + to_dict()
    }
    class TimeLogDAO {
        + create_tables()
        + add_entry(date, clock_in)
        + update_entry(date, clock_out, duration)
        + get_entries_for_month(year, month)
    }
    class TimeLogManager {
        + clock_in()
        + clock_out()
        + get_monthly_entries()
        + total_hours(entries)
    }
    class Scheduler {
        + hours_remaining(target, worked)
        + days_remaining()
        + daily_target(hours_remain, days_remain)
    }
    class MainWindow {
        + __init__()
        + refresh_all()
    }
    class ClockInOutFrame {
        + _clock_in()
        + _clock_out()
        + refresh_status()
    }
    class EntriesFrame {
        + refresh()
    }
    class SummaryFrame {
        + refresh()
    }

    TimeLogDAO --> DatabaseManager : uses
    TimeLogManager --> TimeLogDAO : uses
    MainWindow --> TimeLogManager : uses
    MainWindow --> Scheduler : uses
    ClockInOutFrame --> MainWindow : calls
    EntriesFrame --> MainWindow : calls
    SummaryFrame --> MainWindow : calls
