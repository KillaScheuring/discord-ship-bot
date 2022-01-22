import os
from shutil import copyfile


def handle_setup_file(server):
    """
    Handles setting up the file for a given server
    :param server: The server sending the message
    """
    if not os.path.exists("crew_storage"):
        os.mkdir("crew_storage")
    if not os.path.exists(f"crew_storage/{server}"):
        os.mkdir(f"crew_storage/{server}")
    if not os.path.isfile(f"crew_storage/{server}/ship.json"):
        copyfile("base_files/ship.json", f"crew_storage/{server}/ship.json")
    if not os.path.isfile(f"crew_storage/{server}/crew.json"):
        copyfile("base_files/crew.json", f"crew_storage/{server}/crew.json")
    if not os.path.isfile(f"crew_storage/{server}/bounty_history.json"):
        copyfile("base_files/bounty_history.json", f"crew_storage/{server}/bounty_history.json")
