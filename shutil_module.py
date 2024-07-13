import shutil

# print(dir(shutil))
# fol=shutil.copytree("pythontutorial","prince1")
# print(fol)
des=shutil.copy("xyz.txt","prince.txt")
print(des)
# deel=shutil.rmtree("pythontutorial")
cmd="index"
res=shutil.which(cmd)
print(res)