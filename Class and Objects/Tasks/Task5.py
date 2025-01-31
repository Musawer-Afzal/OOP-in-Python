# Problem 5 based on OOP Python.
# TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, 
# experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:
# eligibility criteria:
# if experience is more than 3 years, average feedback should be 4.5 or more
# if experience is 3 years or less, average feedback should be 4 or more
# he/she should posses the technology skill for the course
# Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its 
# attributes and methods.
# Note:
# Consider all instance variables to be private and methods to be public.
# An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
# check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
# allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor.    
# Else, return false.
# Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.



class Instructor:
    def __init__(self, name, experience, avg_feedback, technology_skills):
        self.__name = name
        self.__experience = experience
        self.__avg_feedback = avg_feedback
        self.__technology_skills = technology_skills  # List of skills

    def check_eligibility(self):
        if (self.__experience > 3 and self.__avg_feedback >= 4.5) or \
           (self.__experience <= 3 and self.__avg_feedback >= 4):
            return True
        return False

    def allocate_course(self, technology):
        if self.check_eligibility() and technology in self.__technology_skills:
            return True
        return False

    # Setter methods
    def set_experience(self, experience):
        self.__experience = experience

    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    def set_technology_skills(self, technology_skills):
        self.__technology_skills = technology_skills

    # Getter methods (if needed)
    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def get_avg_feedback(self):
        return self.__avg_feedback

    def get_technology_skills(self):
        return self.__technology_skills

# Testing the class
instructor1 = Instructor("Alice", 4, 4.6, ["Python", "Java"])
instructor2 = Instructor("Bob", 2, 4.1, ["C++", "JavaScript"])

print(f"Is {instructor1.get_name()} eligible? {instructor1.check_eligibility()}")  # True
print(f"Can {instructor1.get_name()} teach Python? {instructor1.allocate_course('Python')}")  # True
print(f"Can {instructor1.get_name()} teach C++? {instructor1.allocate_course('C++')}")  # False

print(f"Is {instructor2.get_name()} eligible? {instructor2.check_eligibility()}")  # True
print(f"Can {instructor2.get_name()} teach Java? {instructor2.allocate_course('Java')}")  # False