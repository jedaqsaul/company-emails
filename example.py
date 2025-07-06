# # # split

# # names="John Doe, Peter Parker, Mary Jane Watson-Parker"
# # parts=names.split(",")
# # print(parts)


# # n=' Peter Parker '
# # clean_n=n.strip()
# # print(clean_n)

# # s='Mary Jane Watson-Parker'
# # words=s.split()
# # print(words)
# # print(type(words))

# # # slice-- means take two items


# # first_two=words[:2]
# # print(first_two)

# # # " ".join(...)
# # parts=["Mary", "Jane"]
# # joined =" ".join(parts)
# # print(joined)


# # putting it all together

# # " ".join(n.strip().split()[:2])for n in names.split(', ')



# def valid_names(S):
#     final_names=[]
#     stripped_name=[]

#     names=S.split(",")
    
#     for name in names:
#         stripped_name.append(name.strip())
    
#     for s_names in stripped_name:
#         final=s_names.split()[:2]
#         final_names.append(final)
#     return final_names


# print(valid_names("John Doe, Peter Parker, Mary Jane Watson-Parker"))

# name="John Doe"
# parts = name.split()
# print(parts)


# first_letter=[]
# for part in parts:
#     first_letter.append(part[0].upper())
# print(first_letter)
# joined=''.join(first_letter)
# print(joined)
email_count={}

prefix="jdoe"

