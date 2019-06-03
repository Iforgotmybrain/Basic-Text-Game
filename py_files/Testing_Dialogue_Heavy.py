import SaveSystem


class SaveInit:
    def start_save(self):
        print("Starting save")
        SaveSystem.save_load.saving()
    def start_load(self):
        print('Starting load')
        SaveSystem.save_load.loading()

topdawg = SaveInit()