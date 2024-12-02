import dearpygui.dearpygui as dpg

from core.nodes import BaseNode


class NodeItem:
    def __init__(self, base_node: BaseNode):
        self.base_node = base_node

        width = 100

        # TODO: link, unlink callbacks
        with dpg.node(
            parent="Node Editor", label=self.base_node.label, tracked=True
        ) as node_id:
            self.node_id = node_id

            # Add inputs
            for input_label in self.base_node.inputs:
                dpg.add_node_attribute(
                    label=input_label, attribute_type=dpg.mvNode_Attr_Input
                )

            # Add outputs
            for output_label in self.base_node.outputs:
                dpg.add_node_attribute(
                    label=output_label, attribute_type=dpg.mvNode_Attr_Output
                )

            # Add static parameters
            for param_name, param_options in self.base_node.parameters.items():
                with dpg.node_attribute(
                    label=param_name,
                    attribute_type=dpg.mvNode_Attr_Static,
                ):
                    match param_options["type"]:
                        case "int":
                            dpg.add_slider_int(
                                label=param_name,
                                default_value=param_options["value"],
                                callback=self.update_parameter,
                                user_data=param_name,
                                min_value=param_options.get("min_value", None),
                                max_value=param_options.get("max_value", None),
                                width=width,
                            )
                        case "combo":
                            dpg.add_combo(
                                label=param_name,
                                default_value=param_options["value"],
                                items=param_options["options"],
                                width=width,
                            )
                        case _:
                            pass

    def update_parameter(self, sender, app_data, user_data):
        param_name = user_data
        self.base_node.parameters[param_name] = app_data
