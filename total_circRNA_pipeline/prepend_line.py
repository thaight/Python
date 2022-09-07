def prepend_line(line, prefix, version, path):
    """ Use: Insert a given line to the top of a file for submission to slurm schedulers """
    # Define name of temporary dummy file for every prefix
    for ID in prefix:
        file_name = path + "SRA-download" #NEED TO FIX THIS SO THAT YOU PARSE A VARIAB>
        temp_file = file_name + "_" + ID + ".sh"
        # Open original file in read mode and temp file in write mode
        with open(file_name, 'r') as read_obj, open(temp_file, 'w') as write_obj:
            # Write shebang line to temp file
            write_obj.write("#!/bin/bash" + '\n')
            write_obj.write("#SBATCH --job-name=" + ID + "_SRA_download" + '\n')
            for X in line:
                # Write run time parameteres for each element of line
                write_obj.write("#SBATCH " + X + '\n')
            # Write in module load information needed
            write_obj.write("#module load " + version + '\n')
            # Read lines from original file one by one and append them to the temp file
            for obj in read_obj:
                write_obj.write(obj)
            # Makes the new scripts executable
            make_executable(temp_file)
