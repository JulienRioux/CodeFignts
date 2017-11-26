
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].





def fileNaming(names):
    # Initialize the list of file without duplicate
    noDuplicate = []
    
    # Rename file when it's a copy of a file that already exist
    def renameDup(file):
        k = 1
        while file + "(" + str(k) + ")" in noDuplicate:
            k += 1
        return file + "(" + str(k) + ")"
    
    for i in names:
        # For every names, append to noDuplicate if there is
        # no duplicate up to date
        if i not in noDuplicate:
            noDuplicate.append(i)
        # Otherwide, append the new name of the copy of the file 
        else:
            noDuplicate.append(renameDup(i))
    
    return noDuplicate
    
