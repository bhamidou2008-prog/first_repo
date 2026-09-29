student={'first_name': 'John',
          'last_name': 'Doe',
          'age': 20,
          'gender': 'male',
          'marital_status': 'single',
          'country':'senegal',
          'city':'Dakar',
          'skills':['Python', 'JavaScript', 'HTML', 'CSS'],}

student['skills'].append('Java')

del student['marital_status']

print(student)

del student

print(student)