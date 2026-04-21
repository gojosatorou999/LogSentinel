import os
import time
import argparse
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def monitor_log(file_path, keywords, interval=1.0):
    """
    Monitors a log file for specific keywords in real-time.
    """
    if not os.path.exists(file_path):
        print(f"{Fore.RED}Error: File '{file_path}' does not exist.")
        return

    print(f"{Fore.CYAN}Monitoring {Fore.YELLOW}{file_path}{Fore.CYAN} for keywords: {Fore.GREEN}{', '.join(keywords)}")
    print(f"{Fore.DIM}Press Ctrl+C to stop.{Style.RESET_ALL}\n")

    try:
        with open(file_path, 'r', errors='ignore') as f:
            # Move to the end of the file
            f.seek(0, os.SEEK_END)
            
            while True:
                line = f.readline()
                if not line:
                    time.sleep(interval)
                    continue
                
                line = line.strip()
                match_found = False
                highlighted_line = line
                
                for keyword in keywords:
                    if keyword.lower() in line.lower():
                        match_found = True
                        # Highlight the keyword
                        highlighted_line = highlighted_line.replace(
                            keyword, f"{Fore.RED}{Style.BRIGHT}{keyword}{Style.RESET_ALL}"
                        )
                
                if match_found:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"[{Fore.MAGENTA}{timestamp}{Fore.RESET}] {highlighted_line}")
                
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}Monitoring stopped.")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Python Log Monitor Tool")
    parser.add_argument("file", help="Path to the log file to monitor")
    parser.add_argument("keywords", nargs="+", help="Keywords to search for in the log file")
    parser.add_argument("--interval", type=float, default=1.0, help="Check interval in seconds (default: 1.0)")

    args = parser.parse_args()
    
    monitor_log(args.file, args.keywords, args.interval)

if __name__ == "__main__":
    main()
