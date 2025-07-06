def solution(S,C):
    company =C.lower()
    names=S.split(", ")
    email_counts={}
    result=[]


    for full_name in names:
        
        parts=full_name.strip().split()
        
        

        first_initial=parts[0][0].lower()

        if len(parts)==3:
            middle_initial=parts[1][0].lower()
           
            last_name=parts[2]
            
        else:
            middle_initial=""
            last_name=parts[1]

        last_name_clean=last_name.replace("-", "").lower()
        
        last_name_trunc=last_name_clean[:8]
        

        prefix=first_initial+middle_initial+last_name_trunc

        if prefix in email_counts:
            email_counts[prefix]=email_counts[prefix]+1
            email_full=f"{prefix}{email_counts[prefix]}@{company}.com"
        else:
            email_counts[prefix]=1
            email_full=f"{prefix}@{company}.com"        
        

        

        entry=f"{full_name} <{email_full}>"
        
        result.append(entry)

        
    return ", ".join(result)


        
        
        


print(solution("John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker", "Example"))