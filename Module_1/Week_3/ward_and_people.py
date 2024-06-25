'''
2. Một Ward (phường) gồm có name (string) và danh sách của mọi người trong Ward.
Một người person có thể là student, doctor, hoặc teacher. Một student gồm có name,
yob (int) (năm sinh), và grade (string). Một teacher gồm có name, yob, và subject
(string). Một doctor gồm có name, yob, và specialist (string). Lưu ý cần sử dụng a
list để chứa danh sách của mọi người trong Ward.
    (a) Cài đặt các class Student, Doctor, và Teacher theo mô tả trên. Thực hiện phương thức
        describe() method để in ra tất cả thông tin của các object.
    (b) Viết add_person(person) method trong Ward class để add thêm một người mới với nghề
        nghiệp bất kỳ (student, teacher, doctor) vào danh sách người của ward. Tạo ra một ward
        object, và thêm vào 1 student, 2 teacher, và 2 doctor. Thực hiện describe() method để in ra
        tên ward (name) và toàn bộ thông tin của từng người trong ward.
    (c) Viết count_doctor() method để đếm số lượng doctor trong ward.
    (d) Viết sort_age() method để sort mọi người trong ward theo tuổi của họ với thứ tự tăng dần.
    (e) Viết compute_average() method để tính trung bình năm sinh của các teachers trong ward...
'''


from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstract base class for Person.
    """

    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        """
        Get the year of birth.

        Returns:
            int: Year of birth.
        """
        return self._yob

    @abstractmethod
    def describe(self):
        """
        Abstract method to describe the person.
        """


class Student(Person):
    """
    Class representing a Student.
    """

    def __init__(self, name: str, yob: int, grade: str):
        """
        Initialize a Student object.

        Args:
            name (str): Name of the student.
            yob (int): Year of birth of the student.
            grade (str): Grade of the student.
        """
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        """
        Describe the student.
        """
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):
    """
    Class representing a Teacher.
    """

    def __init__(self, name: str, yob: int, subject: str):
        """
        Initialize a Teacher object.

        Args:
            name (str): Name of the teacher.
            yob (int): Year of birth of the teacher.
            subject (str): Subject taught by the teacher.
        """
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        """
        Describe the teacher.
        """
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):
    """
    Class representing a Doctor.
    """

    def __init__(self, name: str, yob: int, specialist: str):
        """
        Initialize a Doctor object.

        Args:
            name (str): Name of the doctor.
            yob (int): Year of birth of the doctor.
            specialist (str): Specialist area of the doctor.
        """
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        """
        Describe the doctor.
        """
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward:
    """
    Class representing a Ward (district).
    """

    def __init__(self, name: str):
        """
        Initialize a Ward object.

        Args:
            name (str): Name of the ward.
        """
        self.__name = name
        self.__list_people = []

    def add_person(self, person: Person):
        """
        Add a person to the ward.

        Args:
            person (Person): A Person object (Student, Teacher, or Doctor).
        """
        self.__list_people.append(person)

    def describe(self):
        """
        Describe the ward and its members.
        """
        print(f"Ward Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        """
        Count the number of doctors in the ward.

        Returns:
            int: Number of doctors in the ward.
        """
        
        count = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                count += 1
        return count

    def sort_age(self):
        """
        Sort the people in the ward by their age in ascending order.
        """
        self.__list_people.sort(key=lambda p: p.get_yob())

    def compute_average(self):
        """
        Compute the average year of birth of the teachers in the ward.

        Returns:
            float: Average year of birth of teachers, or None if no teachers are found.
        """
        teachers = [p for p in self.__list_people if isinstance(p, Teacher)]
        if not teachers:
            return None
        yobs = [p.get_yob() for p in teachers]
        return sum(yobs) / len(yobs)
