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

    for full_name in names:

        # split name into two parts
        parts=full_name.strip().split()
        # print(parts)
        

        # first initial

        first_initial=parts[0][0].lower()
        
        # check if there is a middle name

        if len(parts)==3:
            middle_initial=parts[1][0].lower()
            last_name=parts[2]
        else:
            middle_initial=""
            last_name=parts[1]

        # remove hyphens from last name
        last_name_clean=last_name.replace("-", "").lower()

        
        # Truncate to first 8 letters
        last_name_trunc=last_name_clean[:8]

        # Build email prefix

        prefix=first_initial+middle_initial+last_name_trunc
       

        # handle duplicates

        if prefix in email_counts:
            email_counts[prefix]+=1
            print(email_counts)
            print("email_counts")
            email_full=f"{prefix}{email_counts[prefix]}@{company}.com"
        else:
            email_counts[prefix]=1
            email_full=f"{prefix}@{company}.com"

        # combine into "Name <email>"
        entry=f"{full_name} <{email_full}>"
        result.append(entry)


    return ", ".join(result)
        


print(solution("John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker", "Moringa"))


# -----STEPS TAKEN----

# prepare the company name
# split the input names
# Initialize helpers-emailcounts and results
# Loop through each name
# split the names into tow parts
# Extract the first initial
# Handle middle initial and lastname
# Clean and truncate last name
# Build the email prefix
# Handle duplicate prefixes
# Format the output string
# store result
# Join all results