from dataset_generator import DatasetGenerator


def main():
    print('Hello!')
    dataset_generator = DatasetGenerator()

    while True:
        dataset_generator()
        user_input = input('Do you want to record next command (y / n)? ')
        if user_input not in ['y', 'Y', 'yes']:
            break
    print("Thanks!")

if __name__ == '__main__':
    main()
