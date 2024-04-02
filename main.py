if __name__ == "__main__":
    import init
    import os
    from window import Window

    # Initiate main window
    window_obj = Window()

    # If DB file exists, run the main window, otherwise initial window
    if os.path.isfile(window_obj.db_file):
        init.display_main_window(window_obj)
    else:
        init.display_init_window(window_obj)

    # Process window
    window_obj.display_window()