import inotify.adapters
import os
import sys
from plyer import notification

def main(mount_point):
    # Create an inotify instance
    i = inotify.adapters.Inotify()

    # Add watch for the directory or file of interest
    i.add_watch(mount_point)

    print(f"Monitoring {mount_point} for read and write events...")

    # Listen for events
    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        file_path = os.path.join(path, filename)

        if 'IN_ACCESS' in type_names:
            print(f"Read operation detected on: {file_path}")
            notification.notify(
                title="Read Operation Detected",
                message=f"A read operation was detected on: {file_path}",
                app_name="SimpleFS Monitor",
                timeout=10  # Duration in seconds
            )
        elif 'IN_MODIFY' in type_names:
            print(f"Write operation detected on: {file_path}")
            notification.notify(
                title="Write Operation Detected",
                message=f"A write operation was detected on: {file_path}",
                app_name="SimpleFS Monitor",
                timeout=10  # Duration in seconds
            )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <mount_point>")
        sys.exit(1)

    mount_point = sys.argv[1]
    main(mount_point)
