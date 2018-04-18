# -*- coding=utf8 -*-

__Author__ = 'majuchuan'


class people:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def eat(self):
        return "%s is eating, job is %s" % (self.name, self.job)

    def sleep(self):
        return "%s is sleeping, job is %s" % (self.name, self.job)


class student(people):
    def __init__(self, name, job):
        super().__init__(name, job)

    def study(self):
        return "%s is studying, job is %s" % (self.name, self.job)

    def intruduce(self):
        return "%s can intruduce,job is %s" % (self.name, self.job)


s = student('马晓明', 'CEO')
print(s.name)
print(s.job)
print(s.eat())
print(s.sleep())
print(s.study())
print(s.intruduce())

