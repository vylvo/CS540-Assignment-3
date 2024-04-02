# CS540-Assignment-3
Link: [CS540 Assignment 3.py](https://github.com/vylvo/CS540-Assignment-3/blob/ebd98d2e74671b1a0276fee4942fbaf3b75bb55c/CS540%20Assignment%203.py)

# Memory Management and Address Translation
Program Functionality
This Python script demonstrates memory management and address translation concepts by implementing a page/frame table to map logical addresses to physical addresses. The program simulates memory allocation, page faults, and page loading from secondary storage.

Functionality:
- Page/Frame Table: Implements a page/frame table data structure to map logical page numbers to physical frame numbers.
- Logical to Physical Address Translation: Translates logical addresses (consisting of a page number and an offset) to physical addresses using the page/frame table. Handles page faults by loading pages from secondary storage into memory when necessary.
- Output: Provides the corresponding page numbers and offsets for given logical addresses in hexadecimal format.
Instructions for Execution:
1. Ensure you have Python installed on your system. If not, download and install Python from python.org.
2. Clone or download the script file memory_management.py.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the following command:
python memory_management.py
5. The program will execute and display the logical addresses along with their corresponding page numbers, offsets, and physical addresses.
6. Review the output to verify the correctness of address translation and handling of page faults.

Logical Address: 0x3A7F => Page Number: 0x0D, Offset: 0x7F => Physical Address: 0x187F
Logical Address: 0xABCD => Page Number: 0x0A, Offset: 0xCD => Physical Address: 0x8CD
Logical Address: 0x5678 => Page Number: 0x05, Offset: 0x78 => Physical Address: 0x1478
