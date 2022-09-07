def SRA_download(sample_data,sample_type,SRApath):
    """ Use: Download SRA files """
    if sample_type == "SRA":
        script_dir = SRApath + "SRA-download_"
        for X in sample_data:
            command = script_dir + X + ".sh"
            subprocess.run([command, X, SRApath])
