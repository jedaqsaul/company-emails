def solution(S, C):
    # prepare the company name
    company=C.lower()
    
    # split input names
    names=S.split(", ")
    

    # initialize helpers
    email_count={}

    result=[]
    # loop through each name
    for full_name in names:
        # split the names into two parts
        parts=full_name.strip().split()
        # extract the first initial
        first_initial=parts[0][0].lower()
        # Handle middle initial and last name

        if len(parts)==3:
            middle_initial=parts[1][0].lower()
            last_name=parts[2]
        else:
            middle_initial=""
            last_name=parts[1]
        # clean and truncate last name

        # clean
        last_name_clean=last_name.replace("-", "").lower()

        # truncate
        last_name_trunc=last_name_clean[:8]

        

        # Build the email prefix

        prefix=first_initial+middle_initial+last_name_trunc        
        


        # INTEREST SECTION
        # handle duplicate prefixes

        if prefix in email_count:
            email_count[prefix]+=1
            final_email=f"{prefix}{email_count[prefix]}@{company}.com"
        else:
            email_count[prefix]=1
            final_email=f"{prefix}@{company}.com"
        print(final_email)

        # format the output string
        entry=f"{full_name} <{final_email}>"

        # store the result


        result.append(entry)

        # join all results

    return ", ".join(result)




        
        


print(solution("John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker", "MoringA"))