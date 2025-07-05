# def company_email(S):
    
#     result=[]
    
#     names=S.split(',')
#     for name in names:
#         result.append(name.strip())
#     # print (result)

#     splitted_name=[]
#     for name in result:
#         splitted_name.append(name.split())
#     # print(splitted_name)

#     final_names=[]
#     for names in splitted_name:
#         first_two=names[:2]
#         final_names.append(first_two)
#     print(final_names)


#     last_one=[]
#     for name in final_names:
#         joined=" ".join(name)
#         last_one.append(joined)

#     return last_one

    

# print(company_email("John Doe, Peter Parker, Mary Jane Watson-Parker, Aquila Jedidiah Wafula"))

def solution(S, C):
    #Convert company name to lowercase once

    company=C.lower()


    # split names by ", "

    names=S.split(', ')

    # dictionary to count occurences of emails prefixes
    email_counts={}

    # list to collect final formatted entries
    result=[]
