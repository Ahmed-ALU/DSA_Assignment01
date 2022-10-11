from ast import operator
from inspect import stack
import pstats
import re
# self.list = listt
operation_stack_undo = stack()
operation_stack_redo = stack()
redoo = False
# counter = int()
class Undoablelist():
    global operation_stack_undo, redoo, operation_stack_redo, counter
    def __init__(self, listt):
        self.listt = list(listt)

    def insert(self, item):
        counter = int()
        # if redoo == False:
        #     operation_stack_redo.clear()
        # elif redoo == True:
        #     pass
        temp_list = list()
        self.listt.sort()
        for i in self.listt:
            counter += 1
            if i <= item:
                temp_list.append(i)
                if counter == len(self.listt):
                    temp_list.append(item)
                    self.listt = temp_list
                    operation_stack_undo.append(f"add{item}")
                    return self.listt
            elif i > item :
                index = self.listt.index(i)
                temp_list.append(item)
                for j in self.listt[index:]:
                    temp_list.append(j)
                self.listt = temp_list
                operation_stack_undo.append(f"add{item}")
                return self.listt
    
    def delete(self, item):
        # if redoo == False:
        #     operation_stack_redo.clear()
        # elif redoo == True:
        #     pass

        if item in self.listt:
            self.listt.remove(item)
            operation_stack_undo.append(f"del{item}")
            return self.listt
        else:
            # operation_stack_undo.append(f"None")
            return self.listt

    def undo(self):
        
        if str(operation_stack_undo[-1]).startswith("add"):
            self.delete(int(operation_stack_undo[-1][3]))
            operation_stack_undo.pop()
            temp_text = str(operation_stack_undo.pop())
            if temp_text.startswith("add"):
                text = "del"+temp_text[3]
                operation_stack_redo.append(text)
            elif temp_text.startswith("del"):
                text = "add"+temp_text[3]
                operation_stack_redo.append(text2)
            elif temp_text.startswith("None"):
                operation_stack_redo.append("None")
            return self.listt
            
        elif str(operation_stack_undo[-1]).startswith("del"):
            self.insert(int(operation_stack_undo[-1][3]))
            operation_stack_undo.pop()
            temp2_text = str(operation_stack_undo.pop())
            if temp2_text.startswith("add"):
                text2 = "del"+temp2_text[3]
                operation_stack_redo.append(text2)
            elif temp2_text.startswith("del"):
                text2 = "add"+temp2_text[3]
                operation_stack_redo.append(text2)
            elif temp2_text.startswith("None"):
                operation_stack_redo.append("None")
            return self.listt
        elif str(operation_stack_undo[-1]).startswith("None"):
            operation_stack_undo.pop()
            return self.listt
        else:
            return self.listt

    def redo(self):
        if len(operation_stack_redo) > 0:
            if str(operation_stack_redo[-1]).startswith("add"):
                redo = True
                self.delete(int(operation_stack_redo[-1][3]))
                operation_stack_undo.pop()
                operation_stack_redo.pop()
                return self.listt
                
            elif str(operation_stack_redo[-1]).startswith("del"):
                self.insert(int(operation_stack_redo[-1][3]))
                operation_stack_undo.pop()
                try:
                    operation_stack_redo.pop()
                except BaseException:
                    pass
                return self.listt
            elif str(operation_stack_redo[-1]).startswith("None"):
                return self.listt
                pass
            else:
                return self.listt
        else: 
            return self.listt

lis = Undoablelist([1, 2, 3])
print(lis.insert(4))
print(lis.delete(2))
# print (operation_stack_undo, end= "\n\n")
print(lis.undo())
print(lis.undo())
print(lis.undo())
# print (operation_stack_redo, end= "\n\n")
print(lis.redo())
print(lis.redo())
print(lis.insert(5))
print(lis.redo())
print(lis.delete(7))
print(lis.undo())
print(lis.undo())


# print (operation_stack_undo, end= "\n\n")
# print(lis.undo())
# print (operation_stack_undo, end= "\n\n")
# print(lis.undo())

# print (operation_stack_redo)


