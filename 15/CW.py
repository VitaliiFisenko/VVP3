class stack:
    def __init__(self, obj_list=None):
        self.obj_list = obj_list or []

    def push(self, element):
        self.obj_list.insert(0, element)

    def pop(self):
        return self.obj_list.pop(0)

    def is_empty(self):
        if not self.obj_list:
            return True
        return False

    def top(self):
        return self.obj_list[0]


# stack_obj = stack([1, 2, 3, 45, 6, 6, 7])
# print(stack_obj.obj_list)
# print(stack_obj.top())
# print(stack_obj.is_empty())
# print(stack_obj.pop())
# print(stack_obj.obj_list)
# print(stack_obj.push(111))
# print(stack_obj.obj_list)


# d = {1: 1, 2: 2, 3: 3, 4: 4}
#
#
# for k, v in d.copy().items():
#     if k == 2:
#         d.pop(k)

class obj:
    def __init__(self, num, next_num):
        self.num = num
        self.next_num = next_num

    def __repr__(self):
        return f'{self.num} -> {self.next_num}'


class linked_list:
    def __init__(self):
        self.objects = []

    @property
    def prev_obj(self):
        if not self.objects:
            return
        index = len(self.objects) - 1
        return self.objects[index]

    def inset_at_end(self, num):
        if self.prev_obj:
            self.prev_obj.next_num = num
        self.objects.append(obj(num, None))

    def inset_at_head(self, num):
        self.objects.insert(0, obj(num, self.objects[0].num))

    def delete(self, index):
        self.objects.pop(index)
        self.objects[index - 1].next_num = self.objects[index].num

    def is_empty(self):
        if not self.objects:
            return False
        return True

    def delete_at_head(self):
        self.objects.pop(0)

    def search(self, obj_num):
        for obj in self.objects:
            if obj.num == obj_num:
                return obj


# l = linked_list()
# l.inset_at_end(1)
# print(l.objects)
# l.inset_at_end(2)
# print(l.objects)
# l.inset_at_head(3)
# print(l.objects)
# print(l.search(2))


class obj2:
    def __init__(self, num, prev_num, next_num):
        self.num = num
        self.prev_num = prev_num
        self.next_num = next_num

    def __repr__(self):
        return f'{self.prev_num} <- {self.num} -> {self.next_num}'


class linked_list2:
    def __init__(self):
        self.objects = []

    @property
    def prev_obj(self):
        if not self.objects:
            return
        index = len(self.objects) - 1
        return self.objects[index]

    def inset_at_end(self, num):
        if self.prev_obj:
            self.prev_obj.next_num = num
            self.objects.append(obj2(num, self.prev_obj.num, None))
            return
        self.objects.append(obj2(num, None, None))

    def inset_at_head(self, num):
        self.objects[0].prev_num = num
        self.objects.insert(0, obj2(num, None, self.objects[0].num))

    def delete(self, index):
        self.objects.pop(index)
        self.objects[index - 1].next_num = self.objects[index].num

    def is_empty(self):
        if not self.objects:
            return False
        return True

    def delete_at_head(self):
        self.objects.pop(0)

    def search(self, obj_num):
        for obj in self.objects:
            if obj.num == obj_num:
                return obj


# l = linked_list2()
# l.inset_at_end(1)
# print(l.objects)
# l.inset_at_end(2)
# print(l.objects)
# l.inset_at_head(3)
# print(l.objects)
# print(l.search(2))


class Element:
    def __init__(self, value, link):
        self.value = value
        self.link = link

    def __str__(self):
        return f'Value {self.value} --> link {self.link}'


class LinkedList:
    def __init__(self, data):
        self.data = data

    def insert_at_end(self, value):
        if len(self.data) == 0:
            self.data.append(Element(value, value))
            return
        self.data[-1].link = value
        self.data.append(Element(value, self.data[0].value))

    def insert_at_head(self, value):
        if len(self.data) == 0:
            self.data.append(Element(value, value))
            return
        self.data[-1].link = value
        self.data.insert(0, Element(value, self.data[0].value))

    def delete(self, index):
        self.data[index - 1].link = self.data[index].link
        self.data.pop(index)

    def delete_head(self):
        self.data.pop(0)
        self.data[-1].link = self.data[0].value

    def search(self, index):
        return self.data[index]

    def is_empty(self):
        return not bool(len(self.data))

    def __str__(self):
        return str([str(el) for el in self.data])


my_list = LinkedList([])

my_list.insert_at_end(1)
print(my_list)
my_list.insert_at_head(3)
print(my_list)
my_list.insert_at_head(5)
print(my_list)
my_list.insert_at_end(6)
print(my_list)
my_list.insert_at_end(4)
print(my_list)
my_list.delete_head()
print(my_list)
my_list.delete(1)
print(my_list)
my_list.delete_head()
print(my_list)
my_list.delete_head()
print(my_list)