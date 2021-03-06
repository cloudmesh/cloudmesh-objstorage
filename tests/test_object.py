# pytest -v --capture=no tests/test_objstorage.py
# nosetest -v --nopature
# nosetests -v --nocapture tests/test_objstorage.py

import os
from pprint import pprint

import cloudmesh.objstorage.provider.awsobjectstore.Provider
from cloudmesh.common.util import HEADING
from cloudmesh.common.util import path_expand
from pathlib import Path
from cloudmesh.common.util import writefile


class TestObject:

    def create_file(self, location, content):
        d = Path(os.path.dirname(path_expand(location)))
        print()
        print("TESTDIR:", d)

        d.mkdir(parents=True, exist_ok=True)

        writefile(path_expand(location), content)

    def setup(self):
        self.p = cloudmesh.objstorage.provider.awsobjectstore.Provider.Provider(
            service="awss3")
        print('Success')

    def test_01_create_source(self):
        # create source dir

        # BUG TODO
        self.destination = "set the destination location here and use in tests"

        self.sourcedir = path_expand("~/.cloudmesh/objstorage/test/")

        self.create_file("~/.cloudmesh/objstorage/test/stest1.pkl",
                         "content of stest1")
        self.create_file("~/.cloudmesh/objstorage/test/stest1.parquet",
                         "content of stest1")
        self.create_file("~/.cloudmesh/objstorage/test/stest1.obj",
                         "content of stest1")
        self.create_file("~/.cloudmesh/objstorage/test/stest.txt",
                         "content of stest")
        self.create_file("~/.cloudmesh/objstorage/test/stest1.txt",
                         "content of stest1")

        # test if the files are ok
        assert True

    def test_03_get(self):
        HEADING()
        src = path_expand("/test/stest1.parquet")
        print(src)
        dst = path_expand("~/test/stest1.pkl")
        print(dst)
        file = self.p.get('aws', src, dst)
        pprint(file)

        assert file is not None

    def test_02_put(self):
        HEADING()
        src = path_expand("~/abctest.pptx")
        print(src)
        # dst = path_expand("~/.cloudmesh/objstorage/test/a/b/")
        dst = "/abctest.pptx"
        print(dst)
        test_file = self.p.put('aws', src, dst)
        pprint(test_file)

        assert test_file is not None

    def test_01_create_dir(self):
        HEADING()
        src = 'created_dir123'
        directory = self.p.create_dir('aws', src)
        pprint(directory)

        assert dir is not None

    def test_04_list(self):
        HEADING()
        src = '/test'
        contents = self.p.list('aws', src)
        for c in contents:
            pprint(c)

        assert len(contents) > 0

    def test_05_search(self):
        HEADING()
        src = '/'
        filename = 'abctest.pptx'
        #
        # bug use named arguments
        #
        search_files = self.p.search('aws', src, filename, True)
        pprint(search_files)

        assert len(search_files) > 0

    def test_06_delete(self):
        HEADING()
        src = '/created_dir'
        self.p.delete('aws', src)
