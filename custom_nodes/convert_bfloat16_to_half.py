import torch
from comfy.nodes import NODE_CLASS_MAPPINGS, Node

class ConvertBFloat16ToHalf(Node):
    @classmethod
    def INPUT_TYPES(cls):
        # Define la entrada como un tensor
        return {
            "required": {
                "tensor_input": ("tensor",),
            }
        }

    @classmethod
    def OUTPUT_TYPES(cls):
        # Define la salida como un tensor
        return {
            "tensor_output": ("tensor",)
        }

    @classmethod
    def IS_COMPLEX(cls):
        # Esto es opcional, pero puede ayudar a que el nodo se registre correctamente
        return False

    def process(self, tensor_input):
        # Verifica y convierte el tensor a float16 si es necesario
        if tensor_input.dtype == torch.bfloat16:
            tensor_input = tensor_input.to(torch.float16)
        
        return {"tensor_output": tensor_input}

# Registrar el nodo en ComfyUI
NODE_CLASS_MAPPINGS["ConvertBFloat16ToHalf"] = ConvertBFloat16ToHalf