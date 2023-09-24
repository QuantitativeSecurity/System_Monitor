System Monitor

This script provides a simple system monitor to display memory usage and network I/O statistics in real-time.
Features:

    Displays total and used memory in GB.
    Displays total bytes sent and received over the network.

Dependencies:

    psutil: This module provides an interface for retrieving information on system utilization (CPU, memory, disks, network, sensors).
    time: This module provides various time-related functions.

How to Use:

    Ensure you have the psutil library installed. You can install it using pip:

pip install psutil

Run the script:

    python system_monitor.py

    The script will start displaying memory and network statistics every second. To stop the script, press CTRL+C.

Functions:

    get_memory_info(): Returns the total and used memory in GB.

    get_network_info(): Returns the total bytes sent and received over the network.

    main(): The main function that starts the system monitoring process. It fetches memory and network statistics, prints them, and then waits for a second before repeating.

Note:

Keep in mind that the displayed network statistics are cumulative since system boot-up or the last reset. They do not represent the current bandwidth usage per second.
