from setuptools import find_packages,setup

'''
Setuptools is a collection of enhancements to the Python distutils
that allow developers to more easily build and distribute Python packages, 
especially ones that have dependencies on other packages
'''
# find_packages fetches all the packages required for our machine learning project


HYPHEN_E_DOT= '-e .'

def get_requirements(file_path):
    """
    Read the contents of a .txt file and store each line in a Python list.
    Args:
        file_path (str): The path to the .txt file to be read.
    Returns:
        list: A list containing the lines from the file.
    """

    data_list = []  # Initialize an empty list to store the data

    try:
        with open(file_path, 'r') as file:
            # Read each line from the file and append it to the list
            for line in file:
                data_list.append(line.strip())  # Remove leading/trailing whitespace
            if HYPHEN_E_DOT in data_list:
                data_list.remove(HYPHEN_E_DOT)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data_list

# Example usage:
file_path = 'requirements.txt'  # Replace with the path to your .txt file
result = get_requirements(file_path)
# print(result)



setup(
    name="Car-price-predictor",
    version="0.0.1",
    description="A simple Machine learning end to end package that predicts the price of cars.",
    author="Nathan Berhe",
    author_email="natberhe28@gmail.com",
    maintainer="Nathan Berhe",
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn','matplotlib']  --> but it is not practical to list all the packages in a line, instead we need to create
    # a function that will read the file requirements.txt and convert it into a list of strings<--
    install_requires=result 

)
