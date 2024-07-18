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

LOCATIONS = {
  'Pittsburgh':'Pittsburgh, PA Metro Area',
  'LA': 'Los Angeles-Long Beach-Anaheim, CA Metro Area'
}

TIMEZONES = {
  'Pittsburgh':'America/New_York',
  'LA': 'America/Los_Angeles' 
}

# Columns in the dataframes that can (and must) be converted to dateTime objects.
# We define this as a constant, because they'll be needed when localizing times
TIME_COLUMNS = [
  'start_time', 
  'end_time', 
  'request_time'
]