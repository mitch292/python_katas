class my_queue(object):
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