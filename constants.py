# # # # # #
# Imports #
# # # # # #

import operator 

# # # # # # #
# Constants #
# # # # # # #

OPS = {
  '<': operator.lt,
  '>': operator.gt,
  '<=': operator.le,
  '>=': operator.ge
} 

# Constants to multiply seconds by (e.g., mins = s * MINUTES)
# Used to make time calculations easier to read.
MINUTES = 60
HOURS = 60 * 60

