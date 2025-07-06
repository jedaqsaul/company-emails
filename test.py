# # # Create a function that takes a string of names and returns each individual names' in a list

# # # return a list


# # def split_names(S):
# #     result=[]
# #     names=S.split(",")

# #     for name in names:
# #         new_name=name.strip()
# #         result.append(new_name)

# #     return result
# #     # remove_spaces=names.strip()
# #     # return remove_spaces




# # print(split_names("John Doe, Peter Parker, Mary Jane Watson-Parker"))


# people = {
#     "John": 1,
#     "Mary": 1,
#     "Kevin":3,
#     "Sara": 3,
#     "David": 4
# }

# print(people)
# print(people["David"]+1)

# people["aquila"]=2
# people["jedidiah"]=4+6
# print(people)


def solution_moringa(S, C):
    company=C.lower()
    names=S.split(", ")

    

    email_count={}
    result=[]


    for full_names in names:
        parts=full_names.strip().split()
       


        first_name=parts[0]
        second_name=parts[1]

        prefix=(first_name+second_name).lower()
        

        student_email=f"{prefix}@student.{company}school.com"
        

        entry=f"{full_names} <{student_email}>"

        result.append(entry)

    return ", ".join(result)


print(solution_moringa("Aquila Jedidiah Wafula, Natasha Onsongo, Grace Zawadi Wairimu, Eugene Wekesa Wanyonyi, Edwin Korir, Joy Malinda, Celestine Mecheo", "Moringa"))