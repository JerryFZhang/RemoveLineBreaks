import os

input_file_name = 'file.txt'
output_file_name = 'output.txt'

with open(input_file_name, 'r') as my_input:
    print 'Reading initiated...'
    data=my_input.read().replace('\n', '')
    print 'Reading successful.'

def write ():
    with open(output_file_name, 'w') as my_output:
        print 'Writing initiated...'
        my_output.write(data)
        print 'Writing successful.'

if not os.path.isfile(output_file_name):
    print'Cannot find a file in the same directory named as %s' % output_file_name
    os.system(output_file_name)
    print'File named %s created' % output_file_name
    write()

else:

    if os.stat(output_file_name).st_size == 0:
        print'File %s is empty' %output_file_name
        write()

    else:
        input = (raw_input('There is some data in %s, are you sure to delete your existing data in %s? (y/n)' % (output_file_name,output_file_name)))

        if input =='y':
            print'Emptying the existing file...'
            open(output_file_name, 'w').close()
            print'File %s is now empty.' % output_file_name
            write()

        else:
            print 'Program teminated, user refuse to delete data in %s' % output_file_name
