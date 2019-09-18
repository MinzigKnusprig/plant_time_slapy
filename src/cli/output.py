import click as c

def print_create_intro():
    """
        Display the intro header and creation mode text on console.
    """

    print_intro_header()
    c.secho('Data set creation MODE\n', fg='green',bold=True)

def print_train_intro():
    """
        Display the intro header and training mode text on console.
    """

    c.secho('\nTraining model MODE', fg='green',bold=True)

def print_cli_intro():
    """
       Display the intro header and the intro text and
       the main menu options on console.
    """

    print_intro_header()
    c.secho('A small cli programm which create and train data sets.\n', fg='green',bold=True)
    print_main_option()

def print_main_option():
    """
        Display the main menu options text on console.
    """

    c.secho('Choose between the options:')
    c.secho('├── [a]: Create a new data set')
    c.secho('├── [b]: Train with data set')
    c.secho('├── [c]: Show info')
    c.secho('└── [d]: Stop program\n')

def print_choose_train_intro():
    """
        Display the train intro and the sub menu of training text on console.
    """

    print_train_main_intro()
    c.secho('\nDo you want to use an new model or an old model for training? \n')
    c.secho('Choose between option [new] and [old]:')
    c.secho('├── [new]: Train on new model')
    c.secho('└── [old]: Train on old model\n')

def print_new_train_intro():
    """
        Display the train intro and new training text on console.
    """

    print_train_main_intro()
    c.secho('└── Training on new model.\n',fg='green')

def print_old_train_intro():
    """
        Display the train intro and old training text on console.
    """

    print_train_main_intro()
    c.secho('└── Training on old model.\n',fg='green')

def print_train_main_intro():
    """
        Display the intro header and train intro text on console.
    """
    print_intro_header()
    print_train_intro()

def print_done_msg(option):
    """
        Display task is done text on console.
    """

    msg = '\n{} DONE!\n'.format(option)
    c.secho(msg,fg='green',bold=True)

def print_intro_header():
    """
        Clear console and display the intro header text.
    """

    c.clear()
    img = """
 _______    _  _     _                _______                                      
(_______)  | || |   (_)              (_______)                 _                   
    _ _____| || |  _ _ ____   ____       _  ___  ____  _____ _| |_ ___  _____  ___ 
   | (____ | || |_/ ) |  _ \ / _  |     | |/ _ \|    \(____ (_   _) _ \| ___ |/___)
   | / ___ | ||  _ (| | | | ( (_| |     | | |_| | | | / ___ | | || |_| | ____|___ |
   |_\_____|\_)_| \_)_|_| |_|\___ |     |_|\___/|_|_|_\_____|  \__)___/|_____|___/ 
                            (_____|                                                                                                                                                                                   
"""
    c.secho(img, bold=True, fg='red')


def print_help():
    """
        Display intro header, help info and program directory structure as text on console.
    """

    print_intro_header()
    print_help_info()
    img = """
    ├── data		    
    │   ├── datasets		  - map contains created data sets
    │   ├── model_weight_dir	- map contains trained models with corresponding weights
    │   └── raw_imgs		  - map where user store images to turn into a data set
    │       
    ├── logs                    - map contains logfiles for tensorboard
    └── src
        ├── cli                 - python files for command line interface
        ├── cnn                 - python files for convolutional neronal network
        └── utils               - python files to create proper data set from raw datas
"""
    c.secho(img)

def print_help_info():
    """
        Display the help info text on console.
    """

    c.secho("Short information about the structure of the program.",fg='green',bold=True)

def print_end():
    """
        Display the end program text on console
    """

    img = """
 _______ _       _      _     
(_______|_)     (_)    | |    
 _____   _ ____  _  ___| |__  
|  ___) | |  _ \| |/___)  _ \ 
| |     | | | | | |___ | | | |
|_|     |_|_| |_|_(___/|_| |_|\n
"""
    c.secho(img, fg='red',bold=True)

def print_dataset_error_msg(dataset_name,exist):
    """
        Display data set error message text and structure where to solve the error in red on the console.
        Can be used as error message if something is not correct with the data set (exist/not exist depends on the case).
    """

    c.secho("\nERROR: The data set [{}] {}.".format(dataset_name,exist),fg='red',bold=True)
    c.secho("Please check if data set exists inside: ",fg='red',bold=True)

    img = """
    └── data		    
        └──  datasets		    - dir contains created data sets
    """
    c.secho(img, fg='red')

def print_model_error_msg(model_name,exist):
    """
        Display model/weight error message text and structure where to solve the error in red on the console.
        Can be used as error message if something is not correct with the model/weight (exist/not exist depends on the case).
    """

    c.secho("\nERROR: The model files or directory [{}] {}.".format(model_name,exist),fg='red',bold=True)
    c.secho("Please check if model files and directory exist inside: ",fg='red',bold=True)

    img = """
    └── data		    
        └──  model_weight_dir	- map contains trained models with corresponding weights
    """
    c.secho(img, fg='red')

def print_raw_dir_error_msg(raw_name,exist):
    """
        Display raw directory error message text and structure where to solve the error in red on the console.
        Can be used as error message if something is not correct with the raw directory (exist/not exist depends on the case).
    """

    c.secho("\nERROR: The raw directory [{}] {}.".format(raw_name,exist),fg='red',bold=True)
    c.secho("Please check if raw directory exists inside: ",fg='red',bold=True)

    img = """
    └── data		    
        └──  raw_imgs - map where user store images to turn into a data set
    """
    c.secho(img, fg='red')