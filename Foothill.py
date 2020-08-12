"""
*Program 10 : Foothill
*Programmer: Chandler Kilpatrick
*Due: 12/10/19
*CS 3A, Fall 2019
*Description: This program will sort and display several arrays.
""" 


# beginning of class Student definition -------------------------
class Student:
   
   # class ("static") attributes and intended constants
   DEFAULT_NAME =  "zz-error"
   DEFAULT_POINTS = 0
   MAX_POINTS = 30
   SORT_BY_FIRST = 88
   SORT_BY_LAST = 98
   SORT_BY_POINTS = 108
   sort_key = SORT_BY_LAST




   # initializer ("constructor") method -------------------
   def __init__(self,
                last = DEFAULT_NAME,
                first = DEFAULT_NAME,
                points = DEFAULT_POINTS):
      # instance attributes
      if (not self.set_last_name(last)):
         self.last_name = Student.DEFAULT_NAME
      if (not self.set_first_name(first)):
         self.first_name = Student.DEFAULT_NAME
      if (not self.set_points(points)):
         self.total_points = Student.DEFAULT_POINTS




   # mutator ("set") methods -------------------------------
   def set_last_name(self, last):
      if not self.valid_string(last):
         return False
      # else
      self.last_name = last
      return True

   def set_first_name(self, first):
      if not self.valid_string(first):
         return False
      # else
      self.first_name = first
      return True
   
   def set_points(self, points):
      if not self.valid_points(points):
         return False
      # else
      self.total_points = points
      return True



   
   # accessor ("get") methods -------------------------------
   def get_last_name(self):
        return self.last_name

   def get_first_name(self):
        return self.first_name
   
   def get_total_points(self):
        return self.total_points
    


    

   # output method  ----------------------------------------
   def display(self, client_intro_str = "--- STUDENT DATA ---"):
      print( client_intro_str + str(self) )





   # standard python stringizer ------------------------
   def __str__(self):
      return self.to_string()





   # instance helpers -------------------------------
   def to_string(self, optional_title = " ---------- "):
      ret_str = ( (optional_title
                   + "\n    name: {}, {}"
                   + "\n    total points: {}.").
                  format(self.last_name , self.first_name,
                         self.total_points) )
      return ret_str





   # static/class methods -----------------------------------

   @classmethod
   def compare_two_students(cls, first_stud, second_stud):
      
      if cls.sort_key == cls.SORT_BY_FIRST:
         return (cls.compare_strings_ignore_case(first_stud.get_first_name(),
                                     second_stud.get_first_name()))
      
      elif cls.sort_key == cls.SORT_BY_LAST:
         return (cls.compare_strings_ignore_case(first_stud.get_last_name(),
                                     second_stud.get_last_name()))
      
      elif cls.sort_key == cls.SORT_BY_POINTS:
         return (second_stud.get_total_points() - first_stud.get_total_points())
         
                                     

      
   @staticmethod
   def get_sort_key(cls):
        return cls.sort_key
      
   @staticmethod
   def set_sort_key(cls, key):
      cls.sort_key = key
      
   
   @staticmethod
   def valid_string(test_str):
      if (len(test_str) > 0) and test_str[0].isalpha():
         return True;
      return False

   @classmethod     
   def valid_points(cls, test_points):
      if 0 <= test_points <= cls.MAX_POINTS:
         return False
      else:
         return True

   @staticmethod   
   def compare_strings_ignore_case(first_string, second_string):
      """ returns -1 if first < second, lexicographically,
         +1 if first > second, and 0 if same
         this particular version based on last name only
         (case insensitive) """
      
      fst_upper = first_string.upper()
      scnd_upper = second_string.upper()
      if fst_upper < scnd_upper:
         return -1
      # else if
      if fst_upper > scnd_upper:
         return 1
      # else
      return 0








# beginning of class StudentArrayUtilities definition ---------------
class StudentArrayUtilities:

   @classmethod
   def get_median_destructive(cls, array, array_size):

      saved_sort_key = Student.get_sort_key(Student)
      Student.set_sort_key(Student, Student.SORT_BY_POINTS)
      StudentArrayUtilities.array_sort(array, array_size)
      Student.set_sort_key(Student, saved_sort_key)
      array_size = int(array_size)
      
      if array_size == 1:
         
         return (array[0].get_total_points())
      
      elif array_size % 2 == 0 and array_size >= 2:
         
         return ((array[array_size // 2].get_total_points() +
                  array[array_size // 2 + 1].get_total_points()) // 2)
      
      elif array_size % 2 != 0 and array_size >= 3:
         
         return (array[array_size//2 + 1].get_total_points())
         
      else:
         
         return 0
   
      
         
   
   @classmethod
   def to_string(cls, stud_array, 
                   optional_title = "--- The Students -----------:\n"):
      return( cls.to_string(stud_array, optional_title) )

   @classmethod
   def array_sort(cls, data, array_size):
      for k in range(array_size):
         if not cls.float_largest_to_top(data, array_size - k):
            return

   @staticmethod
   def float_largest_to_top(data, array_size):
      
      changed = False
      
      # notice we stop at array_size - 2 because of expr. k + 1 in loop
      for k in range(array_size - 1):
         
         if Student.compare_two_students(data[k], data[k + 1]) > 0:
            
            data[k], data[k+1] = data[k + 1], data[k]
            changed = True;
      return changed

   NOT_FOUND = -1   # static constant best defined at top of class
   @classmethod
   def array_search(cls, data, array_size, key_first, key_last):
      for k in range(array_size):
          if ( data[k].get_last_name() == key_last
               and data[k].get_first_name() == key_first ):
             return k  # found match, return index
      return cls.NOT_FOUND

   @classmethod
   def binary_search_for_last_name(cls, data, key_last_nm,
                     first_index, last_index):
      # exhuasted search
      if (first_index > last_index):
         return cls.NOT_FOUND
      
      middle_index = int( (first_index + last_index) / 2 )
      
      result = Student.compare_strings_ignore_case(
         key_last_nm,
         data[middle_index].get_last_name()
         )

      # < 0 means key before middle index
      if (result < 0):
         return cls.binary_search_for_last_name(
            data, key_last_nm, first_index, middle_index - 1)

      # > 0 means key after middle index
      if (result > 0):
         return cls.binary_search_for_last_name(
            data, key_last_nm, middle_index + 1, last_index)
      
      # else key IS in middle index position, i.e., found him
      return middle_index   

   # class stringizers ----------------------------------
   @staticmethod
   def to_string(stud_array, 
                   optional_title = "--- The Students -----------:\n"):
      ret_val = optional_title + "\n"
      for student in stud_array:   
         ret_val = ret_val + str(student) + "\n"
      return ret_val

# client --------------------------------------------

# instantiate some students, one with an illegal name ...  
my_students = \
         [
            Student("smith","fred", 95),
            Student("bauer","jack",123),
            Student("jacobs","carrie", 195),
            Student("renquist","abe",148),
            Student("3ackson","trevor", 108),
            Student("perry","fred",225),
            Student("lewis","frank", 44),
            Student("stollings","pamela",452),
            Student("jones","bob",253),
            Student("halpert","jim",173),
            Student("scott","michael",421),
            Student("malon","kevin",382),
            Student("shrute","dwight",203),
            Student("bratten","creed",186),
            Student("flenterson","toby",224)
            
         ]

my_students_two = \
         [
            Student("smith","fred", 95),
            Student("bauer","jack",123),
            Student("jacobs","carrie", 195),
            Student("renquist","abe",148),
            Student("jackson","trevor", 108),
            Student("perry","fred",225),
            Student("lewis","frank", 44),
            Student("stollings","pamela",452),
            Student("jones","bob",253),
            Student("halpert","jim",173),
            Student("scott","michael",421),
            Student("malon","kevin",382),
            Student("shrute","dwight",203),
            Student("bratten","creed",186),
            Student("flenterson","toby",224),
            Student("hudson","stanley",332)
         ]

my_students_three = \
         [
            Student("kilpatrick","kevin", 60)

         ]
print(StudentArrayUtilities.to_string(my_students_two, "Before default sort : "))
print()
array_size = len(my_students_two)

StudentArrayUtilities.array_sort(my_students_two, array_size)
print(StudentArrayUtilities.to_string(my_students_two, "After default sort : "))
print()

Student.set_sort_key(Student, Student.SORT_BY_FIRST)
StudentArrayUtilities.array_sort(my_students_two, array_size)
print(StudentArrayUtilities.to_string(my_students_two, "After sort BY FIRST:: "))
print()

Student.set_sort_key(Student, Student.SORT_BY_POINTS)
StudentArrayUtilities.array_sort(my_students_two, array_size)
print(StudentArrayUtilities.to_string(my_students_two, "After sort BY POINTS:: "))
print()

Student.set_sort_key(Student, Student.SORT_BY_FIRST)
before_value = Student.get_sort_key(Student)
StudentArrayUtilities.array_sort(my_students_two, array_size)
print("Median of even class = " +
       str(StudentArrayUtilities.get_median_destructive(my_students_two, array_size)))

after_value = Student.get_sort_key(Student)
if after_value == before_value:
   print("Successfully preserved sort key.")

array_size_one = len(my_students)
print("Median of odd class = " +
       str(StudentArrayUtilities.get_median_destructive(my_students, array_size_one)))

array_size_three = len(my_students_three)
print("Median of small class = " +
       str(StudentArrayUtilities.get_median_destructive(my_students_three, array_size_three)))






# search for two names in the list
# I wasn't sure if I should delete this code or not. It still runs if needed.
'''
last_name = "jacobs"
found = StudentArrayUtilities.binary_search_for_last_name(my_students_two,
                                            last_name,
                                            0, array_size - 1)
if found != StudentArrayUtilities.NOT_FOUND:
   print( last_name + " IS in list at position " + str(found) )
else:
   print( last_name + " is NOT in list." )

last_name = "Stollings"
found = StudentArrayUtilities.binary_search_for_last_name(my_students_two,
                                            last_name,
                                            0, array_size - 1)
if found != StudentArrayUtilities.NOT_FOUND:
   print( last_name + " IS in list at position " + str(found) )
else:
   print( last_name + " is NOT in list." )

# search for someone NOT in the list
last_name = "hendry"
found = StudentArrayUtilities.binary_search_for_last_name(my_students_two,
                                            last_name,
                                            0, array_size - 1)
if found != StudentArrayUtilities.NOT_FOUND:
   print( last_name + " IS in list at position " + str(found) )
else:
   print( last_name + " is NOT in list." )
'''






"""                         MY RUNS

##################################################################

========== RESTART: /Users/chandlerkilpatrick/Downloads/Foothill.py ==========
Before default sort : 
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: jackson, trevor
    total points: 108.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: lewis, frank
    total points: 44.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: jones, bob
    total points: 253.
 ---------- 
    name: halpert, jim
    total points: 173.
 ---------- 
    name: scott, michael
    total points: 421.
 ---------- 
    name: malon, kevin
    total points: 382.
 ---------- 
    name: shrute, dwight
    total points: 203.
 ---------- 
    name: bratten, creed
    total points: 186.
 ---------- 
    name: flenterson, toby
    total points: 224.
 ---------- 
    name: hudson, stanley
    total points: 332.


After default sort : 
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: bratten, creed
    total points: 186.
 ---------- 
    name: flenterson, toby
    total points: 224.
 ---------- 
    name: halpert, jim
    total points: 173.
 ---------- 
    name: hudson, stanley
    total points: 332.
 ---------- 
    name: jackson, trevor
    total points: 108.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: jones, bob
    total points: 253.
 ---------- 
    name: lewis, frank
    total points: 44.
 ---------- 
    name: malon, kevin
    total points: 382.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: scott, michael
    total points: 421.
 ---------- 
    name: shrute, dwight
    total points: 203.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: stollings, pamela
    total points: 452.


After sort BY FIRST:: 
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: jones, bob
    total points: 253.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: bratten, creed
    total points: 186.
 ---------- 
    name: shrute, dwight
    total points: 203.
 ---------- 
    name: lewis, frank
    total points: 44.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: halpert, jim
    total points: 173.
 ---------- 
    name: malon, kevin
    total points: 382.
 ---------- 
    name: scott, michael
    total points: 421.
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: hudson, stanley
    total points: 332.
 ---------- 
    name: flenterson, toby
    total points: 224.
 ---------- 
    name: jackson, trevor
    total points: 108.


After sort BY POINTS:: 
 ---------- 
    name: stollings, pamela
    total points: 452.
 ---------- 
    name: scott, michael
    total points: 421.
 ---------- 
    name: malon, kevin
    total points: 382.
 ---------- 
    name: hudson, stanley
    total points: 332.
 ---------- 
    name: jones, bob
    total points: 253.
 ---------- 
    name: perry, fred
    total points: 225.
 ---------- 
    name: flenterson, toby
    total points: 224.
 ---------- 
    name: shrute, dwight
    total points: 203.
 ---------- 
    name: jacobs, carrie
    total points: 195.
 ---------- 
    name: bratten, creed
    total points: 186.
 ---------- 
    name: halpert, jim
    total points: 173.
 ---------- 
    name: renquist, abe
    total points: 148.
 ---------- 
    name: bauer, jack
    total points: 123.
 ---------- 
    name: jackson, trevor
    total points: 108.
 ---------- 
    name: smith, fred
    total points: 95.
 ---------- 
    name: lewis, frank
    total points: 44.


Median of even class = 190
Successfully preserved sort key.
Median of odd class = 186
Median of small class = 60

##################################################################



##################################################################
"""
