# import file_operations
# file_operations.save_to_file("Rolf", "data.txt")

from utils.common.file_operations import save_to_file, read_file
from utils.find import find_in

save_to_file("Rolf", "data.txt")
print(read_file("data.txt"))