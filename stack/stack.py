#!/usr/bin/bash python3
from copy import copy
import asyncio
class Stack(object):
    def __init__(self, max_size = 2046):
        self._stack_list = []
        self._len = 0
        self.max_size = max_size
        
    def get_stack(self):
        return self._stack_list
    
    def get_len(self):
        return self._len
    
    def is_full_stack(self):
        return self.get_len() >= self.max_size
    
    async def rpop(self):
        """
        出栈
        Returns:
             list
        """
        length = self.get_len()
        list_back = []
        if length != 0:
            list_back = self._stack_list.pop()
            
        return list_back
     
    async def lpush(self, sub_stack = None):
        """
         入栈
         Args:
              sub_stack: list data

         Returns:
              boolean
         """
        is_success = False
        if not self.is_full_stack():
            try:
                sub_stack = [sub_stack]
                self._stack_list.extend(list(sub_stack))
                self._len = len(self._stack_list)
                is_success = True
            except Exception:
                is_success = False
          
        return is_success

    async def _reverse_stack(self, reverse_stack = None, reverse_way = False):
        """
         将栈逆置（不可恢复性操作）
         Args:
              reverse_stack:
              reverse_way:

         Returns:
              boolean
        """
        if reverse_way:
            self._stack_list = reversed(self._stack_list)
            is_success = True
        else:
            _stack = copy(self._stack_list)
            try:
                while (len(_stack)):
                    reverse_stack.extend([_stack.pop()])
            
                self._stack_list = reverse_stack
                is_success = True
            except Exception:
                is_success = False
    
        return is_success

    async def reverse_stack(self, reverse_way = False):
        return await self._reverse_stack([], reverse_way = False)


