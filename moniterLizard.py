import psutil
import time

def get_memory_info():
    mem_info = psutil.virtual_memory()
    total_memory = mem_info.total / (1024.0 ** 3)
    used_memory = mem_info.used / (1024.0 ** 3)
    return total_memory, used_memory

def get_network_info():
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_received = net_io.bytes_recv
    return bytes_sent, bytes_received

def main():
    print('Starting system monitor...')
    while True:
        total_memory, used_memory = get_memory_info()
        bytes_sent, bytes_received = get_network_info()
        print(f'Total memory: {total_memory} GB')
        print(f'Used memory: {used_memory} GB')
        print(f'Total bytes sent: {bytes_sent}')
        print(f'Total bytes received: {bytes_received}')
        time.sleep(1)

if __name__ == '__main__':
    main()
