# SimpleFS Monitoring Script

This project provides a Python script to monitor read and write operations on files within the SimpleFS filesystem. The script uses `inotify` to detect file operations and `plyer` to send desktop notifications.

## Prerequisites

Ensure you have Python 3 installed on your system. Ensure the instructions for mounting the block device with the filesystem in the `Build and Run` section in the main `README.md` has been followed.

## Setup

### Using a Virtual Environment

1. **Create a virtual environment:**

   ```sh
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**

    ```sh
    source venv/bin/activate
    ```

3. **Install the required packages:**

   ```sh
   pip install inotify plyer
   ```

## Usage

Run the Python script with the mount point of the SimpleFS filesystem as an argument:

```sh
python monitor_simplefs.py /path/to/simplefs/mount
```

### Example

```sh
python monitor_simplefs.py ../../test/
```

This will monitor the specified mount point for read and write operations and send desktop notifications with details about each detected operation.

## Features

- Monitors read operations on files in the SimpleFS filesystem.
- Monitors write operations on files in the SimpleFS filesystem.
- Sends desktop notifications with details of the detected operations.

## Explanation

The script initializes an inotify instance to watch for `IN_ACCESS` (read) and `IN_MODIFY` (write) events. When such an event is detected, it sends a desktop notification with the file path.