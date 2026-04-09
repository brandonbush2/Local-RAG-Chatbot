import torch
from transformers import AutoModelForCausalLM, AutoTokenizer,BitsAndBytesConfig

MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"

def load_model():
    quant_config = BitsAndBytesConfig(
        load_in_4bit = True,
        bnb_4bit_compute_dtype = torch.bfloat16,
        bnb_4bit_use_double_quant = True,
        bnb_4bit_quant_type = "nf4",
    )
    
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        dtype = torch.bfloat16,
        quantization_config = quant_config,
        device_map = "cuda:0",
        attn_implementation = "eager",
    )

    #allow sampling flags to be passed at generation time
    model.generation_config.do_sample = True

    model.eval() #inference mode
    return tokenizer, model