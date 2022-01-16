#import dill

"""
with open("dilled_function.dill", "rb") as file:
    tested_dilled_function = dill.load(file)

print(tested_dilled_function("test"))
"""

# === Charge les fonctions de pré-traitement
def preprocessing_function_loading():
    NOTEBOOK_PATH = "../notebook"
    import dill
    preprocessing_function_name_list = ["normalize_pixels", "preprocess_img"]

    preprocessing_function_name=preprocessing_function_name_list[0]
    print("Import de [" + preprocessing_function_name + "]")
    with open(NOTEBOOK_PATH + "/" + preprocessing_function_name + ".dill", "rb") as file:
        normalize_pixels = dill.load(file)
    print(normalize_pixels.__name__)

    preprocessing_function_name = preprocessing_function_name_list[1]
    print("Import de [" + preprocessing_function_name + "]")
    with open(NOTEBOOK_PATH + "/" + preprocessing_function_name + ".dill", "rb") as file:
        preprocess_img = dill.load(file)
    print(preprocess_img.__name__)

    return normalize_pixels, preprocess_img

normalize_pixels, preprocess_img = preprocessing_function_loading()
#--- Charge les fonctions de pré-traitement

print(normalize_pixels.__name__)
print(preprocess_img.__name__)
