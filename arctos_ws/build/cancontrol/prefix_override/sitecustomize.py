import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/louis/Projects/arctoshumble/arctos_ws/install/cancontrol'
