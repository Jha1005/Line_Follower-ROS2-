import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pushpanjali/Downloads/serial_line_follower/install/my_bot'
