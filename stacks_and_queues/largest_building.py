def largest_rectangle(h):
    n = len(h) + 1
    largest_building = 0
    building_queue = Queue()
    
    for i in range(n):
        for j in range(i, n):
            if i < j:
                building_queue.put(h[i:j])
    
    while not building_queue.is_empty():
        new_plan = building_queue.pop()
        new_building_size = min(new_plan) * len(new_plan)
        if largest_building < new_building_size:
            largest_building = new_building_size
8
    return largest_building


class Queue(object):
    def __init__(self):
        self._data = []
    
    def peek(self):
        if len(self._data) > 0:
            return self._data[0]
        return None

    def pop(self):
        if len(self._data) > 0:
            return self._data.pop(0)
        return None
        
    def put(self, value):
        self._data.append(value)
    
    def is_empty(self):
        return len(self._data) == 0


if __name__ == "__main__":
    print(largest_rectangle([1,2,3,4,5]))