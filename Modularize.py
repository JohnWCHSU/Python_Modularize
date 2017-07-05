# Pythone v3.6

# import library
import lib.import_lib

lib.import_lib.import_func()

del lib

#--------------------------------------------------#

# import library and rename
import lib.import_lib as rename_lib

rename_lib.import_func()

del rename_lib

#--------------------------------------------------#

# import the function or object from the library
from lib.import_lib import import_func

import_func()

del import_func

