# -*- coding: utf-8 -*-
"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作：
获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥已经存在，则变更其数据值；如果密钥不存在，
则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，
从而为新的数据值留出空间。
"""


class LinkedNode(object):

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def _move_to_head(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
        self._add_node(node)

    def _add_node(self, node):
        head_next = self.head.next
        self.head.next = node
        head_next.prev = node
        node.next = head_next
        node.prev = self.head

    def _remove_tail(self):
        tail_prev = self.tail.prev
        new_prev = tail_prev.prev
        new_prev.next = self.tail
        self.tail.prev = new_prev
        return tail_prev

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head, self.tail = LinkedNode(), LinkedNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.linked_list = None

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            new_node = LinkedNode(key, value)

            self._add_node(new_node)
            self.cache[key] = new_node
            self.size += 1

            if self.size > self.capacity:
                tail = self._remove_tail()
                self.size -= 1
                self.cache.pop(tail.key)
        else:
            node.value = value
            self._move_to_head(node)


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(5)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
