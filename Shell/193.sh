# 193. Valid Phone Numbers
#
# @date: 2017/01/24
# Read from the file file.txt and output all valid phone numbers to stdout.
awk '/^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/' file.txt