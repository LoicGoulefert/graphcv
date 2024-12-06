import dearpygui.dearpygui as dpg

from ui.editor import Editor


def main():
    dpg.create_context()

    editor = Editor()
    editor.setup_ui()

    dpg.create_viewport(title="GraphCV", width=1200, height=800)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary window", True)

    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
