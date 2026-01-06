class MyCircularQueue:
    """
    Circular Queue Implementation
    
    Like a carousel with fixed seats - when we reach the end,
    we wrap around to the beginning if there's space.
    """

    def __init__(self, k: int):
        """Initialize with k slots"""
        self.queue = [0] * k  # Fixed-size array
        self.head = 0         # Points to front element
        self.count = 0        # Current number of elements
        self.capacity = k     # Maximum capacity

    def enQueue(self, value: int) -> bool:
        """Add element to rear. Like someone boarding the carousel."""
        if self.isFull():
            return False
        
        # Calculate rear position: (head + count) wraps around
        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """Remove element from front. Like someone getting off the carousel."""
        if self.isEmpty():
            return False
        
        # Move head forward (with wraparound)
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """Get front element without removing it"""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """Get rear element without removing it"""
        if self.isEmpty():
            return -1
        # Rear is at (head + count - 1) position, the 
        # Reason why we need to -1 is because the head is the first element, and the count is the number of elements, 
        # so the rear is the last element, so we need to -1 to get the last element
        tail = (self.head + self.count - 1) % self.capacity
        return self.queue[tail]

    def isEmpty(self) -> bool:
        """Check if carousel is empty"""
        return self.count == 0

    def isFull(self) -> bool:
        """Check if carousel is full"""
        return self.count == self.capacity


# please clarify the circular queue with vivid examples in "Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values."

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# idea: use a list to store the queue, and use two pointers to point to the front and rear of the queue

# Operation → Pointer Movement
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# enQueue() → REAR moves forward  ➡️
# deQueue() → FRONT moves forward ➡️
# All others → NO movement        ⏸️

def demonstrate_circular_queue():
    """
    🎠 VIVID DEMONSTRATION: Circular Queue in Action
    
    Imagine a 3-seat carousel where people board and exit
    """
    print("🎠 Welcome to the Circular Queue Carousel!")
    print("=" * 50)
    
    # Create a small circular queue for clear demonstration
    cq = MyCircularQueue(3)
    
    def show_state():
        """Helper to visualize current state"""
        print(f"Queue: {cq.queue}")
        print(f"Head: {cq.head}, Count: {cq.count}, Capacity: {cq.capacity}")
        print(f"Empty: {cq.isEmpty()}, Full: {cq.isFull()}")
        if not cq.isEmpty():
            print(f"Front: {cq.Front()}, Rear: {cq.Rear()}")
        print("-" * 30)
    
    print("\n📥 Step 1: Add passengers 10, 20, 30")
    cq.enQueue(10)
    print("Added 10:")
    show_state()
    
    cq.enQueue(20)
    print("Added 20:")
    show_state()
    
    cq.enQueue(30)
    print("Added 30 (FULL!):")
    show_state()
    
    print("\n🚫 Step 2: Try to add 40 (should fail - carousel full)")
    result = cq.enQueue(40)
    print(f"Adding 40: {result} (False = failed)")
    show_state()
    
    print("\n📤 Step 3: Remove passengers from front")
    cq.deQueue()  # Remove 10
    print("Removed passenger at front (10):")
    show_state()
    
    cq.deQueue()  # Remove 20
    print("Removed passenger at front (20):")
    show_state()
    
    print("\n✨ Step 4: THE MAGIC - Add new passengers 40, 50")
    print("Watch how we reuse the freed seats!")
    
    cq.enQueue(40)
    print("Added 40 (uses seat 0 - wraparound!):")
    show_state()
    
    cq.enQueue(50)
    print("Added 50 (uses seat 1 - wraparound!):")
    show_state()
    
    print("\n🎯 RESULT: We reused seats 0 and 1 that were freed earlier!")
    print("This is the power of circular queues - no wasted space!")

if __name__ == "__main__":
    demonstrate_circular_queue()