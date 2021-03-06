# noinspection PyPep8
from cloudmesh.objstorage.provider.awsobjectstore.Provider import \
    Provider as Awss3Provider
from cloudmesh.mongo.DataBaseDecorator import DatabaseUpdate
from cloudmesh.objstorage.ObjectStorageABC import ObjectStorageABC


class Provider(ObjectStorageABC):

    def __init__(self, service=None, config="~/.cloudmesh/cloudmesh4.yaml"):
        super().__init__(service=service, config=config)

        if self.kind == "awsobjectstore":
            self.provider = Awss3Provider(service=service, config=config)
        else:
            raise ValueError(
                f"Storage provider '{self.kind}' not yet supported")

    def cm_update(self, d):

        cm = {
            'cm': {
                'kind': 'define me from d',
                'name': 'define me from d',
                'cloud': 'define me from d'
            }
        }
        d.update(cm)
        return d

    @DatabaseUpdate()
    def create_dir(self, directory=None):
        """
        creates a directory
        :param directory: the name of the directory
        :return: dict
        """
        d = self.provider.create_dir(self,
                                     directory=directory)
        d = self.cm_update(d)

        return d

    @DatabaseUpdate()
    def list(self, source=None, recursive=False):
        """
        lists the information as dict
        :param source: the source which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        d = self.provider.list(self,
                               source=source,
                               recursive=recursive)
        d = self.cm_update(d)

        return d

    @DatabaseUpdate()
    def put(self, source=None, destination=None, recursive=False):
        """
        puts the source on the service
        :param source: the source which either can be a directory or file
        :param destination: the destination which either can be a directory or
                            file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        d = self.provider.get(self,
                              source=source,
                              destination=destination,
                              recursive=recursive)
        d = self.cm_update(d)

        return d

    # not yet sure if service is needed
    @DatabaseUpdate()
    def get(self, source=None, destination=None, recursive=False):
        """
        gets the destination and copies it in source
        :param source: the source which either can be a directory or file
        :param destination: the destination which either can be a directory or
                            file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        d = self.provider.get(self,
                              source=source,
                              destination=destination,
                              recursive=recursive)

        d = self.cm_update(d)

        return d

    @DatabaseUpdate()
    def delete(self, source=None, recursive=False):
        """
        deletes the source
        :param source: the source which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        d = self.provider.delete(self,
                                 source=source,
                                 recursive=recursive)

        d = self.cm_update(d)

        return d

    def search(self, directory=None, filename=None,
               recursive=False):
        """
        gets the destination and copies it in source
        :param directory: the directory which either can be a directory or file
        :param filename: the filename
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        d = self.provider.get(self,
                              directory=directory,
                              filename=filename,
                              recursive=recursive)

        d = self.cm_update(d)

        return d
