import utils

MODEL_FILE_INFO = r"C:\Users\kbenmus\work\Jupiter_projects\A62_projet_synthese\A62-EquipeCV\model\model_rf.pklz"

t = utils.pickle_read(MODEL_FILE_INFO)
print(t)

tt = r"C:\Users\kbenmus\work\Jupiter_projects\A62_projet_synthese\A62-EquipeCV\notebook\pickeled_function.plkz"
utils.pickle_read(tt)