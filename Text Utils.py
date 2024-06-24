import math
import random
import torch

class toUpper:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "toUpper"
    # OUTPUT_NODE = True
    CATEGORY = "Utils"

    @staticmethod
    def toUpper(text):
        text = text.upper()
        return (text,)

class toLower:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {}),
            },
        }

    RETURN_TYPES = ("STRING", )
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "toUpper"
    # OUTPUT_NODE = True
    CATEGORY = "Utils"

    @staticmethod
    def toUpper(text):
        text = text.lower()
        return (text,)

class toMiddle:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING",{}),
            },
        }

    RETURN_TYPES = ("STRING", )
    #RETURN_NAMES = ("image_output_name",)
    FUNCTION = "toUpper"
    # OUTPUT_NODE = True
    CATEGORY = "Utils"

    @staticmethod
    def toUpper(text):
        text = text.title()
        return (text,)
    
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "String to Upper Case": toUpper,
    "String to Title Case": toMiddle,
    "String to Lower Case": toLower,
}