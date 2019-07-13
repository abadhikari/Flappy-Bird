class ListNode:
    def __init__(self, data, prev=None, link=None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self


class Deque:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def _add_between(self, item, before, after):
        node = ListNode(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._length += 1

    def add_first(self, item):
        self._add_between(item, None, self._head)

    def add_last(self, item):
        self._add_between(item, self._tail, None)

    def _remove(self, node):
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._length -= 1
        return node.data

    def remove_first(self):
        return self._remove(self._head)

    def remove_last(self):
        return self._remove(self._tail)

    def peek_head(self):
        return self._head.data

    def peek_tail(self):
        return self._tail.data

    def __len__(self):
        return self._length
