"""
John (Jack) Risolo
Tuesday, 09/10/2024
Nassau Community College
Class Assignment #1 | Algorithm's
"""

DISCOUNT: float = 10.00



def avg_grade(*grades: int or float, rounding: int = 1) -> float:
    return round(sum(grades) / len(grades),rounding)

def fetch_discounted_price(price: float or int) -> float or int:
    # Decided to utilize max(0, price) because a discount cannot result in a negative price.
    return max(0, float(abs(price) - abs(DISCOUNT)))
    
    
print(avg_grade(60, 60, 60))


while True:
    instruction = input("Enter Instruction...")
    (call, command, *grades) = instruction.split()
    print(call, command, grades)
    if call.lower() == "grade":
        match str(command).lower():
            case "avg":
                for i in range(len(grades)):
                    if str(grades[i]).isnumeric():
                        grades[i] = int(grades[i])
                    elif str(grades[i]).isdecimal():
                        grades[i] = float(grades[i])
                    else:
                        del grades[i]
                        i -= 1
                print(f"AVG FROM GRADES IS {avg_grade(*grades)}")
                break
            case "alpha":
                for grade in grades:
                    if str(grade).isnumeric() or str(grade).isdecimal():
                        if grade >= 90: 
                            print(f"{grade} GRADE TO LETTER GRADE IS 'A'}) 
                        elif grade >= 80:
                            print(f"{grade} GRADE TO LETTER GRADE IS 'B'}) 
                        elif grade >= 70:
                            print(f"{grade} GRADE TO LETTER GRADE IS 'C'}) 
                        elif grade >= 60: 
                            print(f"{grade} GRADE TO LETTER GRADE IS 'D'}) 
                        else: 
                           print(f"{grade} GRADE TO LETTER GRADE IS 'F'}) 
        
print(fetch_discounted_price(5.99))
















class Grade:
    
    def __init__(self, grade: float or int, title: str = "Untitled Assignment", date: str = "Date Unknown"):
        self._grade = grade
        self.title = title
        self.date = date
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, new_grade: int or float):
        if not isinstance(new_grade, int) and not isinstance(new_grade, float):
            raise ValueError("Grade must be an integer or a float.")
        else:
            self._grade = new_grade
            
            
first = Grade(50.5)
print(first.grade)
