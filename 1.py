from difflib import SequenceMatcher
with open('demo1.txt')  as one_file ,open ('demo2.txt') as two_file,open ('demo3.txt') as three_file:
    data_file1=one_file.read()
    data_file2=two_file.read()
    data_file3=three_file.read()
    match=SequenceMatcher(None,data_file1,data_file2,data_file3).ratio()
    print(f"the plgiarized content is { round(match * 100)}%")