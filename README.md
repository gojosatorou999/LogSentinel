# LogSentinel: Python Log Monitor Tool

**LogSentinel** is a lightweight, real-time log monitoring utility written in Python. It allows users to track log files for specific keywords, providing instant visual feedback when critical events (like "ERROR", "CRITICAL", or specific "USER_ID") are detected.

#### Features

- **Real-time Monitoring**: Mimics the behavior of `tail -f` to watch file updates instantly.
- **Keyword Spotting**: Monitors multiple keywords simultaneously.
- **Visual Highlighting**: Uses terminal colors to highlight detected keywords for quick identification.
- **Timestamping**: Adds a clear timestamp to each detected log line.
- **Efficient**: Uses minimal CPU by leveraging file pointer tracking and periodic polling.

## How it Works (Detection Logic)

LogSentinel employs a "tailing" algorithm to monitor changes in a file without re-reading the entire file every time:

1.  **File Pointer Tracking**: Upon starting, the script moves the file pointer to the very end of the file (`seek(0, os.SEEK_END)`). This ensures we only monitor *new* entries.
2.  **Continuous Polling**: In a loop, the script attempts to read a new line. 
    - If a line exists, it is processed.
    - If no line is found, it waits for a predefined interval (default 1s) before trying again.
3.  **Keyword Matching**: Each new line is compared against the user-provided keyword list. The search is case-insensitive for maximum flexibility.
4.  **Highlighting Engine**: When a match is found, the script uses ANSI escape codes (via `colorama`) to wrap the keyword in bright red formatting before printing it to the terminal.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/gojosatorou999/LogSentinel.git
    cd LogSentinel
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script by providing the log file path and the keywords you want to monitor:

```bash
python log_monitor.py system.log "ERROR" "WARNING" "CRITICAL"
```

### Options
- `--interval [seconds]`: Set how often the tool checks for new lines (default is 1.0).

## License
MIT
