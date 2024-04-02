import random
PAGE_SIZE = 1024  # Page size in bytes
FRAME_SIZE = 1024  # Frame size in bytes
NUM_PAGES = 16  # Number of pages in logical memory
NUM_FRAMES = 8  # Number of frames in physical memory
SECONDARY_STORAGE = {}  # Secondary storage to simulate disk storage

def generate_logical_address():
    return random.randint(0, (NUM_PAGES * PAGE_SIZE) - 1)  # Generates a random logical address within the range of logical memory


def handle_page_fault(page_number):
    if page_number not in SECONDARY_STORAGE:
        # Simulate loading page from disk into memory
        SECONDARY_STORAGE[page_number] = [random.randint(0, 255) for _ in range(PAGE_SIZE)]  # Generate random page data
    # Return the loaded page from secondary storage
    return SECONDARY_STORAGE[page_number]


def main():
    random.seed()  # Seed random number generator

    # Initialize page/frame table
    page_frame_table = [-1] * NUM_PAGES  # Page/frame table initialized with -1 indicating no mapping initially

    # Allocate frames in physical memory
    physical_memory = [-1] * NUM_FRAMES  # Physical memory initialized with -1 indicating empty frames initially

    # Fill page/frame table and physical memory
    for i in range(NUM_PAGES):
        page_frame_table[i] = i % NUM_FRAMES  # Circular mapping of pages to frames ensures each page has a corresponding frame

    # Input logical addresses in hexadecimal format
    logical_addresses = ["0x3A7F", "0xABCD", "0x5678"]

    # Translate logical addresses to physical addresses
    for address in logical_addresses:
        logical_address = int(address, 16)  # Convert hexadecimal string to integer
        page_number = (logical_address // PAGE_SIZE) & 0x0F  # Calculate the page number from the logical address
        offset = logical_address & 0xFF # Calculate the offset within the page from the logical address

        if page_number < NUM_PAGES:  # Check if the page number is within the valid range
            frame_number = page_frame_table[page_number]  # Retrieves the frame number corresponding to the page from the page/frame table

            if frame_number == -1:  # Page fault handling
                print(f"Page fault occurred for page {page_number}. Loading page from secondary storage...")
                page_data = handle_page_fault(page_number)
                # Load page into physical memory
                frame_number = page_number % NUM_FRAMES
                physical_memory[frame_number] = page_data
                page_frame_table[page_number] = frame_number  # Update page/frame table
                print(f"Page {page_number} loaded into frame {frame_number}.")

            physical_address = (frame_number * FRAME_SIZE) + offset  # Calculate the physical address by adding offset to the base address of the frame

            print(f"Logical Address: {address} => Page Number: 0x{page_number:02X}, Offset: 0x{offset:2X} => Physical Address: 0x{physical_address:X}")  
        else:
            print(f"Invalid Page Number for Logical Address: {address}")  # Prints an error message for invalid page number


if __name__ == "__main__":
    main()