from Jumpscale import j
import os

src = "https://github.com/threefoldtech/sandbox_osx/tree/master/base/openresty/lualib"
dest = "https://github.com/threefoldtech/sandbox_base/tree/master/base/openresty/lualib"

src_path=j.clients.git.getContentPathFromURLorPath(src)
dest_path=j.clients.git.getContentPathFromURLorPath(dest)

for item in j.sal.fs.listFilesInDir(src_path,True,filter="*.lua"):
    dest_part = j.sal.fs.pathRemoveDirPart(item, src_path)
    dest_full_path = os.path.join(dest_path,dest_part)
    j.sal.fs.createDir(j.sal.fs.getDirName(dest_full_path))
    j.sal.fs.moveFile(item,dest_full_path)

for item in j.sal.fs.listDirsInDir(src_path,True):
    if j.sal.fs.exists(item) and len(j.sal.fs.listFilesInDir(item))==0:
        j.sal.fs.remove(item)
