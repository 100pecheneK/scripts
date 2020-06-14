import os


def get_commands_list():
    commands_list = []
    python_interpreter = 'python3'
    commands_list += [f'{python_interpreter} -m venv env']
    commands_list += ['source env/bin/activate']
    commands_list += ['pip install --upgrade pip']
    commands_list += ['pip install django']
    commands_list += ['pip install ipython']
    commands_list += ['pip freeze > req.txt']
    project_name = input('Project name: ')
    commands_list += [f'django-admin startproject {project_name} .']
    commands_list += ['echo']
    commands_list += [
        f'echo PLEASE TYPE: source env/bin/activate\;cd {project_name}']
    return commands_list


def get_available_commands(commands_list):
    for i, command in enumerate(commands_list[:-1]):
        commands_list[i] += ';'
    return commands_list


def get_available_commands_in_single_line(commands_list):
    commands_list = get_available_commands(commands_list)
    commands = ''
    for command in commands_list:
        commands += str(command)
    return commands


def start_commands(available_commands):
    os.system(available_commands)


def main():
    commands_list = get_commands_list()
    available_commands = get_available_commands_in_single_line(commands_list)
    start_commands(available_commands)


main()
