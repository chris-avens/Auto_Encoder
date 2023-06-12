import os.path

save_path = input('Where do you want to save the file: ')
name_of_file = input('What is the name of the file: ')
completeName = os.path.join(save_path, name_of_file+'.txt')
file1 = open(completeName, 'w')

# list here the parameters
# if there are more than two, format it like ['param1','param2','param3',...]
param_list = [['I', 'here'], ['She', 'there'], ['He', 'everywhere'], ['They', 'somehow here']]
for i in param_list:
    # write the formatting of the text inside the triple quotes '''
    # multiline is ok
    toFile = f'''{i[0]} was {i[1]}
{i[1]} was {i[0]}

'''
    file1.write(toFile)

file1.close()

