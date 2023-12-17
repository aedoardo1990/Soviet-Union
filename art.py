INTRO = """
⠀⠀⢠⣤⣤⡄⢠⣤⣤⣤⠀⣤⡄⢠⣤⢀⣤⡄⣤⣤⣤⢠⣤⣤⣤⡄⠀⠀⢀⣤⡄⣤⡄⣠⣤⠀⣤⡄⣠⣤⢠⣤⣤⣤⡄⣤⡄⢠⣤⠀
⠀⠀⢸⣿⠉⠁⣾⡟⢹⣿⢠⣿⡇⣿⡏⢸⣿⢠⣿⠋⠉⠈⢹⣿⠋⠁⠀⠀⢸⣿⠀⣿⡇⣿⣿⢸⣿⠃⣿⡇⢸⣿⢹⣿⠀⣿⣿⢸⣿⠀
⠀⠀⠸⣿⣆⠀⣿⡇⣼⡿⢸⣿⠀⣿⡇⢸⣿⢸⣿⣶⡆⠀⢸⣿⠀⠀⠀⠀⢸⣿⢸⣿⠁⣿⢿⣿⣿⢀⣿⡇⣿⡇⢸⣿⢰⣿⣿⣼⡟⠀
⠀⠀⠀⢸⣿⢠⣿⠇⣿⡇⣸⣿⢸⣿⠃⣿⡇⣸⡿⠀⠀⠀⣿⡇⠀⠀⠀⠀⣿⡏⢸⣿⢸⣿⢸⣿⡟⢸⣿⠁⣿⡇⣾⡏⢸⣿⢹⣿⡇⠀
⠀⠀⠿⠿⠿⠸⠿⠿⠿⠇⠿⠿⠿⠋⠀⠿⠇⠿⠿⠿⠀⠀⠿⠇⠀⠀⠀⠀⠿⠿⠿⠟⠸⠿⠀⠿⠇⠸⠿⠸⠿⠿⠿⠇⠼⠟⠸⠿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣀⣀⣀⢀⣀⠀⣀⡀⢀⣀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⡟⣿⡿⢸⣿⢀⣿⡇⣾⣿⠘⠛⣻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⠃⣿⡇⣸⡿⢸⣿⠀⣿⡇⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⢀⣿⡇⣿⡇⢸⣿⢠⣿⡇⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣸⣿⣾⣿⠀⣿⣷⣿⡏⢸⣿⠁⣿⣷⣶⡆⠀⠀⠀⠀⠀⠀⠀⠠⢤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⠤⠀⠀⠀⠀⠀
⠀⠀⠀⠾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠟⠙⠿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠿⠋⠀⠀⠀⠀⠈⠻⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂
"""


GAGARIN = '''
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣷⣿⡿⠶⣶⣄⠠⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⡟⣭⣽⣿⣷⣝⢿⠿⣦⣀⣦⡀⠀⠀⠀⠀⠀
⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⢫⣭⣿⣷⣘⣿⣏⣿⣿⣿⣿⡿⠿⠿⠿⠦⡀⠀⠀⠀
⠀⣸⣿⣿⣿⣿⣿⣿⣿⣷⡈⠻⢏⣿⣿⣿⠿⣟⣯⣽⣶⡶⢦⣀⣀⣀⠀⠀⠀⠀
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⣽⣾⢿⣟⣭⣵⡾⢿⣛⠻⠭⠭⠆⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡵⣟⣿⣿⠿⣚⢽⣙⣦⣽⣶⣶⣦⡔⠖⢠⠄⠀⠀
⣿⣿⣿⣿⣿⣿⣿⡿⢯⣪⣷⢿⢿⡿⣮⣷⣾⣿⣿⣛⣿⣿⠿⢿⣷⠀⠀⠀⠀⠀
⡻⣿⣿⣿⣿⣿⣯⡾⡟⢝⣮⣷⡶⣾⣿⣷⣿⣻⣽⣿⠟⠁⠀⢩⣿⣷⡤⠀⠀⠀              "Dedicated to Yuri Gagarin,
⢱⣿⣿⣿⠯⠚⣕⡙⣨⣿⡿⠫⡟⣾⠋⢉⠻⣿⣿⢃⣄⣶⣶⢿⣿⡏⣷⠀⠀⠀
⣿⣿⣿⣧⠈⢀⣿⡇⣿⣿⡇⣶⣴⣴⣼⣷⣿⣿⣿⡇⢻⣿⣿⠘⣿⡇⢸⡆⠀⠀               the first cosmonaut in space."
⠹⣽⣿⣿⣧⡈⣿⡇⣿⣿⣧⢻⣿⣿⣿⣿⣿⢩⣿⣿⠜⣿⣿⢠⢿⠂⢸⡇⠀⠀
⠀⠙⠿⠿⠛⢷⣼⡇⣿⣿⣿⡀⣿⣿⣿⣿⣿⣾⣶⣶⣝⡿⡉⡌⣾⠊⣼⠀⠀⠀
⠀⠀⠀⠈⠂⠀⠙⢷⣝⢿⠿⠗⡪⣛⠻⣿⣛⠻⣯⡭⠶⠈⢡⠁⢸⣼⠟⡀⠀⠀
⠀⠀⠀⠀⠀⠀⢄⡀⠙⠻⣦⣤⡈⠛⠾⣿⡁⠀⢀⣶⣿⠃⣂⣤⠞⢩⡀⠐⠄⠀
⠀⠀⠀⠀⠀⣸⣿⣿⣦⣄⡀⠍⠛⢛⠿⢶⣶⣶⡶⠶⠞⢛⡯⣵⡇⣟⢣⠅⢰⣄
⠀⠀⠀⠀⣌⠛⣿⡇⠁⠘⣩⠻⣶⣈⢉⣅⠀⠀⠀⢴⣦⣵⣾⡿⣧⣯⠀⢀⠸⢱
⠀⣀⠀⣀⣩⣮⣴⡵⠠⣿⡷⠉⣛⣽⡿⠁⢀⣴⣶⣄⠹⣿⡿⠷⡺⢣⣷⣦⠰⠸
⣴⣿⣿⣶⣝⠿⣿⣿⡆⠛⠃⢰⣿⣭⣥⡀⢞⣿⣿⡟⠀⣾⢷⣼⣿⣾⣿⣿⣷⡆
⣶⣿⣿⣿⣮⠳⣾⣿⣇⠀⠀⠀⠹⢿⡷⣧⣆⣉⣹⣞⡻⢦⡀⠙⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣯⣎⢿⣿⣿⡷⣶⣶⣼⡶⢭⣅⢦⡦⣤⣿⣿⣿⡐⢸⣿⣧⠩⣿⣿
'''