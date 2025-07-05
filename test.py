# Create a function that takes a string of names and returns each individual names' in a list

# return a list


def split_names(S):
    result=[]
    names=S.split(",")

    for name in names:
        new_name=name.strip()
        result.append(new_name)

    return result
    # remove_spaces=names.strip()
    # return remove_spaces




print(split_names("John Doe, Peter Parker, Mary Jane Watson-Parker"))
