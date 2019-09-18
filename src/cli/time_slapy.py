import click as c
import src.cli.time_lap_processor as menu
import src.cli.output as output

@c.command()
@c.option("--option1", prompt='Name of the raw images directory')
@c.option("--option2", prompt='Name of the new data set')
@c.option("--option3", prompt='Do you want to filter the background?', type=c.Choice(['y','n']))
def choose_create_dataset(option1,option2,option3):
    args = [option1,option2,option3]
    menu.handel_create_dataset(args)
    choose_back()

@c.command()
@c.option("--option2", prompt='Name of the data set you want to train with')
@c.option("--option1", prompt='Name of the new model')
def choose_new_model(option1,option2):
    args = [option1, None, option2]
    menu.handel_train_dataset(args)
    choose_back()

@c.command()
@c.option("--option2", prompt='Name of the data set you want to train with')
@c.option("--option3", prompt='Name of the model you want to extent')
@c.option("--option1", prompt='Name of the new model')
#[new,old,dataset]
def choose_old_model(option1,option2,option3):
    args = [option1, option3, option2]
    menu.handel_train_dataset(args)
    choose_back()

@c.command()
@c.option("--option1", prompt='Option', type=c.Choice(['new', 'old']))
def choose_new_old_model(option1):
    if option1=='old':
        output.print_old_train_intro()
        choose_old_model()
    else:
        output.print_new_train_intro()
        choose_new_model()

@c.command()
@c.option("--option1", prompt='Type in [b] to go back to main menu', type=c.Choice(['b']))
def choose_back(option1):
    main()

@c.command()
@c.option("--option", prompt='Option', type=c.Choice(['a', 'b', 'c','d']))
def choose_option(option):
    if option == 'a':
        output.print_create_intro()
        choose_create_dataset()
    elif option == 'b':
        output.print_choose_train_intro()
        choose_new_old_model()
    elif option == 'c':
        output.print_help()
        choose_back()
    elif option == 'd':
        output.print_end()

def main():
    output.print_cli_intro()
    choose_option()

if __name__ == "__main__":
        main()
