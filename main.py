from gui import Gui

gui = Gui("data.db", "Expense tracker","1000x750")

# Display GUI
gui.build_frames()
gui.build_date()
gui.build_item_bought()
gui.build_amount_spent()
gui.build_submit_button()
gui.build_update_button()
gui.build_delete_button()
gui.build_listbox()
gui.build_remain_balance()

# Fetch data
gui.display_data()

# Run main window
gui.run_window()