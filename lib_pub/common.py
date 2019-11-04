#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

def makedirs_ignore_error(path, mode=0o777):
    '''调用 os.makedirs 但忽略 OSError 类型错误'''
    try:
        os.makedirs(path, mode)
    except OSError:
        pass

    return os.path.isdir(path)

def get_repo_file(proj_type,repo_url,proj_local_path,version_id):
    if proj_type == "tar":

        wget_file_cmd = "wget %s%s" % (repo_url,version_id)
        if not os.path.exists(proj_local_path):
            os.makedirs(proj_local_path)
        else:
            pass

        if proj_local_path.startswith("/opt/tarsource/"):
            os.chdir(proj_local_path)
            print "clean up the old version ..."
            os.system("rm -rf *")
            print "clean job finished,wget the file ..."
            os.system(wget_file_cmd)
            print "wget job finished,extract file ..."
            os.system("tar xvf %s" % version_id)
            print "extract job finished ..."
        else:
            raise RuntimeError('You must config the var proj_local_path start with /opt/tarsource/')

    else:
        pass