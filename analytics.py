# Commit Analytics Script

import os
import subprocess

def get_total_commits():
    try:
        output = subprocess.check_output(["git", "rev-list", "--count", "HEAD"])
        return int(output.strip())
    except Exception as e:
        print(f"Error fetching commit count: {e}")
        return 0

if __name__ == "__main__":
    count = get_total_commits()
    print(f"Total repository commits: {count}")
