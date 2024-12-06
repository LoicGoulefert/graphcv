import dearpygui.dearpygui as dpg

from core.nodes import AdaptativeThresholdNode, ThresholdNode

from .node_ui import NodeItem


class Editor:
    def __init__(self):
        pass

    def setup_ui(self):
        """Sets up the user interface for the node editor."""
        with dpg.viewport_menu_bar():

            with dpg.menu(label="Add"):
                dpg.add_menu_item(
                    label="Threshold", tag="Threshold", callback=self.add_node
                )
                dpg.add_menu_item(
                    label="Adaptative Threshold",
                    tag="Adaptative Threshold",
                    callback=self.add_node,
                )

        with dpg.window(
            label="GraphCV",
            tag="Primary window",
        ):
            with dpg.node_editor(label="Node Editor", tag="Node Editor"):
                pass

    def add_node(self, sender, app_data):
        """Callback to add a new node."""
        match sender:
            case "Threshold":
                node = ThresholdNode()
                NodeItem(node)
            case "Adaptative Threshold":
                NodeItem(AdaptativeThresholdNode())
            case _:
                print(f"{sender=}")
