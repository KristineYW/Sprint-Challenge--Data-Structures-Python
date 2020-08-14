class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # Create an empty list for ring buffer initialization
        self.data = []
        # Create a current index which we'll need to use the modulo on later
        self.cur_ind= 0

    def append(self, item):
        # Handle when the list is not full
        if len(self.data) < self.capacity:
            # Append the item to the end of the list
            self.data.append(item)
        # Handle when the list is full
        else: 
            # Update the oldest index on the list with the new item
            self.data[self.cur_ind] = item 
            # Update the current index using the modulo technique on the capacity
            self.cur_ind = (self.cur_ind + 1) % self.capacity

    def get(self):
        return self.data
