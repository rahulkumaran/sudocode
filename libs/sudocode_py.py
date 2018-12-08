def get_code(filename):
    sudo_code = open(filename, "r")
    python_code = open(filename[0:len(filename)-4] + ".py", "w")
    for line in sudo_code:
        line_of_code = ""
        line_element = line.split()

        # adding variable in code
        if 'variable' in line_element:
            line_of_code = line_element[1] + '\n'

        python_code.write(line_of_code)
