"""Counts the number of input records that include the color purple."""


def main():
    data_directory_name = 'data'
    infile_name = 'slot_values.txt'
    do_purple_counter(data_directory_name, infile_name)


def do_purple_counter(data_directory_name, infile_name):
    infile_path_and_name = f'{data_directory_name}/{infile_name}'
    infile = open(infile_path_and_name, 'r', encoding='utf-8')
    purple_count = 0
    for line in infile:
        slot_values = line.split()
        if 'Purple' in slot_values:
            purple_count += 1
    infile.close()
    print(f'\nThere were {purple_count} records in the input file that included the color purple.')


if __name__ == '__main__':
    main()
