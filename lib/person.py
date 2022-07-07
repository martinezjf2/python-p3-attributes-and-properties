#!/usr/bin/env python3

class Person:
    
    jobs = ["Admin", "Finance", "Customer Service", "Sales", "Human Resources", "General Management", "ITC", "Research & Develpment", "Production", "Marketing", "Legal", "Purchasing"]
    
    def __init__(self):
        self._name = ''
        self._job = ''
        
    def set_name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            x = name.title()
            self._name = x
        else:
            print("Name must be string between 1 and 25 characters.")
            
    def get_name(self):
        return self._name
    
    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job in Person.jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
        
        
    name = property(get_name, set_name)
    job = property(get_job, set_job)
    pass