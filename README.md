# Daily System Status Checker

Daily System Status Checker is a small Python tool for checking DNS resolution and network reachability across multiple targets.

It resolves hostnames, runs ping checks, prints timestamped results to the terminal, and stores logs in daily log files for later review.

## Features

- DNS resolution (hostname to IP)
- Ping-based reachability checks
- Timestamped terminal output
- Daily log file generation
- Configurable targets through `config.json`
- Cross-platform use on Windows and Linux

## Files

- `main.py` – main script
- `config.json` – list of targets to check
- `README.md` – project documentation

## How It Works

1. The script loads targets from `config.json`
2. For each target, it:
   - resolves DNS
   - runs a ping test
   - records the result with a timestamp
3. Results are printed in the terminal
4. A daily log file is created automatically

## Configuration

Edit `config.json` to define the targets you want to monitor:

```json
{
  "targets": [
    "1.1.1.1",
    "cloudflare.com",
    "google.com"
  ]
}
```
## Running the Script
```bash
python main.py
```

## Example Output
```bash
[16:54:36] DNS OK for 1.1.1.1 -> 1.1.1.1 (5.33 ms)
[16:54:36] PING OK to 1.1.1.1 -> 19.56 ms
[16:54:36] DNS OK for cloudflare.com -> 104.16.132.229 (9.77 ms)
[16:54:36] PING OK to 104.16.132.229 -> 16.47 ms
```

## Why I built this

I wanted a simple tool to check the status of servers and services I use regularly without manually running repeated DNS and ping checks.

This project helped me practice Python while applying basic networking concepts in a practical way.

## Future improvements

- Failure alerts through webhook or email
- Continuous monitoring mode
- Simple dashboard for historical results
