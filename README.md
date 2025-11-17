# Daily System Status Checker

A small Python tool that checks DNS resolution and network reachability for multiple targets.  
It logs results to daily log files and prints clean, timestamped output to the terminal.

## Features
- DNS resolution (hostname → IP)
- Ping test with latency measurement
- Daily log files stored automatically
- Configurable targets using `config.json`
- Works on Windows and Linux

## How It Works
1. The script loads target hostnames from `config.json`
2. For each target:
   - DNS is resolved
   - A ping test runs
   - Results are timestamped and logged in `/logs/YYYY-MM-DD.txt`
3. The terminal prints the results for quick checking

## Example Output
 [16:54:36] DNS OK for 1.1.1.1 -> 1.1.1.1 (5.33 ms)
 [16:54:36] PING OK to 1.1.1.1 -> 19.56 ms
 [16:54:36] DNS OK for cloudflare.com -> 104.16.132.229 (9.77 ms)
 [16:54:36] PING OK to 104.16.132.229 -> 16.47 ms


## Configuration
Edit `config.json` to add or remove targets:
{
    "targets": [
    "1.1.1.1",
    "cloudflare.com",
    "google.com"
    ]
}


## Running the Script
python main.py

Log files appear automatically inside the `logs` directory.

## Why I Built This
WAnted a simple tool to check the status of personal servers I host and use regularly. Instead of manually pinging, I built the script to automate DNS and reachability checks and log results over time. This project helped me refresh python and apply real networking concepts.

## Future Ideas
- webhook alerts on failure
- dashboard HTML page 
- continuous run option


