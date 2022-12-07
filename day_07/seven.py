import re
dirs, CURRENT_PATH, pathToString = {}, [], lambda x : "/" + "/".join(x[1:])
class Directory:
    def __init__(self,path:str) -> None:
        self.path, self.size, self.children = path, 0, []
    def getSubSize(self) :
        self.size += sum([ Directory.getSubSize(dirs[child]) for child in self.children])
        return self.size
with open('input') as f:
    for line in f.read().splitlines():
        if "$ cd" in line :
            path = re.search("\$ cd (.+)",line).groups()[0]
            if path == ".." :
                CURRENT_PATH.pop()
            else :
                CURRENT_PATH.append(path)
                dirs[pathToString(CURRENT_PATH)] = Directory(pathToString(CURRENT_PATH))
        elif not "$" in line :
            if "dir " in line :
                path = CURRENT_PATH + [re.search("dir (.+)",line).groups()[0]]
                dirs[pathToString(CURRENT_PATH)].children.append(pathToString(path))
            else :
                dirs[pathToString(CURRENT_PATH)].size += int(re.search("(\d+) .+",line).groups()[0])
used = dirs['/'].getSubSize()
dirs_okay = sorted([d for d in dirs.values() if d.size > used - 40000000],key=lambda x: x.size)
print(f"Size of files less than 100000 : {sum([ d.size for d in dirs.values() if d.size <= 100000])}")
print(f"Size of the smallest dir to delete : {dirs_okay[0].size}")